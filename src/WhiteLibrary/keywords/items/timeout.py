from TestStack.White.UIItems import TextBox
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from robot.api import logger


class TimeoutKeywords(LibraryComponent):
    @keyword
    def set_white_busy_timeout(self, value):
        """Sets global timeout value for Whit Teststack

        ``value`` is integer or timeout in seconds.

        """
        logger.info("White Busy Timeout set to" + str(int(value)))
