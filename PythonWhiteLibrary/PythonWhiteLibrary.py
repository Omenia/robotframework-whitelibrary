import clr
clr.AddReferenceToFileAndPath('../WhiteLibrary/bin/WhiteLibrary.dll') #include full path to Dll if required
from WhiteLibrary import Keywords

instance = Keywords()

def alkujuttu():
	instance.alkujuttu()

def input_text(locator, text):
	instance.input_text()
 
def tee_jotain():
	instance.TeeJotain()

 
