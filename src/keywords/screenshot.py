import os
from librarycomponent import LibraryComponent
from robotlibcore import keyword
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.utils import get_link_path

from System.Drawing import Bitmap
from System.Drawing.Imaging import ImageFormat
from TestStack.White import Desktop


class ScreenshotKeywords(LibraryComponent):

    def __init__(self, state):
        super(ScreenshotKeywords, self).__init__(state)
        self.state.screenshotter = self

    @keyword
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

    @keyword
    def take_screenshots_on_failure(self, status):
        """ Disable or enable automatic screenshot creation on failure.
        Parameters
        ----------
        status: bool or str
            True or False, boolean or string, case insensitive. """
        if (str(status).lower() == 'false'):
            self.state.screenshots_enabled = False
        else:
            self.state.screenshots_enabled = True

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