import sys
from pathlib import Path

from loguru import logger


def setup_logging() -> None:
    from .project import maybe_find_docode_project_dir

    project_dir = Path(maybe_find_docode_project_dir() or Path.cwd())
    ws_port_path = Path(project_dir) / "build" / "log" / "_server.log"
    logger.remove()
    _format = "{time:HH:mm:ss} | {level: <8} | {message}"
    logger.add(sys.stdout, level="INFO", colorize=True, format=_format)
    logger.add(ws_port_path, level="DEBUG", format=_format)
