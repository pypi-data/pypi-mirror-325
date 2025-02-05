#!/usr/bin/env python3
from __future__ import annotations

import importlib
import importlib.resources
import importlib.util
import logging
import os
import sys
from importlib.abc import Traversable
from pathlib import Path
from typing import Optional

import bsapi

import bsscripts

logger = logging.getLogger(__name__)

from bsscripts.commands import ExitCommand, Command
from bsscripts.commands.check_grading import (
    FindGraderCommand,
    CheckGradingProgressCommand,
    CheckGradingGroupsCommand,
)
from bsscripts.commands.distribute import DistributeCommand
from bsscripts.commands.help import HelpCommand
from bsscripts.commands.list import (
    ListUngradedCommand,
    ListUndistributedCommand,
    ListGradersCommand,
    ListDivisionCommand,
    ListDeadlinesCommand,
    ListAssignmentsCommand,
)
from bsscripts.commands.resend import ResendNotificationsCommand
from bsscripts.config import Config, SMTPConfig, load_validated
from bsscripts.course_plugin import CoursePlugin, DefaultCoursePlugin
from bsscripts.division import DivisionLog
from bsscripts.utils import read_json


class App:
    _instance: App

    def __init__(
        self,
        config: Config,
        api_config: bsapi.APIConfig,
        smtp_config: SMTPConfig,
        api: bsapi.BSAPI,
        root_path: Path,
        package_data_path: Traversable,
    ):
        self.config = config
        self.api_config = api_config
        self.smtp_config = smtp_config
        self.api = api
        self.api_helper = bsapi.helper.APIHelper(api)
        self.root_path = root_path
        self.package_data_path = package_data_path
        self.course_plugin: CoursePlugin = DefaultCoursePlugin()
        self.commands: list[Command] = []
        self.keep_running = True
        bsscripts.app.App._instance = self
        self._register_commands()

    @staticmethod
    def get_instance() -> App:
        return bsscripts.app.App._instance

    def _register_commands(self):
        self.register_command(ListAssignmentsCommand())
        self.register_command(ListDeadlinesCommand())
        self.register_command(ListDivisionCommand())
        self.register_command(ListGradersCommand())
        self.register_command(ListUndistributedCommand())
        self.register_command(ListUngradedCommand())
        self.register_command(CheckGradingGroupsCommand())
        self.register_command(CheckGradingProgressCommand())
        self.register_command(FindGraderCommand())
        self.register_command(DistributeCommand())
        self.register_command(ExitCommand())
        self.register_command(HelpCommand())
        self.register_command(ResendNotificationsCommand())

    def register_command(self, command: Command):
        for c in self.commands:
            assert not c.prefix_starts_with(
                command.prefix
            ), f'prefix "{command.prefix}" overlaps with "{c.prefix}"'
            assert not command.prefix_starts_with(
                c.prefix
            ), f'prefix "{c.prefix}" overlaps with "{command.prefix}"'

        self.commands.append(command)

    def has_distributed(self, assignment_id: str) -> bool:
        return (self.root_path / "distributions" / assignment_id).is_dir()

    def is_valid_assignment_id(self, assignment_id: str) -> bool:
        return assignment_id in self.config.assignments

    def load_division_log(self, assignment_id: str) -> DivisionLog:
        if not self.has_distributed(assignment_id):
            return DivisionLog()
        return DivisionLog.read(self.root_path / "logs" / assignment_id)

    def get_command(self, args: list[str]) -> Optional[bsscripts.commands.Command]:
        candidates = self.commands
        idx = 0

        while len(candidates) > 1 and idx < len(args):
            prefix = args[: idx + 1]
            candidates = [c for c in candidates if c.prefix_starts_with(prefix)]
            idx += 1

        if len(candidates) == 1:
            return candidates[0]
        else:
            return None

    def repl(self):
        self.keep_running = True
        while self.keep_running:
            user_input = input(f"{self.config.course_name}> ")
            args = [arg.strip() for arg in user_input.split(" ") if arg.strip()]

            command = self.get_command(args)
            if not command:
                print("Unknown command")
                continue

            command_args = args[len(command.prefix) :]
            command.execute_with_args(command_args)


