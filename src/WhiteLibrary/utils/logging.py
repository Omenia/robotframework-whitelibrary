from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from Castle.Core.Logging import LoggerLevel    # noqa: E402
from System import Console     # noqa: E402
from System.IO import StringWriter    # noqa: E402
from TestStack.White.Configuration import CoreAppXmlConfiguration, WhiteDefaultLoggerFactory    # noqa: E402


LOGGER_LEVELS = {
    "ERROR": LoggerLevel.Error,
    "WARN": LoggerLevel.Warn,
    "INFO": LoggerLevel.Info,
    "DEBUG": LoggerLevel.Debug,
    "TRACE": LoggerLevel.Debug
}


def parse_log(log):
    message = ""
    for line in log.splitlines():
        if line.startswith(("[Fatal", "[Error", "[Warn", "[Debug", "[Info")):
            if message != "":
                yield message
            message = line
        else:
            message = "\n".join((message, line))
    if message != "":
        yield message


def update_white_log_level():
    robot_log_lvl = BuiltIn().get_variable_value("${LOG_LEVEL}")
    white_log_lvl = LOGGER_LEVELS[robot_log_lvl]
    CoreAppXmlConfiguration.Instance.LoggerFactory = WhiteDefaultLoggerFactory(white_log_lvl)


class LogWriter(object):
    def __init__(self):
        # Redirect White's output to a StringWriter
        self.log_writer = StringWriter()
        Console.SetOut(self.log_writer)

    def log_white_output(self):
        messages = self.log_writer.ToString()
        for message in parse_log(messages):
            if message.startswith("[Error") or message.startswith("[Fatal"):
                logger.error(message)
            elif message.startswith("[Debug"):
                logger.debug(message)
            elif message.startswith("[Warn"):
                logger.warn(message)
            else:
                logger.info(message)

    def reset_white_output(self):
        # Empty the StringBuilder containing White's output
        string_builder = self.log_writer.GetStringBuilder()
        string_builder.Remove(0, string_builder.Length)
