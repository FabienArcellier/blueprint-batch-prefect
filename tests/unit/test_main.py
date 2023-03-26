from app import main

from prefect_streamline import flowtest

def test_main_my_favorite_function_should_return_43():
    # Acts
    with flowtest.use_native_runner():
        result = flowtest.fn(main.myflow)()

        # Assert
        assert result == 43