def load_course_plugin(path: Path, app: App) -> CoursePlugin:
    spec = importlib.util.spec_from_file_location("bsscripts.plugin", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    course: CoursePlugin = module.create_course_plugin(app)

    return course


ROOT_ENV_VAR = "BSSCRIPTS_ROOT"
APP_ID_ENV_VAR = "BSSCRIPTS_APP_ID"
APP_KEY_ENV_VAR = "BSSCRIPTS_APP_KEY"
USER_ID_ENV_VAR = "BSSCRIPTS_USER_ID"
USER_KEY_ENV_VAR = "BSSCRIPTS_USER_KEY"


def main():
    # Set up root path as current directory, unless one is specified via the environment variable.
    if ROOT_ENV_VAR in os.environ:
        root_path = Path(os.environ[ROOT_ENV_VAR])
    else:
        root_path = Path(".")

    # Set up logging to file for INFO or above.
    # WARNING or above is also logged to standard error.
    logging.basicConfig(
        filename=(root_path / "app.log"),
        level=logging.INFO,
        encoding="utf-8",
        filemode="a",
    )
    logger = logging.getLogger(__name__)
    sh = logging.StreamHandler()
    sh.setLevel(logging.WARNING)
    logging.getLogger().addHandler(sh)

    # Attempt to load config schemas used to validate the actual configs.
    package_data_path = importlib.resources.files(bsscripts).joinpath("data")
    schema_path = package_data_path.joinpath("schema")
    api_config_schema = read_json(schema_path / "api.schema.json")
    app_config_schema = read_json(schema_path / "app.schema.json")
    smtp_config_schema = read_json(schema_path / "smtp.schema.json")

    # Attempt to load config files.
    config_path = root_path / "data" / "config"
    api_config_path = config_path / "api.json"
    app_config_path = config_path / "app.json"
    smtp_config_path = config_path / "smtp.json"

    if not api_config_path.is_file():
        logger.fatal('Could not find API config file at "%s"', api_config_path)
        sys.exit(1)

    api_config = load_validated(api_config_path, api_config_schema, bsapi.APIConfig)

    # Attempt to load app config if one exists.
    if app_config_path.is_file():
        app_config = load_validated(
            app_config_path, app_config_schema, bsscripts.config.Config
        )
    else:
        app_config = None

    # TODO: extra app config validation not captured by the schema such as checking if all grader ids are valid grader ids etc.

    # Attempt to load SMTP config if one exists.
    if smtp_config_path.is_file():
        smtp_config = load_validated(
            smtp_config_path, smtp_config_schema, bsscripts.config.SMTPConfig
        )
    else:
        smtp_config = None

    # Take application identifier and key from environment variables if set, otherwise use config ones.
    if APP_ID_ENV_VAR in os.environ:
        api_config.app_id = os.environ[APP_ID_ENV_VAR]
    if APP_KEY_ENV_VAR in os.environ:
        api_config.app_key = os.environ[APP_KEY_ENV_VAR]

    # Take user identifier and key from environment variables if set, otherwise use identity manager.
    if USER_ID_ENV_VAR in os.environ and USER_KEY_ENV_VAR in os.environ:
        user_id = os.environ[USER_ID_ENV_VAR]
        user_key = os.environ[USER_KEY_ENV_VAR]
    else:
        manager = bsapi.identity.IdentityManager.from_config(api_config)
        if not manager.load_store():
            logger.error("Failed to load identity store")
        identity = manager.get_identity(app_config.tag)
        if not identity:
            logger.fatal("No identity selected, aborting")
            sys.exit(1)
        user_id = identity.user_id
        user_key = identity.user_key

    api = bsapi.BSAPI.from_config(api_config, user_id, user_key)
    app = App(app_config, api_config, smtp_config, api, root_path, package_data_path)

    course_plugin_path = root_path / "data" / "course" / app_config.course / "plugin.py"
    if course_plugin_path.is_file():
        app.course_plugin = load_course_plugin(course_plugin_path, app)
        if not app.course_plugin.initialize():
            print("Course plugin failed to initialize")

    app.repl()


if __name__ == "__main__":
    main()
