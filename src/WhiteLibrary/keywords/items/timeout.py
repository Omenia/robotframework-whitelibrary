from TestStack.White.Configuration import CoreAppXmlConfiguration
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from robot.api import logger


class TimeoutKeywords(LibraryComponent):
    @keyword
    def set_white_busy_timeout(self, value):
        """Sets global timeout value for Whit Teststack

        ``value`` is integer or timeout in seconds.

        """

        CoreAppXmlConfiguration.Instance.BusyTimeout = int(value)
        #self.state.busyTimeout = str(test)
        logger.info("White Busy Timeout set to" + str(CoreAppXmlConfiguration.Instance.BusyTimeout))
        return CoreAppXmlConfiguration.Instance.BusyTimeout

    @keyword
    def get_white_busy_timeout(self):
        """Sets global timeout value for Whit Teststack

        ``value`` is integer or timeout in seconds.

        """
        return CoreAppXmlConfiguration.Instance.BusyTimeout


