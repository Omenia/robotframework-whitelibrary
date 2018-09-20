import clr
clr.AddReference('System')
clr.AddReference('TestStack.White') #include full path to Dll if required
from TestStack.White.UIItems.WindowItems import Window
from TestStack.White.UIItems import Button, TextBox, Label
from TestStack.White import Application
from TestStack.White.UIItems.Finders import SearchCriteria


from robot.api import logger


STRATEGIES = {"id": "ByAutomationId",
              "text": "ByText"}


class WhiteLibrary(object):
    ROBOT_LIBRARY_SCOPE = "Global"
    
    def __init__(self):
        self.app = None
        self.window = None

    def launch_application(self, sut_path):
        self.app = Application.Launch(sut_path)

    def attach_window(self, window_title):
        self.window = self.app.GetWindow(window_title)
        logger.console("window {}".format(self.window))

    def close_application(self):
        '''
        Close application
        | No arguments |
        '''
        self.app.Close()
        self.app = None
        self.window = None

    def input_text_to_textbox(self, locator, text):
        '''
        Write text to textbox
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | text | inserted string | M |
        '''            
        textBox = self._get_item_by_locator(TextBox, locator)
        textBox.Text = text

    def set_slider_value(self, locator, double):
        '''
        Write slider to value double
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | double | inserted value (must be between scale) | M |
        '''
        self.WHITE_LIB.set_slider(locator, double)

    def verify_slider_value(self, locator, expected):
        '''
        Verify slider value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected double | M |
        '''
        actual = self.WHITE_LIB.verify_slider(locator)
        verify_value(expected, actual)

    def verify_progressbar_value(self, locator, expected):
        '''
        Verify progressbar value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected double | M |
        '''
        actual = self.WHITE_LIB.verify_progressbar(locator)
        verify_value(expected, actual)

    def verify_text_in_textbox(self, locator, expected):
        '''
        Verify text in textbox
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        '''
        actual = self.WHITE_LIB.verify_text_textbox(locator)
        verify_value(expected, actual)

    def verify_label(self, locator, expected):
        '''
        Verify text in label
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        '''
        label = self._get_item_by_locator(Label, locator)
        self._verify_value(expected, label.Text)

    def select_combobox_value(self, locator, value):
        '''
        Select combobox value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | value | selected value | M |
        '''
        self.WHITE_LIB.select_combobox_value(locator, value)

    def select_listbox_value(self, locator, value):
        '''
        Select listbox value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | value | selected value | M |
        '''
        self.WHITE_LIB.select_listbox_value(locator, value)

    def toggle_check_box(self, locator):
        '''
        Toggle check box
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        '''
        self.WHITE_LIB.toggle_check_box(locator)

    def select_combobox_index(self, locator, index):
        '''
        Select combobox index
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | index | combobox index | M |
        '''
        self.WHITE_LIB.select_combobox_index(locator, int(index))

    def verify_combobox_item(self, locator, expected):
        '''
        Verify combobox selected value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        '''
        actual = self.WHITE_LIB.verify_combobox_item(locator)
        verify_value(expected, actual)

    def verify_button(self, locator, expected):
        '''
        Verify text in button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        '''
        actual = self.WHITE_LIB.verify_button(locator)
        verify_value(expected, actual)

    def click_button(self, locator):
        '''
        Click button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        '''
        button = self._get_item_by_locator(Button, locator)
        button.Click()

    def _get_item_by_locator(self, item_type, locator):
        if "=" not in locator:
            locator = "id=" + locator
        search_strategy, locator_value = locator.split("=")
        search_method = STRATEGIES[search_strategy]
        method = getattr(SearchCriteria, search_method)
        search_criteria = method(locator_value)
        return self.window.Get[item_type](search_criteria)

    def verify_radio_button(self, locator, expected):
        '''
        Verify value of radio button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        '''
        actual = self.WHITE_LIB.verify_radio_button(locator)
        verify_value(expected, actual)

    def verify_check_box(self, locator, expected):
        '''
        Verify value of check box
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        '''
        actual = self.WHITE_LIB.verify_check_box(locator)
        verify_value(expected, actual)

    def select_radio_button(self, locator):
        '''
        Click button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        '''
        self.WHITE_LIB.select_radio_button(locator)

    def verify_menu(self, locator, expected):
        '''
        Verify menu item exists
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | expected | expected text in value | M |
        '''
        actual = self.WHITE_LIB.verify_menu(locator)
        verify_value(expected, actual)

    def click_menu_button(self, locator):
        '''
        Click menu button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        '''
        self.WHITE_LIB.click_menu_button(locator)

    def select_modal_window(self, locator):
        '''
        Select modal window by title
        | Arguments | Usage | (M)andatory / (O)ptional |
        | Title | Modal window title | M |
        '''
        self.WHITE_LIB.select_modal_window(locator)

    def select_tab_page(self, locator, title):
        """ Selects a tab page. """
        self.WHITE_LIB.selectTabPage(locator, title)

    def select_tree_node(self, locator, *node_path):
        """ Selects a tree node. """
        self.WHITE_LIB.selectTreeNode(locator, node_path)

    def expand_tree_node(self, locator, *node_path):
        """ Expands a tree node. """
        self.WHITE_LIB.expandTreeNode(locator, node_path)

    def double_click_tree_node(self, locator, *node_path):
        """ Double-clicks a tree node. """
        self.WHITE_LIB.doubleClickTreeNode(locator, node_path)

    def right_click_tree_node(self, locator, *node_path):
        """ Right-clicks a tree node. """
        self.WHITE_LIB.rightClickTreeNode(locator, node_path) 
        
    def _verify_value(self, expected, actual):
        if expected != actual:
            raise AssertionError("Expected value {}, but found {}".format(expected, actual))