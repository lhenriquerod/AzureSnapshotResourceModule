"""Module created to generate an error message."""
import logging

class ExceptionError:
    """Class created to generate an error message."""

    def __init__(self):
        """"""
        logging.basicConfig(level=logging.INFO)
        self.__logger = logging.getLogger(__name__)

    def exception_error(self, method: str, exception: str):
        """Mothod created to generate an error message."""
        called_method = method
        exception_error = exception

        return self.__logger.error(f"Called Method: {called_method}(). Error: {exception_error}. %s")
