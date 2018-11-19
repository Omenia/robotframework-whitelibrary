import os
import clr
clr.AddReference('System')
clr.AddReference('TestStack.White') #include full path to Dll if required
from System.Drawing import Bitmap
from System.Drawing.Imaging import ImageFormat
from TestStack.White import Application, Desktop
from TestStack.White.UIItems.WindowItems import Window
from TestStack.White.UIItems import Button, TextBox, Label, RadioButton, Slider, CheckBox, ProgressBar, UIItem
from TestStack.White.UIItems.TabItems import Tab
from TestStack.White.UIItems.TreeItems import Tree
from TestStack.White.UIItems.ListBoxItems import ComboBox, ListBox
from TestStack.White.UIItems.MenuItems import Menu
from TestStack.White.UIItems.Finders import SearchCriteria


from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.utils import get_link_path


STRATEGIES = {"id": "ByAutomationId",
              "text": "ByText",
              "index": "Indexed"}


class WhiteLibrary(object):
    ROBOT_LIBRARY_SCOPE = "Global"
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.app = None
        self.window = None
        self.ROBOT_LIBRARY_LISTENER = self
        self.screenshot_type = 'desktop'
        self.screenshots_enabled = True

    def launch_application(self, sut_path):
        self.app = Application.Launch(sut_path)

    def attach_application_by_name(self, sut_name):
        """ Attaches to a running application by name.
        Parameters
        ---------- 
        sut_name: string
            Application process name
        """
        self.app = Application.Attach(sut_name)

    def attach_application_by_id(self, sut_id):
        """ Attaches to a running application by id.
        Parameters
        ---------- 
        sut_id: int
            Application process id
        """
        self.app = Application.Attach(sut_id)

    def attach_window(self, window_title):
        self.window = self.app.GetWindow(window_title)
        logger.console("window {}".format(self.window))

    def close_application(self):
        """
        Close application
        | No arguments |
        """
        self.app.Close()
        self.app = None
        self.window = None

    def input_text_to_textbox(self, locator, text):
        """
        Write text to textbox
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | text | inserted string | M |
        """
        textBox = self._get_typed_item_by_locator(TextBox, locator)
        textBox.Text = text

    def click_item(self, locator):
        """
        Click an item
        Parameters
        ----------
        locator - element id, text or index prefixed with <locator_type>=
        """
        item = self._get_item_by_locator(locator)
        item.Click()

    def right_click_item(self, locator):
        """
        Right click an item
        Parameters
        ----------
        locator - element id, text or index prefixed with <locator_type>=
        """
        item = self._get_item_by_locator(locator)
        item.RightClick()

    def double_click_item(self, locator):
        """
        Double click an item
        Parameters
        ----------
        locator - element id, text or index prefixed with <locator_type>=
        """
        item = self._get_item_by_locator(locator)
        item.DoubleClick()

    def set_slider_value(self, locator, value):
        """
        Write slider to value double
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | value | inserted value (must be between scale) | M |
        """
        slider = self._get_typed_item_by_locator(Slider, locator)
        slider.Value = float(value)

    def verify_slider_value(self, locator, expected):
        """
        Verify slider value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected double | M |
        """
        slider = self._get_typed_item_by_locator(Slider, locator)
        self._verify_value(float(expected), slider.Value)

    def verify_progressbar_value(self, locator, expected):
        """
        Verify progressbar value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | expected | expected value | M |
        """
        progressbar = self._get_typed_item_by_locator(ProgressBar, locator)
        self._verify_value(float(expected), progressbar.Value)

    def verify_text_in_textbox(self, locator, expected):
        """
        Verify text in textbox
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        """
        textbox = self._get_typed_item_by_locator(TextBox, locator)
        self._verify_value(expected, textbox.Text)

    def verify_label(self, locator, expected):
        """
        Verify text in label
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        """
        label = self._get_typed_item_by_locator(Label, locator)
        self._verify_value(expected, label.Text)

    def select_combobox_value(self, locator, value):
        """
        Select combobox value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | value | selected value | M |
        """
        combobox = self._get_typed_item_by_locator(ComboBox, locator)
        combobox.Select(value)

    def select_listbox_value(self, locator, value):
        """
        Select listbox value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | value | selected value | M |
        """
        listbox = self._get_typed_item_by_locator(ListBox, locator)
        listbox.Select(value)

    def listbox_selection_should_be(self, locator, value):
        """
        Check that the value on the listbox is selected
        Parameters
        ----------
        locator - element id, text or index prefixed with <locator_type>=
        value - value that should be selected
        Raises
        ------
        AssertionError - if the selection was not as expected
        """
        listbox = self._get_typed_item_by_locator(ListBox, locator)
        if listbox.SelectedItemText != value:
            raise AssertionError("Expected listbox selection to be " +
                                 value + ", was " + listbox.SelectedItemText)

    def toggle_check_box(self, locator):
        """
        Toggle check box
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        """
        checkbox = self._get_typed_item_by_locator(CheckBox, locator)
        checkbox.Toggle()

    def select_combobox_index(self, locator, index):
        """
        Select combobox index
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | index | combobox index | M |
        """
        combobox = self._get_typed_item_by_locator(ComboBox, locator)
        combobox.Select(int(index))

    def verify_combobox_item(self, locator, expected):
        """
        *DEPRECATED* Please use Verify Combobox Selection instead
        Verify combobox selected value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        """
        self.verify_combobox_selection(locator, expected)

    def verify_combobox_selection(self, locator, expected):
        """
        Verify combobox selected value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        """
        combobox = self._get_typed_item_by_locator(ComboBox, locator)
        self._verify_value(expected, combobox.EditableText)

    def verify_button(self, locator, expected):
        """
        Verify text in button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        """
        button = self._get_typed_item_by_locator(Button, locator)
        self._verify_value(expected, button.Text)

    def click_button(self, locator):
        """
        Click button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        """
        button = self._get_typed_item_by_locator(Button, locator)
        button.Click()

    def _get_typed_item_by_locator(self, item_type, locator):
        search_criteria = self._get_search_criteria(locator)
        return self.window.Get[item_type](search_criteria)

    def _get_item_by_locator(self, locator):
        search_criteria = self._get_search_criteria(locator)
        return self.window.Get(search_criteria)

    def _get_search_criteria(self, locator):
        if "=" not in locator:
            locator = "id=" + locator
        search_strategy, locator_value = locator.split("=")
        if search_strategy == "index":
            locator_value = int(locator_value)
        search_method = STRATEGIES[search_strategy]
        method = getattr(SearchCriteria, search_method)
        return method(locator_value)

    def verify_radio_button(self, locator, expected):
        """
        Verify value of radio button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        """
        radiobutton = self._get_typed_item_by_locator(RadioButton, locator)
        self._verify_value(bool(expected), radiobutton.IsSelected)

    def verify_check_box(self, locator, expected):
        """
        Verify value of check box
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        """
        checkbox = self._get_typed_item_by_locator(CheckBox, locator)
        self._verify_value(bool(expected), checkbox.IsSelected)

    def select_radio_button(self, locator):
        """
        Click button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        """
        radiobutton = self._get_typed_item_by_locator(RadioButton, locator)
        radiobutton.Select()

    def verify_menu(self, locator, expected):
        """
        Verify menu item exists
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | expected | expected text in value | M |
        """
        menu = self._get_typed_item_by_locator(Menu, locator)
        self._verify_value(expected, menu.Name)

    def click_menu_button(self, locator):
        """
        Click menu button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        """
        menu_button = self._get_typed_item_by_locator(Menu, locator)
        menu_button.Click()

    def select_modal_window(self, locator):
        """
        Select modal window by title
        | Arguments | Usage | (M)andatory / (O)ptional |
        | Title | Modal window title | M |
        """
        self.window = self.window.ModalWindow(locator)

    def select_tab_page(self, locator, title):
        """ Selects a tab page. """
        tab = self._get_typed_item_by_locator(Tab, locator)
        tab.SelectTabPage(title)

    def select_tree_node(self, locator, *node_path):
        """ Selects a tree node. """
        tree = self._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).Select()

    def expand_tree_node(self, locator, *node_path):
        """ Expands a tree node. """
        tree = self._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).Expand()

    def double_click_tree_node(self, locator, *node_path):
        """ Double-clicks a tree node. """
        tree = self._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).DoubleClick()

    def right_click_tree_node(self, locator, *node_path):
        """ Right-clicks a tree node. """
        tree = self._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).RightClick()

    def take_desktop_screenshot(self):
        """ Takes a screenshot of the whole desktop and inserts screenshot link to log file.
        Returns
        -------
        string
            path to the screenshot file
        """
        filepath = self._get_screenshot_path("whitelib_screenshot_{index}.png")
        logger.info(get_link_path(filepath, self._log_directory), also_console=True)
        logger.info(
            '</td></tr><tr><td colspan="3">''<a href="{src}"><img src="{src}" width="800px"></a>'.format(
                src=get_link_path(filepath, self._log_directory)), html=True)
        bmp = Desktop.CaptureScreenshot()
        bmp.Save(filepath, ImageFormat.Png)
        return filepath

    def take_screenshots_on_failure(self, status):
        """ Disable or enable automatic screenshot creation on failure.
        Parameters
        ----------
        status: bool or str
            True or False, boolean or string, case insensitive. """
        if (str(status).lower() == 'false'):
            self.screenshots_enabled = False
        else:
            self.screenshots_enabled = True

    @property
    def _log_directory(self):
        try:
            logfile = BuiltIn().get_variable_value('${LOG FILE}')
            if logfile is None:
                return BuiltIn().get_variable_value('${OUTPUTDIR}')
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwdu() if PY2 else os.getcwd()

    def _get_screenshot_path(self, filename):
        directory = self._log_directory
        filename = filename.replace('/', os.sep)
        index = 0
        while True:
            index += 1
            formatted = filename.format(index=index)
            filepath = os.path.join(directory, formatted)
            # filename didn't contain {index} or unique path was found
            if formatted == filename or not os.path.exists(filepath):
                return filepath

    def _end_keyword(self, name, attrs):
        if attrs['status'] == 'FAIL':
            if self.screenshot_type == 'desktop' and self.screenshots_enabled:
                self.take_desktop_screenshot()

    def _verify_value(self, expected, actual):
        if expected != actual:
            raise AssertionError("Expected value {}, but found {}".format(expected, actual))
