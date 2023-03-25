import logging

from prefect import flow, get_run_logger


@flow(name="main.my_favorite_function")
def my_favorite_function() -> int:
    logger = get_run_logger()
    logger.info("execution done")
    return 43


@flow(name="main.my_favorite_function_2")
def my_favorite_function_2() -> int:
    return 45
