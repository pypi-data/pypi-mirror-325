"""
## Unit tests for the exception module
    - Test exception classes
    - Test exception modes
    - Test exception chaining
    - Test exception initialization

## Test cases
    - ### Function tests
        - test_exception_function
        - test_complex_exception
        - test_custom_exception
        - test_additional_message
        - test_rich_formatting
        - test_exception_chaining
        - test_exception_modes

    - ### Class tests
        - test_exception_class

    - ### Edge cases
        - test_edge_cases
        - test_edge_cases_initialization
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.module_exceptions import ExceptionBase

import pytest

# ------------------------------------------------------------------------------
# Test
# ------------------------------------------------------------------------------


class ClassException(ExceptionBase):
    """Exception class for classes"""

    pass


class FunctionException(ExceptionBase):
    """Exception class for functions"""

    pass


class ChainedException(ExceptionBase):
    """Exception for testing chaining"""

    pass


class MyClass:
    """Class for testing"""

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def square(x: int) -> int:
        """Function for testing"""
        if x < 0:
            raise ValueError("x must be positive")
        return x * x


# Function tests


def test_exception_function():
    """Test exception class"""
    try:
        raise RuntimeError("Runtime test error")
    except RuntimeError as e:
        with pytest.raises(FunctionException) as exc_info:
            raise FunctionException(
                "Test exception class", exception=e, mode="simple"
            ) from e

        error_msg = str(exc_info.value)
        assert "Runtime test error" in error_msg
        assert "RuntimeError" in error_msg
        assert "FunctionException" in error_msg


def test_complex_exception():
    """Test complex exception formatting"""
    try:
        raise ValueError("Original error")
    except ValueError as e:
        with pytest.raises(FunctionException) as exc_info:
            raise FunctionException(
                message="Test complex message", exception=e, mode="complex"
            )

        error_msg = str(exc_info.value)
        assert "Original error" in error_msg
        assert "Filename:" in error_msg
        assert "Line:" in error_msg
        assert "Function:" in error_msg
        assert "Time Stamp:" in error_msg


def test_custom_exception():
    """Test custom exception formatting"""
    custom_keys = ["time", "filename", "function", "line"]
    try:
        raise ValueError("Original error")
    except ValueError as e:
        with pytest.raises(FunctionException) as exc_info:
            raise FunctionException(
                message="Test custom message",
                exception=e,
                mode="custom",
                list_of_keys=custom_keys,
            )

        error_msg = str(exc_info.value)
        assert "ValueError" in error_msg
        assert "Time Stamp:" in error_msg
        assert "Function:" in error_msg
        assert "Line:" in error_msg
        assert "Filename:" in error_msg
        assert "Secondary error" not in error_msg


def test_additional_message():
    """Test additional message functionality"""
    additional_info = {"user": "test_user", "operation": "test_operation"}

    try:
        raise ValueError("Original error")
    except ValueError as e:
        with pytest.raises(FunctionException) as exc_info:
            raise FunctionException(
                message="Test message", exception=e, additional_message=additional_info
            )

        error_msg = str(exc_info.value)
        assert "Additional Information" in error_msg
        assert "user: test_user" in error_msg
        assert "operation: test_operation" in error_msg


def test_rich_formatting():
    """Test rich output formatting"""
    try:
        raise ValueError("Original error")
    except ValueError as e:
        exc = FunctionException(
            message="Test rich formatting", exception=e, use_rich=True
        )

        rich_output = str(exc)
        assert "│" in rich_output  # Table border character


def test_exception_chaining():
    """Test exception chaining functionality"""
    try:
        try:
            raise ValueError("Original error")
        except ValueError as e:
            raise ChainedException("First chain", exception=e)
    except ChainedException as e:
        with pytest.raises(FunctionException) as exc_info:
            raise FunctionException("Second chain", exception=e)

        error_msg = str(exc_info.value)
        assert "Second chain" in error_msg
        assert "First chain" in error_msg
        assert "Original error" in error_msg


@pytest.mark.parametrize("mode", ["simple", "complex", "traceback", "custom"])
def test_exception_modes(mode):
    """Test all exception modes"""
    try:
        raise ValueError("Value error")
    except ValueError as e:
        with pytest.raises(FunctionException):
            raise FunctionException(
                message=f"Test {mode} mode",
                exception=e,
                mode=mode,
                list_of_keys=["time", "line"] if mode == "custom" else None,
            )


# Class tests


def test_exception_class():
    """Test exception class"""
    try:
        MyClass("test").square(-1)
    except ValueError as e:
        with pytest.raises(ClassException) as exc_info:
            raise ClassException(
                message="Test exception class", exception=e, mode="complex"
            )

        error_msg = str(exc_info.value)
        assert "x must be positive" in error_msg
        assert "ClassException" in error_msg


# Edge cases


@pytest.mark.parametrize(
    "message, additional_message, filename, class_name, function_name, line, mode, expected_exception, expected_message",
    [
        (
            77,
            None,
            None,
            None,
            None,
            None,
            "simple",
            RuntimeError,
            "message must be a string",
        ),
        (
            "My message",
            "Car",
            None,
            None,
            None,
            None,
            "simple",
            RuntimeError,
            "additional_message must be a dictionary",
        ),
        (
            "My message",
            None,
            (55.70, 44),
            None,
            None,
            None,
            "simple",
            RuntimeError,
            "filename must be a string",
        ),
        (
            "My message",
            None,
            None,
            22,
            None,
            None,
            "simple",
            RuntimeError,
            "class_name must be a string",
        ),
        (
            "My message",
            None,
            None,
            None,
            [55, 20],
            None,
            "simple",
            RuntimeError,
            "function must be a string",
        ),
        (
            "My message",
            None,
            None,
            None,
            None,
            "77",
            "simple",
            RuntimeError,
            "line must be an integer",
        ),
        (
            "My message",
            None,
            None,
            None,
            None,
            None,
            "invalid_mode",
            RuntimeError,
            "Invalid mode",
        ),
    ],
)
def test_edge_cases(
    message,
    additional_message,
    filename,
    class_name,
    function_name,
    line,
    mode,
    expected_exception,
    expected_message,
):
    """Test edge cases for ExceptionBase"""
    try:
        raise RuntimeError("Test exception")
    except Exception as e:
        with pytest.raises(expected_exception) as exc_info:
            raise FunctionException(
                message=message,
                additional_message=additional_message,
                filename=filename,
                class_name=class_name,
                function=function_name,
                line=line,
                exception=e,
                mode=mode,
            )

        assert expected_message in str(exc_info.value)


@pytest.mark.parametrize(
    "message, additional_message, filename, class_name, function_name, line, mode, expected_exception, expected_message",
    [
        (
            77,
            None,
            None,
            None,
            None,
            None,
            "simple",
            RuntimeError,
            "message must be a string",
        ),
        (
            "My message",
            "Car",
            None,
            None,
            None,
            None,
            "simple",
            RuntimeError,
            "additional_message must be a dictionary",
        ),
        (
            "My message",
            None,
            (55.70, 44),
            None,
            None,
            None,
            "simple",
            RuntimeError,
            "filename must be a string",
        ),
        (
            "My message",
            None,
            None,
            22,
            None,
            None,
            "simple",
            RuntimeError,
            "class_name must be a string",
        ),
        (
            "My message",
            None,
            None,
            None,
            [55, 20],
            None,
            "simple",
            RuntimeError,
            "function must be a string",
        ),
        (
            "My message",
            None,
            None,
            None,
            None,
            "77",
            "simple",
            RuntimeError,
            "line must be an integer",
        ),
        (
            "My message",
            None,
            None,
            None,
            None,
            None,
            "invalid_mode",
            RuntimeError,
            "Invalid mode",
        ),
    ],
)
def test_edge_cases_initialization(
    message,
    additional_message,
    filename,
    class_name,
    function_name,
    line,
    mode,
    expected_exception,
    expected_message,
):
    """Test edge cases for ExceptionBase initialization"""
    try:
        obj: FunctionException = FunctionException(
            message=message,
            additional_message=additional_message,
            filename=filename,
            class_name=class_name,
            function=function_name,
            line=line,
            exception=TypeError("Test exception"),
            mode=mode,
        )
    except Exception as e:
        with pytest.raises(expected_exception) as exc_info:
            raise e

        assert expected_message in str(exc_info.value)


# ------------------------------------------------------------------------------
# End of tests
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    pytest.main(["-v", __file__])
