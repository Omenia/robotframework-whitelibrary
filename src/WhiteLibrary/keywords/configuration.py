from TestStack.White.Configuration import CoreAppXmlConfiguration
from TestStack.White.UIItems import DateFormat
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from robot.api import logger


class WhiteConfigurationKeywords(LibraryComponent):

    @keyword
    def set_white_busy_timeout(self, value):
        """Sets busy timeout for White Teststack

        ``value`` is integer or timeout in milli seconds. Default is 5000.

        """

        CoreAppXmlConfiguration.Instance.BusyTimeout = int(value)
        logger.info("White Busy Timeout set to" + str(CoreAppXmlConfiguration.Instance.BusyTimeout))
        return CoreAppXmlConfiguration.Instance.BusyTimeout
    @keyword
    def get_white_busy_timeout(self):
        """Gets busy timeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.BusyTimeout

    @keyword
    def set_white_find_window_timeout(self, value):
        """Sets find window timeout for White Teststack

        ``value`` is integer or timeout in milli seconds. Default is 30000.

        """

        CoreAppXmlConfiguration.Instance.FindWindowTimeout = int(value)
        logger.info("White FindWindowTimeout set to" + str(CoreAppXmlConfiguration.Instance.FindWindowTimeout))
        return CoreAppXmlConfiguration.Instance.FindWindowTimeout
    @keyword
    def get_white_find_window_timeout(self):
        """Gets white find window timeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.FindWindowTimeout

    @keyword
    def set_white_double_click_interval(self, value):
        """Sets DoubleClickInterval for White Teststack

        ``value`` is integer. DoubleClickInterval adds delay in double click action between clicks. Value is milliseconds. Default value is 0.

        """

        CoreAppXmlConfiguration.Instance.DoubleClickInterval = int(value)
        logger.info("White MaxElementSearchDepth set to" + str(CoreAppXmlConfiguration.Instance.DoubleClickInterval))
        return CoreAppXmlConfiguration.Instance.DoubleClickInterval
    @keyword
    def get_white_double_click_interval(self):
        """Gets DoubleClickInterval for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.DoubleClickInterval
