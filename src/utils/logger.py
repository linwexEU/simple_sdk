import logging


def config_logger(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s][%(levelname)s] %(module)s:%(funcName)s:%(lineno)d - %(message)s",
    )
