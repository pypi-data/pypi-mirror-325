"""
### ExceptionBase

- This module provides a base class for exceptions
- It includes various methods for formatting exceptions - simple, complex, traceback, and custom
- It will automatically capture the source code information and include it in the formatted exception

### Note
- Inherits from `Exception`
- Abstract class
- Thread safety mechanism for locking
- Properties for accessing parsed data

### Custom
- To use the custom mode, you need to provide a list of keys to be displayed in the exception.
- The list of keys can be any combination of the following:
    - time
    - filename
    - class
    - module
    - function
    - line

### Usage

```python
from book_exceptions import ExceptionBase

class MyCustomException(ExceptionBase):
    pass

# Simple usage
try:
    raise RuntimeError("Test")
except Exception as e:
    raise MyCustomException(
        message="Error occurred while performing operation",
        exception=e
    )

# Advanced usage
try:
    raise RuntimeError("Test")
except Exception as e:
    raise MyCustomException(
        message="Error occurred while performing operation",
        exception=e,
        mode= "complex"
    )

# Custom usage
try:
    raise RuntimeError("Test")
except Exception as e:
    raise MyCustomException(
        message="Error occurred while performing operation",
        exception=e,
        mode= "custom",
        list_of_keys=["time","function", "line"]
    )
```
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Standard Library
from abc import ABC
from logging import Logger
from datetime import datetime
from typing import Dict, Final, List, Literal, Any
from functools import cached_property, lru_cache
from threading import Lock
import json
import inspect
import traceback
import os
from io import StringIO

# Third-Party
from rich.console import Console
from rich.table import Table

# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------

MAP_KEYS: Final[List[str]] = ["time", "filename", "class", "module", "function", "line"]

CONSOLE: Final[Console] = Console()

# ------------------------------------------------------------------------------
# Exceptions
# ------------------------------------------------------------------------------


class ExceptionBase(Exception, ABC):
    """
    ## Base class for exceptions
        - Inherits from `Exception`
        - Abstract class
        - Locking mechanism for thread safety
        - Properties for accessing parsed data
        - Highly customizable

    ## Note
        - All parameters are optional.
        - If `exception` is not provided, it will be set to `None`.
        - All information will be automatically captured from the stack trace if not provided.

    ## Usage

    ### Simple Example
        -  To use the `ExceptionBase` class, simply create a new class that inherits from it.
        -  And uses it as a base class for your custom exception.

        ```python
            from book_exceptions import ExceptionBase

            class MyCustomException(ExceptionBase):
                pass

            # Example usage
            try:
                raise RuntimeError("Test")
            except Exception as e:
                raise MyCustomException(
                    message="Error occurred while performing operation",
                    exception=e
                )
        ```
    ### Advanced Example

    - You can also raise it with different `modes` = `simple`, `complex`, `traceback`, or `custom`.

    ```python
        from book_exceptions import ExceptionBase

        class MyCustomException(ExceptionBase):
            pass

        # Example usage
        try:
            raise RuntimeError("Test")
        except Exception as e:
            raise MyCustomException(
                message="Error occurred while performing operation",
                exception=e,
                mode= "complex"
            )
    ```
    ## Attributes
        - #### `message` | `str`
            - The message associated with the exception.
        - #### `filename` | `str`
            - The filename associated with the exception.
        - #### `class_name` | `str`
            - The class name associated with the exception.
        - #### `module_name` | `str`
            - The module name associated with the exception.
        - #### `function` | `str`
            - The function name associated with the exception.
        - #### `line` | `int`
            - The line number associated with the exception.
        - #### `exception` | `Exception`
            - The exception associated with the exception.
        - #### `mode` | `Literal["simple", "complex", "traceback", "custom"]`
            - The mode associated with the exception.
        - #### `list_of_keys` | `list[str]`
            - The list of keys to be displayed in the custom mode.
        - #### `logger` | `Logger`
            - The logger associated with the exception.
        - #### `use_rich` | `bool`
            - Whether to use rich formatting or not.
        - #### `json` | `bool`
            - Will return the additional message as a JSON string, as the sole output.
    """

    # Set slots
    __slots__ = (
        "message",
        "additional_message",
        "filename",
        "class_name",
        "module_name",
        "function",
        "line",
        "exception",
        "mode",
        "list_of_keys",
        "logger",
        "parse_dict",
        "use_rich",
        "json",
    )

    # Constructor

    def __init__(
        self,
        message: str | None = None,
        additional_message: Dict[str, Any] | None = None,
        filename: str | None = None,
        class_name: str | None = None,
        module_name: str | None = None,
        function: str | None = None,
        line: int | None = None,
        exception: Exception | None = None,
        mode: Literal["simple", "complex", "traceback", "custom"] = "simple",
        list_of_keys: list[str] | None = None,
        logger: Logger | None = None,
        use_rich: bool = False,
        json: bool = False,
    ) -> None:
        try:
            super().__init__(message)
            self.message: str = message
            self.additional_message: Dict[str, Any] | None = additional_message
            self.filename: str | None = filename
            self.class_name: str | None = class_name
            self.module_name: str | None = module_name
            self.function: str | None = function
            self.line: int | None = line
            self.exception: Exception | None = exception
            self.mode: Literal["simple", "complex", "traceback", "custom"] = mode
            self.list_of_keys: list[str] | None = list_of_keys
            self.logger: Logger | None = logger
            self.use_rich: bool = use_rich
            self.json: bool = json
            self.parse_dict: dict[str, Any] = {}
            self.lock = Lock()

            self._validated()
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while initializing ExceptionBase: {str(e)}"
            ) from e

    # Validation

    def _validated(self) -> bool:
        """Validate attributes before formatting"""
        try:

            if self.message and not isinstance(self.message, str):
                raise TypeError(f"message must be a string, got {type(self.message)}")
            if self.filename and not isinstance(self.filename, str):
                raise TypeError(f"filename must be a string, got {type(self.filename)}")
            if self.class_name and not isinstance(self.class_name, str):
                raise TypeError(
                    f"class_name must be a string, got {type(self.class_name)}"
                )
            if self.module_name and not isinstance(self.module_name, str):
                raise TypeError(
                    f"module_name must be a string, got {type(self.module_name)}"
                )
            if self.function and not isinstance(self.function, str):
                raise TypeError(f"function must be a string, got {type(self.function)}")

            if self.mode:
                if not isinstance(self.mode, str):
                    raise TypeError(f"mode must be a string, got {type(self.mode)}")
                if self.mode not in ["simple", "complex", "traceback", "custom"]:
                    raise ValueError(f"Invalid mode specified: {self.mode}")

            if self.additional_message and not isinstance(
                self.additional_message, dict
            ):
                raise TypeError(
                    f"additional_message must be a dictionary, got {type(self.additional_message)}"
                )

            if self.line and not isinstance(self.line, int):
                raise TypeError(f"line must be an integer, got {type(self.line)}")
            if self.exception and not isinstance(self.exception, Exception):
                raise TypeError(
                    f"exception must be an Exception, got {type(self.exception)}"
                )
            if self.list_of_keys and any(
                not isinstance(key, str) for key in self.list_of_keys
            ):
                raise TypeError(
                    f"list_of_keys must be a list of strings, got {type(self.list_of_keys)}"
                )
            if self.logger and not isinstance(self.logger, Logger):
                raise TypeError(f"logger must be a Logger, got {type(self.logger)}")

            return True

        except Exception as e:
            raise RuntimeError(
                f"An error occurred while validating attributes: {str(e)}"
            ) from e

    # Properties

    @cached_property
    def get_lock(self) -> Lock:
        """Get the Thread lock"""
        if not self.lock:
            self.lock = Lock()
        return self.lock

    @cached_property
    def get_formatted_simple(self) -> str:
        """Get the formatted simple message"""
        return self._simpleMessage()

    @cached_property
    def get_formatted_message(self) -> str:
        """Get the formatted message"""
        return self._formatMessage()

    @cached_property
    def get_formatted_traceback(self) -> str:
        """Get the formatted traceback"""
        return self._traceback()

    @cached_property
    def get_formatted_json(self) -> str:
        """Get the formatted JSON message"""
        return self._JSONMessage()

    @cached_property
    def get_formatted_rich(self) -> str:
        """Get the formatted rich message"""
        return self._makeTable()

    @cached_property
    def get_formatted_custom(self) -> str:
        """Get the formatted custom message"""
        return self._customMessage()

    @cached_property
    def get_formatted_json(self) -> str:
        """Get the formatted JSON message"""
        return json.dumps(self.additional_message, indent=4)

    # Magic methods

    def __str__(self) -> str:
        try:
            if self.json:
                output: str = self.get_formatted_json
                self._checkLogger(output)
                return output

            message: str = ""
            match self.mode:
                case "simple":
                    message = self.get_formatted_simple
                case "complex":
                    message = self.get_formatted_message
                case "traceback":
                    message = self.get_formatted_traceback
                case "custom":
                    message = self.get_formatted_custom
                case _:
                    raise ValueError("Invalid mode")

            self._checkLogger(message)

            if self.use_rich and self.mode != "traceback":
                return self.get_formatted_rich

            return message

        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting exception message: {str(e)}"
            ) from e

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.message!r}, {self.line!r}, {self.function!r}, {self.filename!r}, {self.exception!r})"

    # Private methods

    def _checkLogger(self, message: str | None = None) -> bool:
        """Check if logger is set and log the message"""
        try:
            if not self.logger:
                return False
            else:
                self.logger.error(message)
                return True
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while checking logger: {str(e)}"
            ) from e

    @lru_cache(maxsize=128)
    def _formatMessage(self) -> str:
        """Format the message to complex mode"""
        try:
            # Acquire lock
            with self.get_lock:

                # Capture source
                source: Dict[str, Any] = self.capture_source()

                # Format message
                if self.message:
                    string: str = f"\n====== {self.__class__.__name__} ======\n"
                    string += f"Message: {self.message}\n"
                    self.parse_dict["message"] = self.message

                if source.get("time"):
                    time = source["time"]
                    string += f"Time Stamp: {time}\n"
                    self.parse_dict["time"] = time

                if self.filename:
                    filename = self.filename
                    string += f"Filename: {filename}\n"
                    self.parse_dict["filename"] = filename
                elif source.get("filename"):
                    filename = self._formatFile(source["filename"])
                    string += f"Filename: {filename}\n"
                    self.parse_dict["filename"] = filename

                if self.class_name:
                    class_name = self.class_name
                    string += f"Class: {class_name}\n"
                    self.parse_dict["class"] = class_name
                elif source.get("class"):
                    class_name = source["class"]
                    string += f"Class: {class_name}\n"
                    self.parse_dict["class"] = class_name

                if self.module_name:
                    module_name = self.module_name
                    string += f"Module: {module_name}\n"
                    self.parse_dict["module"] = module_name
                elif source.get("module"):
                    module_name = source["module"]
                    string += f"Module: {module_name}\n"
                    self.parse_dict["module"] = module_name

                if self.function:
                    function = self.function
                    string += f"Function: {function}\n"
                    self.parse_dict["function"] = function
                elif source.get("function"):
                    function = source["function"]
                    string += f"Function: {function}\n"
                    self.parse_dict["function"] = function

                if self.line:
                    line = self.line
                    string += f"Line: {line}\n"
                    self.parse_dict["line"] = line
                elif source.get("line"):
                    line = source["line"]
                    string += f"Line: {line}\n"
                    self.parse_dict["line"] = line

                if self.exception:
                    string += self._handleException()

                if self.additional_message:
                    string += "\n\n====== Additional Information ======\n"
                    for key, value in self.additional_message.items():
                        string += f"{key}: {value}\n"
                    self.parse_dict["additional_message"] = self.additional_message

                return string
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting message: {str(e)}"
            ) from e

    @lru_cache(maxsize=128)
    def _formatFile(self, filename: str) -> str:
        """Format the filename"""
        try:
            return os.path.basename(filename)
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting filename: {str(e)}"
            ) from e

    @lru_cache(maxsize=128)
    def _traceback(self) -> str:
        """Format the traceback"""
        try:
            # Acquire lock
            with self.get_lock:
                if self.exception:
                    # Get formatted exception information
                    header: str = "\n\n====== Traceback ======\n"
                    tb_lines = traceback.format_exception(
                        type(self.exception),
                        self.exception,
                        self.exception.__traceback__,
                    )
                    footer: str = "\n\n====== End of Traceback ======\n"
                    string: str = "".join(tb_lines).strip()
                    return header + string + footer
                return self._formatMessage()
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting traceback: {str(e)}"
            ) from e

    @lru_cache(maxsize=128)
    def _customMessage(self) -> str:
        """Format the custom message"""
        try:
            # Acquire lock
            with self.get_lock:

                # Check if list_of_keys is provided
                if not self.list_of_keys:
                    raise ValueError(
                        "list_of_keys must be specified if custom message is used"
                    )

                # Output string
                string: str = ""

                if self.message:
                    string: str = f"Message: {self.message}\n"
                    self.parse_dict["message"] = self.message

                # Get source information
                source: Dict[str, Any] = self.capture_source()

                for key in self.list_of_keys:
                    if key in MAP_KEYS:
                        if key == "time":
                            string += f"Time Stamp: {source['time']}\n"
                            self.parse_dict["time"] = source["time"]

                        elif key == "filename":
                            if self.filename:
                                string += f"Filename: {self.filename}\n"
                                self.parse_dict["filename"] = self.filename
                            elif source.get("filename"):
                                string += f"Filename: {self._formatFile(source['filename'])}\n"
                                self.parse_dict["filename"] = self._formatFile(
                                    source["filename"]
                                )

                        elif key == "class":
                            if self.class_name:
                                string += f"Class: {self.class_name}\n"
                                self.parse_dict["class"] = self.class_name
                            elif source.get("class"):
                                string += f"Class: {source['class']}\n"
                                self.parse_dict["class"] = source["class"]

                        elif key == "module":
                            if self.module_name:
                                string += f"Module: {self.module_name}\n"
                                self.parse_dict["module"] = self.module_name
                            elif source.get("module"):
                                string += f"Module: {source['module']}\n"
                                self.parse_dict["module"] = source["module"]

                        elif key == "function":
                            if self.function:
                                string += f"Function: {self.function}\n"
                                self.parse_dict["function"] = self.function
                            elif source.get("function"):
                                string += f"Function: {source['function']}\n"
                                self.parse_dict["function"] = source["function"]

                        elif key == "line":
                            if self.line:
                                string += f"Line: {self.line}\n"
                                self.parse_dict["line"] = self.line
                            elif source.get("line"):
                                string += f"Line: {source['line']}\n"
                                self.parse_dict["line"] = source["line"]
                    else:
                        raise ValueError(f"Invalid key specified: {key}")

                if self.exception:
                    string += f"Exception: {self.exception.__class__.__name__}\n"
                    self.parse_dict["exception"] = self.exception.__class__.__name__
                    string += self._handleException()
                    self.parse_dict["error_message"] = (
                        str(self.exception.args[0]) if self.exception.args[0] else ""
                    )

                if self.additional_message:
                    string += "\n\n====== Additional Information ======\n"
                    for key, value in self.additional_message.items():
                        string += f"{key}: {value}\n"
                        self.parse_dict[key] = value

                header = f"\n====== {self.__class__.__name__} ======\n"

                # Memory cleanup
                del source

                # Return formatted string
                return header + string

        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting custom message: {str(e)}"
            ) from e

    @lru_cache(maxsize=128)
    def _handleException(self) -> str:
        """Handle the exception"""
        try:

            if self.exception:
                string: str = ""
                if issubclass(type(self.exception), ExceptionBase):
                    string += "\n====== Chain of Exceptions ======\n"
                    string += f"{self.__class__.__name__} -> {self.exception.__class__.__name__}\n"
                    self.parse_dict["chain_of_exceptions"] = (
                        f"{self.__class__.__name__} -> {self.exception.__class__.__name__}"
                    )

                    # Pass list_of_keys to chained exception
                    self.exception.list_of_keys = self.list_of_keys
                    self.exception.mode = self.mode

                    if self.mode == "simple":
                        string += self.exception._simpleMessage()

                    elif self.mode == "complex":
                        string += self.exception._formatMessage()

                    elif self.mode == "traceback":
                        string += self.exception._traceback()

                    elif self.mode == "custom":
                        string += self.exception._customMessage()

                    for name, data in self.exception.parse_dict.items():
                        if name == "additional_message":
                            for key, value in data.items():
                                self.parse_dict[
                                    f"{self.exception.__class__.__name__}_{key}"
                                ] = value
                        else:
                            self.parse_dict[
                                f"{self.exception.__class__.__name__}_{name}"
                            ] = data

                else:
                    string += "Error Message: " + str(self.exception)
                    self.parse_dict["exception"] = self.exception.__class__.__name__

                return string
            return ""
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting exception: {str(e)}"
            ) from e

    @lru_cache(maxsize=128)
    def _simpleMessage(self) -> str:
        """Format the simple message"""
        try:
            # Acquire lock
            with self.get_lock:

                string: str
                string = f"\n====== {self.__class__.__name__} ======\n"
                if self.message:
                    string += f"Message: {self.message}\n"

                if self.exception:
                    string += f"Exception: {self.exception.__class__.__name__}\n"

                if not issubclass(
                    type(self.exception), ExceptionBase
                ) and not issubclass(type(self), ExceptionBase):
                    string += f"Error Message: {str(self.exception)}\n"

                self.parse_dict: dict[str, Any] = {
                    "message": self.message,
                    "exception": self.exception.__class__.__name__,
                }

                if not self.use_rich:
                    self.parse_dict["error_message"] = (
                        str(self.exception.args[0]) if self.exception.args[0] else ""
                    )

                string += self._handleException()

                if self.additional_message:
                    string += "\n\n====== Additional Information ======\n"
                    for key, value in self.additional_message.items():
                        string += f"{key}: {value}\n"
                    self.parse_dict["additional_message"] = self.additional_message

                return string
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting simple message: {str(e)}"
            ) from e

    @lru_cache(maxsize=128)
    def _JSONMessage(self) -> str:
        """Format the JSON message"""
        try:
            # Acquire lock
            with self.get_lock:

                # Get Source
                source: Dict[str, Any] = self.capture_source()

                json_dict: Dict[str, Any] = {
                    "message": self.message,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "filename": self._formatFile(
                        self.filename if self.filename else source["filename"]
                    ),
                    "class": self.class_name if self.class_name else source["class"],
                    "module": (
                        self.module_name if self.module_name else source["module"]
                    ),
                    "function": self.function if self.function else source["function"],
                    "line": self.line if self.line else source["line"],
                }
                if self.exception:

                    if issubclass(type(self.exception), ExceptionBase):
                        json_dict["chain_of_exceptions"] = (
                            f"{self.__class__.__name__} -> {self.exception.__class__.__name__}"
                        )
                        json_dict["exception"] = self.exception.__class__.__name__
                        json_dict["exception_message"] = str(self.exception.message)
                        json_dict["error_type"] = (
                            self.exception.exception.__class__.__name__
                        )
                        json_dict["error_message"] = str(self.exception.exception)
                    else:
                        json_dict["exception"] = self.exception.__class__.__name__
                        json_dict["exception_message"] = (
                            str(self.exception.args[0])
                            if self.exception.args[0]
                            else ""
                        )

                if self.additional_message:
                    for key, value in self.additional_message.items():
                        json_dict[key] = value

                json_string: str = json.dumps(json_dict, indent=4)
                return json_string
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting JSON message: {str(e)}"
            ) from e

    @lru_cache(maxsize=128)
    def _makeTable(self) -> str:
        """Format the table"""
        try:
            # Acquire lock
            with self.get_lock:
                # String stream
                string_io = StringIO()
                console = Console(file=string_io)

                # Define common key order
                key_order = [
                    "message",
                    "time",
                    "filename",
                    "class",
                    "module",
                    "function",
                    "line",
                    "exception",
                    "error_message",
                    "chain_of_exceptions",
                ]

                # Create and populate table
                table = Table(title=self.__class__.__name__, title_style="bold")
                table.add_column("Key", style="bold")
                table.add_column("Value")

                # Add rows for main exception
                for key in key_order:
                    if key in self.parse_dict:
                        table.add_row(str(key), str(self.parse_dict[key]))

                # Add any additional message items
                if "additional_message" in self.parse_dict:
                    for key, value in self.parse_dict["additional_message"].items():
                        table.add_row(str(key), str(value))

            # Print main table
            console.print(table)
            console.print("\n")

            # Create chained exception table if exists
            if hasattr(self.exception, "parse_dict"):
                table2 = Table(
                    title=self.exception.__class__.__name__, title_style="bold"
                )
                table2.add_column("Key", style="bold")
                table2.add_column("Value")

                # Add rows in same order for chained exception
                for key in key_order:
                    if key in self.exception.parse_dict:
                        table2.add_row(str(key), str(self.exception.parse_dict[key]))

                # Add any additional message items from chained exception
                if "additional_message" in self.exception.parse_dict:
                    for key, value in self.exception.parse_dict[
                        "additional_message"
                    ].items():
                        table2.add_row(str(key), str(value))

                console.print(table2)

            output = string_io.getvalue()
            string_io.close()

            return output

        except Exception as e:
            raise RuntimeError(
                f"An error occurred while formatting table: {str(e)}"
            ) from e

    # Public methods

    @lru_cache(maxsize=128)
    def capture_source(self) -> Dict[str, Any]:
        """Capture the source information"""
        try:
            current_frame = inspect.currentframe()
            calling_frame = current_frame.f_back if current_frame else None
            code_obj = calling_frame.f_code if calling_frame else None

            line_number: int
            func_name: str

            if self.exception:
                # Get the traceback information from the provided exception
                tb = traceback.extract_tb(self.exception.__traceback__)
                if tb:
                    last_trace = tb[-1]
                    line_number = last_trace.lineno
                    func_name = last_trace.name

                else:
                    line_number = None
                    func_name = None

            time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            source: Dict[str, Any] = {
                "time": time,
                "class": self.__class__.__name__ if self.__class__ else None,
                "module": self.__class__.__module__ if self.__class__ else None,
                "function": func_name if func_name else None,
                "filename": code_obj.co_filename if code_obj else None,
                "line": line_number if line_number else None,
            }
            return source
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while capturing source: {str(e)}"
            ) from e


# ------------------------------------------------------------------------------
# Example Usage
# ------------------------------------------------------------------------------

# Test Exceptions


class BookValidationException(ExceptionBase):
    """Raised when a book is not valid."""

    pass


class CBookSecurityException(ExceptionBase):
    """Custom exception for security purposes."""

    pass


def do_something(num1: int, num2: int) -> int:
    try:
        return num1 + num2
    except Exception as e:
        raise BookValidationException(
            message="Error performing validation operation", exception=e
        )


if __name__ == "__main__":

    print("Example Usage:")

    # Example usage
    try:
        print("Testing do_something")
        result = do_something(1, "5")
    except Exception as e:
        raise CBookSecurityException(
            message="Security error occurred while performing operation",
            exception=e,
            mode="complex",
        )


"""Output:
CBookSecurityException:
====== CBookSecurityException ======
Message: Security error occurred while performing operation
Time Stamp: 2025-02-05 22:45:05
Filename: book_exceptions.py
Class: CBookSecurityException
Module: __main__
Function: do_something
Line: 356
Exception: BookValidationException
Error Message: Error performing validation operation

====== Chain of Exceptions ======
CBookSecurityException -> BookValidationException

====== BookValidationException ======
Message: Error performing validation operation
Time Stamp: 2025-02-05 22:45:05
Filename: book_exceptions.py
Class: BookValidationException
Module: __main__
Function: do_something
Line: 354
Exception: TypeError
Error Message: unsupported operand type(s) for +: 'int' and 'str'
"""
