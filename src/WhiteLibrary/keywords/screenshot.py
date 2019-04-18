import os
import robot
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.utils import get_link_path, is_truthy
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword, PY2
from System.Drawing.Imaging import ImageFormat
from TestStack.White import Desktop


class ScreenshotKeywords(LibraryComponent):
    def __init__(self, state, directory):
        super(ScreenshotKeywords, self).__init__(state)
        self.state.screenshooter = self
        self._screenshot_directory = directory

    @keyword
    def set_screenshot_directory(self, path):
        """Sets the directory where WhiteLibrary stores screenshots and returns the previously set path.

        If the given directory does not exist in the system, it will be created when the first screenshot is taken.

        ``path`` is the directory path.

        The directory can also be set when the library is imported, see `Importing` for details.
        """
        old_dir = self._screenshot_directory
        self._screenshot_directory = None if path is None else robot.utils.abspath(path)
        return old_dir

    @keyword
    def take_desktop_screenshot(self):
        """Takes a screenshot of the whole desktop and inserts screenshot link to log file.

        Returns path to the screenshot file.
        """
        filepath = self._get_screenshot_path("whitelib_screenshot_{index}.png")
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        logger.info(get_link_path(filepath, self._log_directory))
        logger.info(
            '</td></tr><tr><td colspan="3">'
            '<a href="{src}"><img src="{src}" width="800px"></a>'.format(
                src=get_link_path(filepath, self._log_directory)
            ),
            html=True,
        )
        bmp = Desktop.CaptureScreenshot()
        bmp.Save(filepath, ImageFormat.Png)
        return filepath

    @keyword
    def take_screenshots_on_failure(self, status):
        """Disables or enables automatic screenshot capturing on failure.

        ``status`` is the desired state (True/False) of automatic screenshot on failure.
        Boolean values are evaluated in the same way as the Robot Framework BuiltIn library does, see
        [http://robotframework.org/robotframework | the documentation of BuiltIn] for details.

        WhiteLibrary automatically takes a screenshot on failure unless it is disabled with this keyword.
        """
        if is_truthy(status):
            self.state.screenshots_enabled = True
        else:
            self.state.screenshots_enabled = False

    @property
    def _log_directory(self):
        try:
            logfile = BuiltIn().get_variable_value("${LOG FILE}")
            if logfile is None:
                return BuiltIn().get_variable_value("${OUTPUTDIR}")
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwdu() if PY2 else os.getcwd()  # pylint: disable=no-member

    def _get_screenshot_path(self, filename):
        if self._screenshot_directory is not None:
            directory = self._screenshot_directory
        else:
            directory = self._log_directory
        filename = filename.replace("/", os.sep)
        index = 0
        while True:
            index += 1
            formatted = filename.format(index=index)
            filepath = os.path.join(directory, formatted)
            # filename didn't contain {index} or unique path was found
            if formatted == filename or not os.path.exists(filepath):
                return filepath
