import clr
clr.AddReferenceToFileAndPath('../WhiteLibrary/bin/WhiteLibrary.dll') #include full path to Dll if required
from WhiteLibrary import Keywords

WHITE_LIB = Keywords()

class PythonWhiteLibrary(object):
    def launch_application(self, sut):
	    WHITE_LIB.launch_application(sut)

    def close_application(self):
        WHITE_LIB.close_application()

    def input_text(self, locator, text):
	    WHITE_LIB.input_text(locator, text)

