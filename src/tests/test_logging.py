import unittest
from WhiteLibrary.utils.logging import parse_log


class TestLogParsing(unittest.TestCase):
    def test_empty_log(self):
        log = ""
        parsed = list(parse_log(log))
        self.assertEqual(parsed, [])

    def test_one_liners(self):
        log = """[Info - 9.33.03] 'TestStack.White.Application' Closing Application
[Info - 9.33.03] 'TestStack.White.Application' Closing Application
[Info - 9.33.03] 'TestStack.White.Application' Closing Application
"""
        parsed = list(parse_log(log))
        self.assertEqual(parsed, ["[Info - 9.33.03] 'TestStack.White.Application' Closing Application",
                                  "[Info - 9.33.03] 'TestStack.White.Application' Closing Application",
                                  "[Info - 9.33.03] 'TestStack.White.Application' Closing Application"])

    def test_multi_line_messages(self):
        log = """[Warn - 9.32.56] Window with title: Apple [a - 1.2.3]
UI actions on window needing mouse would not work in area not falling under the desktop
[Warn - 9.32.56] Window with title: Banana [b - 11.22.33]
UI actions on window needing mouse would not work in area not falling under the desktop
"""
        parsed = list(parse_log(log))
        self.assertEqual(parsed, ["""[Warn - 9.32.56] Window with title: Apple [a - 1.2.3]
UI actions on window needing mouse would not work in area not falling under the desktop""",
                                  """[Warn - 9.32.56] Window with title: Banana [b - 11.22.33]
UI actions on window needing mouse would not work in area not falling under the desktop"""])
