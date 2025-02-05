import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Optional

import bsapi
import bsapi.helper
import bsapi.types

logger = logging.getLogger(__name__)


class Command(ABC):
    @dataclass
    class Argument:
        name: str
        help: str
        validator: Optional[Callable[[str], bool]]

    def __init__(self, prefix: list[str], description: str):
        self.prefix = prefix
        self.description = description
        self.positional_args: list[Command.Argument] = []
        self.flag_args: list[Command.Argument] = []
        self.positional_values: list[str] = []
        self.flag_values: dict[str, bool] = dict()
        self.args: list[str] = []

    def prefix_starts_with(self, prefix: list[str]) -> bool:
        return len(prefix) <= len(self.prefix) and self.prefix[: len(prefix)] == prefix

    def add_positional_arg(
        self, name: str, help_: str, validator: Callable[[str], bool] = None
    ):
        self.positional_args.append(Command.Argument(name, help_, validator))

    def add_flag_arg(self, name: str, help_: str):
        assert not any(f.name == name for f in self.flag_args), "flag already exists"

        self.flag_args.append(Command.Argument(name, help_, None))

    def get_positional_arg(self, index: int) -> str:
        assert 0 <= index < len(self.positional_values), "invalid index"

        return self.positional_values[index]

    def get_flag_arg(self, name: str) -> bool:
        assert name in self.flag_values, "unknown flag"

        return self.flag_values[name]

    def parse_args(self, args: list[str]) -> bool:
        self.args = args

        self.positional_values = []
        for idx, arg in enumerate(self.positional_args):
            if idx >= len(args):
                logger.error(
                    'Missing positional argument "%s" at index %d', arg.name, idx
                )
                return False
            if arg.validator and not arg.validator(args[idx]):
                logger.error(
                    'Value "%s" is not valid for argument "%s"', args[idx], arg.name
                )
                return False
            self.positional_values.append(args[idx])

        leftover_args = args[len(self.positional_args) :]
        self.flag_values = {
            f.name: (f"--{f.name}" in leftover_args) for f in self.flag_args
        }

        return True

    @abstractmethod
    def execute(self):
        pass

    def execute_with_args(self, args: list[str]):
        if self.parse_args(args):
            self.execute()


class AppCommand(Command, ABC):
    def __init__(self, prefix: list[str], description: str):
        super().__init__(prefix, description)
        from bsscripts.app import App

        self.app = App.get_instance()


class APICommand(AppCommand):
    def __init__(self, prefix: list[str], description: str):
        super().__init__(prefix, description)
        self.api = self.app.api
        self.api_helper = self.app.api_helper
        self.config = self.app.config

    @abstractmethod
    def execute_api(self):
        pass

    def execute(self):
        try:
            self.execute_api()
        except bsapi.APIError as e:
            logger.error(
                'Failed to execute command "%s" due to API error: %s',
                " ".join(self.prefix),
                e.cause,
            )


class ExitCommand(AppCommand):
    def __init__(self):
        super().__init__(["exit"], "Exit application")

    def execute(self):
        self.app.keep_running = False
