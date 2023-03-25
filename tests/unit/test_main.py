from app import main
from app.core import flow_test

def test_main_my_favorite_function_should_return_43():
    # Acts
    with flow_test.use_native_runner():
        result = flow_test.fn(main.my_favorite_function)()

        # Assert
        assert result == 43
