import logging

from ritual_irys.cli import cli


def main() -> int:
    from nicelog import setup_logging  # type: ignore

    setup_logging()

    logging.getLogger("urllib3").setLevel(logging.CRITICAL)

    cli()
    return 0
