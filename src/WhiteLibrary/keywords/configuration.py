from TestStack.White.Configuration import CoreAppXmlConfiguration
from TestStack.White.UIItems import DateFormat
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from robot.api import logger


class WhiteConfigurationKeywords(LibraryComponent):

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
    def set_white_wait_based_on_hourglass(self, value):
        """Sets WaitBasedOnHourGlass for White Teststack

        ``value`` is boolean. Description: TODO. Default is true.

        """

        CoreAppXmlConfiguration.Instance.WaitBasedOnHourGlass = bool(value)
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

        ``value`` is integer or timeout in milli seconds. Default is 5000.

        """

        CoreAppXmlConfiguration.Instance.UIAutomationZeroWindowBugTimeout = int(value)
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

        ``value`` is integer or timeout in milli seconds. Default is 5000.

        """

        CoreAppXmlConfiguration.Instance.PopupTimeout = int(value)
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

        ``value`` is integer or timeout in milli seconds. Default is 3000.

        """

        CoreAppXmlConfiguration.Instance.TooltipWaitTime = int(value)
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

        ``value`` is integer or timeout in milli seconds. Default is 3000.

        """

        CoreAppXmlConfiguration.Instance.SuggestionListTimeout = int(value)
        logger.info("White SuggestionListTimeout set to" + str(CoreAppXmlConfiguration.Instance.SuggestionListTimeout))
        return CoreAppXmlConfiguration.Instance.SuggestionListTimeout
    @keyword
    def get_white_suggestion_list_timeout(self):
        """Gets SuggestionListTimeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.SuggestionListTimeout

    @keyword
    def set_white_highlight_timeout(self, value):
        """Sets HighlightTimeout for White Teststack

        ``value`` is integer or timeout in milli seconds. Default is 1000.

        """

        CoreAppXmlConfiguration.Instance.HighlightTimeout = int(value)
        logger.info("White HighlightTimeout set to" + str(CoreAppXmlConfiguration.Instance.HighlightTimeout))
        return CoreAppXmlConfiguration.Instance.HighlightTimeout
    @keyword
    def get_white_highlight_timeout(self):
        """Gets HighlightTimeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.HighlightTimeout

    @keyword
    def set_white_default_date_format(self, value):
        """Sets DefaultDateFormat for White Teststack

        ``value`` is string or date format. Format choices are following:
        DayMonthYear, DayYearMonth, MonthDayYear, MonthYearDay, YearMonthDay, YearDayMonth

        Default is based on C# System.Globalization module CultureDefault value.

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


    @keyword
    def set_white_drag_step_count(self, value):
        """Sets DragStepCount for White Teststack

        ``value`` is integer. DragStepCount defines how many steps White Teststack uses to move dragged object to the destination.
        With default value 1 the dragged object is moved instantly in a single step from start to destination.

        """

        CoreAppXmlConfiguration.Instance.DragStepCount = int(value)
        logger.info("White DragStepCount set to" + str(CoreAppXmlConfiguration.Instance.DragStepCount))
        return CoreAppXmlConfiguration.Instance.DragStepCount
    @keyword
    def get_white_drag_step_count(self):
        """Gets DragStepCount for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.DragStepCount

    @keyword
    def set_white_in_proc(self, value):
        """Sets InProc for White Teststack.

        ``value`` is boolean. Description: TODO. Default is false.

        """

        CoreAppXmlConfiguration.Instance.InProc = bool(value)
        logger.info("White InProc Timeout set to" + str(CoreAppXmlConfiguration.Instance.InProc))
        return CoreAppXmlConfiguration.Instance.InProc
    @keyword
    def get_white_in_proc(self):
        """Gets InProc timeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.InProc

    @keyword
    def set_white_combobox_items_populated_without_dropdown_open(self, value):
        """Sets ComboBoxItemsPopulatedWithoutDropDownOpen for White Teststack.

        ``value`` is boolean. Description: TODO. Default is true.

        """

        CoreAppXmlConfiguration.Instance.ComboBoxItemsPopulatedWithoutDropDownOpen = bool(value)
        logger.info("White ComboBoxItemsPopulatedWithoutDropDownOpen Timeout set to" + str(CoreAppXmlConfiguration.Instance.ComboBoxItemsPopulatedWithoutDropDownOpen))
        return CoreAppXmlConfiguration.Instance.ComboBoxItemsPopulatedWithoutDropDownOpen
    @keyword
    def get_white_combobox_items_populated_without_dropdown_open(self):
        """Gets ComboBoxItemsPopulatedWithoutDropDownOpen timeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.ComboBoxItemsPopulatedWithoutDropDownOpen

    @keyword
    def set_white_raw_element_based_search(self, value):
        """Sets RawElementBasedSearch for White Teststack.

        ``value`` is boolean. Description: TODO. Default is false.

        """

        CoreAppXmlConfiguration.Instance.RawElementBasedSearch = bool(value)
        logger.info("White RawElementBasedSearch Timeout set to" + str(CoreAppXmlConfiguration.Instance.RawElementBasedSearch))
        return CoreAppXmlConfiguration.Instance.RawElementBasedSearch
    @keyword
    def get_white_raw_element_based_search(self):
        """Gets RawElementBasedSearch timeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.RawElementBasedSearch

    @keyword
    def set_white_max_element_search_depth(self, value):
        """Sets MaxElementSearchDepth for White Teststack

        ``value`` is integer. MaxElementSearchDepth defines how deep White Stack reaches the element search.
        In a deep application limiting the search improves the search performance. Default value is 10.

        """

        CoreAppXmlConfiguration.Instance.MaxElementSearchDepth = int(value)
        logger.info("White MaxElementSearchDepth set to" + str(CoreAppXmlConfiguration.Instance.MaxElementSearchDepth))
        return CoreAppXmlConfiguration.Instance.MaxElementSearchDepth
    @keyword
    def get_white_max_element_search_depth(self):
        """Gets MaxElementSearchDepth for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.MaxElementSearchDepth

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


    @keyword
    def set_white_move_mouse_to_get_status_of_hourglass(self, value):
        """Sets MoveMouseToGetStatusOfHourGlass for White Teststack.

        ``value`` is boolean. Description: TODO. Default is true.

        """

        CoreAppXmlConfiguration.Instance.MoveMouseToGetStatusOfHourGlass = bool(value)
        logger.info("White MoveMouseToGetStatusOfHourGlass Timeout set to" + str(CoreAppXmlConfiguration.Instance.MoveMouseToGetStatusOfHourGlass))
        return CoreAppXmlConfiguration.Instance.MoveMouseToGetStatusOfHourGlass
    @keyword
    def get_white_move_mouse_to_get_status_of_hourglass(self):
        """Gets MoveMouseToGetStatusOfHourGlass timeout for White Teststack

        """
        return CoreAppXmlConfiguration.Instance.MoveMouseToGetStatusOfHourGlass

    #TODO: Whit stack configuration WorkSessionLocation not implemented
    #TODO: Whit stack configuration KeepOpenOnDispose not implemented
