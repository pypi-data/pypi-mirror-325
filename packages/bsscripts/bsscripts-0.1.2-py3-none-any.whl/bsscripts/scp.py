from __future__ import annotations

import logging
import subprocess
from pathlib import Path

from bsscripts.config import Config

logger = logging.getLogger(__name__)


class SCPUploader:
    def __init__(self, dist_path: Path, logs_path: Path, config: Config):
        self.dist_path = dist_path
        self.logs_path = logs_path
        self.config = config

    def upload(self, assignment_id: str) -> bool:
        distribute = self.config.distribute
        assignment_path = self.dist_path / assignment_id
        assert (
            assignment_path.exists()
        ), f'Assignment path does not exist, wrong assignment id "{assignment_id}"?'

        # ssh DISTRIBUTER@HOST mkdir -p SHARE/<assignment_id>
        args = [
            "ssh",
            f"{distribute.distributor}@{distribute.host}",
            "mkdir",
            "-p",
            f"{distribute.share}/{assignment_id}",
        ]
        cp = subprocess.run(args, shell=False, check=False, capture_output=False)
        if cp.returncode != 0:
            logger.fatal(
                "Failed to create folder on distribution share, exit code %d",
                cp.returncode,
            )
            return False

        # ssh DISTRIBUTER@HOST mkdir -p SHARE/logs/<assignment_id>
        args = [
            "ssh",
            f"{distribute.distributor}@{distribute.host}",
            "mkdir",
            "-p",
            f"{distribute.share}/logs/{assignment_id}",
        ]
        cp = subprocess.run(args, shell=False, check=False, capture_output=False)
        if cp.returncode != 0:
            logger.fatal(
                "Failed to create logs folder on distribution share, exit code %d",
                cp.returncode,
            )
            return False

        # scp <assignment_id>/*.7z DISTRIBUTER@HOST:SHARE/<assignment_id>/
        args = f"scp {assignment_id}/*.7z {distribute.distributor}@{distribute.host}:{distribute.share}/{assignment_id}/"
        cp = subprocess.run(
            args, shell=True, check=False, capture_output=False, cwd=self.dist_path
        )
        if cp.returncode != 0:
            logger.fatal(
                "Failed to copy grader archives to distribution share, exit code %d",
                cp.returncode,
            )
            return False

        # scp <assignment_id>/*.log DISTRIBUTER@HOST:SHARE/logs/<assignment_id>/
        args = f"scp {assignment_id}/*.log {distribute.distributor}@{distribute.host}:{distribute.share}/logs/{assignment_id}/"
        cp = subprocess.run(
            args, shell=True, check=False, capture_output=False, cwd=self.logs_path
        )
        if cp.returncode != 0:
            logger.fatal(
                "Failed to copy logs to distribution share, exit code %d", cp.returncode
            )
            return False

        return True
