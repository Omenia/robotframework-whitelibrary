from TestStack.White.Configuration import CoreAppXmlConfiguration
from TestStack.White.UIItems import DateFormat
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from robot.api import logger


class TimeoutKeywords(LibraryComponent):

    #This class variable lists possible date format options
    dateFormats = {"DayMonthYear":  DateFormat.DayMonthYear,
                   "DayYearMonth":  DateFormat.DayYearMonth,
                   "MonthDayYear":  DateFormat.MonthDayYear,
                   "MonthYearDay":  DateFormat.MonthYearDay,
                   "YearMonthDay":  DateFormat.YearMonthDay,
                   "YearDayMonth":  DateFormat.DayMonthYear}

    @keyword
    def set_white_busy_timeout(self, value):
        """Sets busy timeout for White Teststack

        ``value`` is integer or timeout in milli seconds.

        """

        CoreAppXmlConfiguration.Instance.BusyTimeout = int(value)
        #self.state.busyTimeout = str(test)
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

        ``value`` is integer or timeout in milli seconds.

        """

        CoreAppXmlConfiguration.Instance.FindWindowTimeout = int(value)
        #self.state.busyTimeout = str(test)
        logger.info("White FindWindowTimeout set to" + str(CoreAppXmlConfiguration.Instance.FindWindowTimeout))
        return CoreAppXmlConfiguration.Instance.FindWindowTimeout
    @keyword
    def get_white_find_window_timeout(self):
        """Gets white find window timeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.FindWindowTimeout

    @keyword
    def set_white_wait_based_on_hourglass(self, value):
        """Sets WaitBasedOnHourGlass for White Teststack

        ``value`` is boolean.

        """

        CoreAppXmlConfiguration.Instance.WaitBasedOnHourGlass = bool(value)
        #self.state.busyTimeout = str(test)
        logger.info("White WaitBasedOnHourGlass Timeout set to" + str(CoreAppXmlConfiguration.Instance.WaitBasedOnHourGlass))
        return CoreAppXmlConfiguration.Instance.WaitBasedOnHourGlass
    @keyword
    def get_white_wait_based_on_hourglass(self):
        """Gets WaitBasedOnHourGlass timeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.WaitBasedOnHourGlass

    @keyword
    def set_white_uiautomation_zero_window_bug_timeout(self, value):
        """Sets UIAutomationZeroWindowBugTimeout for White Teststack

        ``value`` is integer or timeout in milli seconds.

        """

        CoreAppXmlConfiguration.Instance.UIAutomationZeroWindowBugTimeout = int(value)
        #self.state.busyTimeout = str(test)
        logger.info("White UIAutomationZeroWindowBugTimeout set to" + str(CoreAppXmlConfiguration.Instance.UIAutomationZeroWindowBugTimeout))
        return CoreAppXmlConfiguration.Instance.UIAutomationZeroWindowBugTimeout
    @keyword
    def get_white_uiautomation_zero_window_bug_timeout(self):
        """Gets UIAutomationZeroWindowBugTimeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.UIAutomationZeroWindowBugTimeout

    @keyword
    def set_white_popup_timeout(self, value):
        """Sets PopupTimeout for White Teststack

        ``value`` is integer or timeout in milli seconds.

        """

        CoreAppXmlConfiguration.Instance.PopupTimeout = int(value)
        #self.state.busyTimeout = str(test)
        logger.info("White PopupTimeout set to" + str(CoreAppXmlConfiguration.Instance.PopupTimeout))
        return CoreAppXmlConfiguration.Instance.PopupTimeout
    @keyword
    def get_white_popup_timeout(self):
        """Gets PopupTimeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.PopupTimeout

    @keyword
    def set_white_tooltip_wait_time(self, value):
        """Sets TooltipWaitTime for White Teststack

        ``value`` is integer or timeout in milli seconds.

        """

        CoreAppXmlConfiguration.Instance.TooltipWaitTime = int(value)
        #self.state.busyTimeout = str(test)
        logger.info("White TooltipWaitTime set to" + str(CoreAppXmlConfiguration.Instance.TooltipWaitTime))
        return CoreAppXmlConfiguration.Instance.TooltipWaitTime
    @keyword
    def get_white_tooltip_wait_time(self):
        """Gets TooltipWaitTime for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.TooltipWaitTime

    @keyword
    def set_white_suggestion_list_timeout(self, value):
        """Sets SuggestionListTimeout for White Teststack

        ``value`` is integer or timeout in milli seconds.

        """

        CoreAppXmlConfiguration.Instance.SuggestionListTimeout = int(value)
        logger.info("White SuggestionListTimeout set to" + str(CoreAppXmlConfiguration.Instance.SuggestionListTimeout))
        return CoreAppXmlConfiguration.Instance.SuggestionListTimeout
    @keyword
    def get_white_suggestion_list_timeout(self):
        """Gets SuggestionListTimeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.SuggestionListTimeout

# TODO: HighlightTimeout

    @keyword
    def set_white_default_date_format(self, value):
        """Sets DefaultDateFormat for White Teststack

        ``value`` is string or date format. Format choices are following:
        DayMonthYear, DayYearMonth, MonthDayYear, MonthYearDay, YearMonthDay, YearDayMonth

        """

        if value in self.dateFormats.keys():
            CoreAppXmlConfiguration.Instance.DefaultDateFormat = self.dateFormats[value]
        else:
            logger.error("You try to set incorrect DateFormat " + str(value))

        logger.info("White DefaultDateFormat set to" + str(CoreAppXmlConfiguration.Instance.DefaultDateFormat))
        return str(CoreAppXmlConfiguration.Instance.DefaultDateFormat).replace(",", "")
    @keyword
    def get_white_default_date_format(self):
        """Gets DefaultDateFormat for White Teststack
        Returns one of the following:
        DayMonthYear, DayYearMonth, MonthDayYear, MonthYearDay, YearMonthDay, YearDayMonth

        """
        return str(CoreAppXmlConfiguration.Instance.DefaultDateFormat).replace(",", "")
