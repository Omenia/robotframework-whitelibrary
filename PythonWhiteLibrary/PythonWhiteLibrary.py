import clr
clr.AddReferenceToFileAndPath('../WhiteLibrary/bin/WhiteLibrary.dll') #include full path to Dll if required
from WhiteLibrary import Keywords

WHITE_LIB = Keywords()

class PythonWhiteLibrary(object):
    def launch_application(self, sut):
	    WHITE_LIB.launch_application(sut)

    def attach_window(self, window):
        WHITE_LIB.attach_window(window)

    def close_application(self):
        WHITE_LIB.close_application()

    def set_logging_level(self, level):
        WHITE_LIB.set_log_level(level)

    def input_text(self, locator, text):
	    WHITE_LIB.input_text(locator, text)

    def verify_text(self, locator, actual):
        found = WHITE_LIB.verify_text(locator)
        if found != actual:
            raise AssertionError("Expected: %s. Found: %s" % (actual, found))