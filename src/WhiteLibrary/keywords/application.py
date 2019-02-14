from robot.api import logger  # noqa: F401 #pylint: disable=unused-import
from System.Diagnostics import ProcessStartInfo
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White import Application


class ApplicationKeywords(LibraryComponent):
    @keyword
    def launch_application(self, sut_path, args=None):
        """Launches an application.

        ``sut_path`` is the absolute path to the application to launch.

        ``args`` is a string of arguments to use when starting the application (optional).

        Examples:
        | Launch Application | C:/path/to/MyApp.exe | | # Launch without arguments |
        | Launch Application | C:/path/to/MyApp.exe | /o log.txt | # Launch with arguments |
        """
        if args is not None:
            process_start_info = ProcessStartInfo(sut_path)
            process_start_info.Arguments = args
            self.state.app = Application.Launch(process_start_info)
        else:
            self.state.app = Application.Launch(sut_path)

    @keyword
    def attach_application_by_name(self, sut_name):
        """Attaches a running application by name.

        ``sut_name`` is the name of the process.

        Example:
        | Attach Application By Name | UIAutomationTest |
        """
        self.state.app = Application.Attach(sut_name)

    @keyword
    def attach_application_by_id(self, sut_id):
        """Attaches a running application by process id.

        ``sut_id`` is the application process id.

        Example:
        | Attach Application By Id | 12188 |
        """
        self.state.app = Application.Attach(int(sut_id))

    @keyword
    def close_application(self):
        """Closes the attached application."""
        self.state.app.Close()
        self.state.app = None
        self.state.window = None
