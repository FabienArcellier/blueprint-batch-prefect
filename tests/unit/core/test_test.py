from prefect import flow, get_run_logger

from app.core import flow_test


def test_test_flow_should_execute_the_function_relative_to_a_specific_flow():
    """
    vérifie que le helper execute bien le flow qui correspond avec les arguments.
    """
    assert flow_test.fn(_fake_flow)(12) == 12


def test_test_flow_should_handle_the_logger():
    """
    vérifie que le helper execute bien le flow qui correspond avec les arguments.
    """
    with flow_test.use_native_runner():
        assert flow_test.fn(_fake_flow_with_logger)() == 12


@flow()
def _fake_flow(arg1: int) -> int:
    return arg1

@flow()
def _fake_flow_with_logger() -> int:
    logger = get_run_logger()
    return 12
