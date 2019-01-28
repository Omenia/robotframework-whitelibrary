from System.Diagnostics import ProcessStartInfo
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White import Application
from robot.api import logger

class ApplicationKeywords(LibraryComponent):
    @keyword
    def launch_application(self, sut_path, args=None):
        if args is not None:
            processStartInfo = ProcessStartInfo(sut_path)
            processStartInfo.Arguments = args
            self.state.app = Application.Launch(processStartInfo)
        else:
            self.state.app = Application.Launch(sut_path)

    @keyword
    def attach_application_by_name(self, sut_name):
        """ Attaches to a running application by name.

        ``sut_name`` is the application process name.
        """
        self.state.app = Application.Attach(sut_name)

    @keyword
    def attach_application_by_id(self, sut_id):
        """ Attaches to a running application by id.

        ``sut_id`` is the application process id.
        """
        self.state.app = Application.Attach(int(sut_id))

    @keyword
    def close_application(self):
        """
        Closes the application.
        """
        self.state.app.Close()
        self.state.app = None
        self.state.window = None
