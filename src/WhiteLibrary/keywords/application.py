from robot.api import logger  # noqa: F401 #pylint: disable=unused-import
from System.Diagnostics import ProcessStartInfo
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.utils.wait import Wait
from TestStack.White import Application, WhiteException


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

    @staticmethod
    def _attach_application(sut_identifier, timeout=0):
        exception_message = "Unable to locate application with identifier: {}".format(sut_identifier)
        if timeout == 0:
            try:
                return Application.Attach(sut_identifier)
            except WhiteException:
                raise AssertionError(exception_message)

        # using hack due to 2.7 doesnt support nonlocal keyword
        # and inner function cant modify primitive datatypes.
        # aand im trying to avoid calling Application.Attach()
        # multiple times as it allocates memory on python .net
        # side.

        hack = {"sut": None}

        def search_application():
            try:
                hack["sut"] = Application.Attach(sut_identifier)  # noqa: F841
                return True
            except WhiteException:
                return False

        Wait.until_true(search_application, timeout, exception_message)

        return hack["sut"]

    @keyword
    def attach_application_by_name(self, sut_name, timeout=0):
        """Attaches a running application by name.

        ``sut_name`` is the name of the process.
        ``timeout`` is the maximum time to wait as a Robot time string. (Optional)


        Example:
        | Attach Application By Name | UIAutomationTest |
        """
        self.state.app = self._attach_application(sut_name, timeout)

    @keyword
    def attach_application_by_id(self, sut_id, timeout=0):
        """Attaches a running application by process id.

        ``sut_id`` is the application process id.
        ``timeout`` is the maximum time to wait as a Robot time string. (Optional)

        Example:
        | Attach Application By Id | 12188 |
        """
        self.state.app = self._attach_application(int(sut_id), timeout)

    @keyword
    def close_application(self):
        """Closes the attached application."""
        self.state.app.Close()
        self.state.app = None
        self.state.window = None
