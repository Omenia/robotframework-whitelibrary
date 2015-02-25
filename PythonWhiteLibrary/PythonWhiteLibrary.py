import clr
clr.AddReferenceToFileAndPath('../WhiteLibrary/bin/WhiteLibrary.dll') #include full path to Dll if required
from WhiteLibrary import Keywords

WHITE_LIB = Keywords()

class PythonWhiteLibrary(object):
    def launch_application(self, sut):
        '''
        Launch windows application
        | Arguments | Usage | (M)andatory / (O)ptional |
        | sut | application under testing | M |
        '''
        WHITE_LIB.launch_application(sut)

    def attach_window(self, window):
        '''
        Attach to window in application
        | Arguments | Usage | (M)andatory / (O)ptional |
        | window | window to attach | M |
        '''
        WHITE_LIB.attach_window(window)

    def close_application(self):
        '''
        Close application
        | No arguments |
        '''
        WHITE_LIB.close_application()

    def set_logging_level(self, level):
        '''
        Set log level
        | Arguments | Usage | (M)andatory / (O)ptional |
        | level | log level (info / debug / warn) | M |
        '''
        WHITE_LIB.set_log_level(level)

    def input_text_to_textbox(self, locator, text):
        '''
        Write text to textbox
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | text | inserted string | M |
        '''
        WHITE_LIB.input_text_textbox(locator, text)

    def verify_text_in_textbox(self, locator, actual):
        '''
        Verify text in textbox
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        '''
        found = WHITE_LIB.verify_text_textbox(locator)
        if found != actual:
            raise AssertionError("Expected: %s Found: %s" % (actual, found))

    def verify_label(self, locator, actual):
        '''
        Verify text in label
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        '''
        found = WHITE_LIB.verify_label(locator)
        if found != actual:
            raise AssertionError("Expected: %s Found: %s" % (actual, found))

    def select_combobox_value(self, locator, value):
        '''
        Select combobox value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | value | selected value | M |
        '''
        WHITE_LIB.select_combobox_value(locator, value)

    def select_combobox_index(self, locator, index):
        '''
        Select combobox index
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | index | combobox index | M |
        '''
        WHITE_LIB.select_combobox_index(locator, int(index))

    def verify_combobox_item(self, locator, actual):
        '''
        Verify combobox selected value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        '''
        found = WHITE_LIB.verify_combobox_item(locator)
        if found != actual:
            raise AssertionError("Expected: %s Found: %s" % (actual, found))

    def verify_button(self, locator, actual):
        '''
        Verify text in button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        '''
        found = WHITE_LIB.verify_button(locator)
        if found != actual:
            raise AssertionError("Expected: %s Found: %s" % (actual, found))

    def click_button(self, locator):
        '''
        Click button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        '''
        WHITE_LIB.click_button(locator)