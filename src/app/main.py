import logging

from prefect import flow, get_run_logger
from prefect_streamline import deploybook # type: ignore[import]


@deploybook.register(interval=30)
@flow(name="main.myflow")
def myflow() -> int:
    logger = get_run_logger()
    logger.info("execution done")
    return 43

