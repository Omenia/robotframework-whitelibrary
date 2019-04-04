from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.InputDevices import Keyboard  # noqa: F401 #pylint: disable=unused-import
from TestStack.White.WindowsAPI import KeyboardInput


SPECIAL_KEYS = ["SHIFT", "CONTROL", "ALT", "LEFT_ALT", "RIGHT_ALT", "RETURN",
                "RIGHT", "BACKSPACE", "LEFT", "ESCAPE", "TAB", "HOME", "END",
                "UP", "DOWN", "INSERT", "DELETE", "CAPS", "F1", "F2", "F3",
                "F4", "F5", "F6", "F7", "F8", "F9", "F11", "F12", "F13", "F14",
                "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23",
                "F24", "PAGEUP", "PAGEDOWN", "PRINT", "PRINTSCREEN", "SPACE",
                "NUMLOCK", "SCROLL", "LWIN", "RWIN"]


class KeyboardKeywords(LibraryComponent):
    @keyword
    def press_special_key(self, key):
        """Press a special key (Ctrl, tab, alt for example).

        ``key`` must be one of the following:
        SHIFT, CONTROL, ALT, LEFT_ALT, RIGHT_ALT, RETURN ,RIGHT, BACKSPACE,
        LEFT, ESCAPE, TAB, HOME, END, UP, DOWN, INSERT, DELETE, CAPS, F1, F2,
        F3, F4, F5, F6, F7, F8, F9, F11, F12, F13, F14,F15, F16, F17, F18, F19,
        F20, F21, F22, F23,F24, PAGEUP, PAGEDOWN, PRINT, PRINTSCREEN, SPACE,
        NUMLOCK, SCROLL, LWIN, RWIN
        """
        if key not in SPECIAL_KEYS:
            raise AttributeError("Allowed special keys are " + str(SPECIAL_KEYS))
        attribute = getattr(KeyboardInput.SpecialKeys, key)
        self.state.window.Keyboard.PressSpecialKey(attribute)

    @keyword
    def hold_special_key(self, key):
        """Hold down a special key.

        ``key`` must be one of the accepted special keys, see documentation of
        `Press Special Key`
        """
        if key not in SPECIAL_KEYS:
            raise AttributeError("Allowed special keys are " + str(SPECIAL_KEYS))
        attribute = getattr(KeyboardInput.SpecialKeys, key)
        self.state.window.Keyboard.HoldKey(attribute)

    @keyword
    def leave_special_key(self, key):
        """Leave a special key that was previously held down.

        ``key`` must be one of the accepted special keys, see documentation of
        `Press Special Key`
        """
        if key not in SPECIAL_KEYS:
            raise AttributeError("Allowed special keys are " + str(SPECIAL_KEYS))
        attribute = getattr(KeyboardInput.SpecialKeys, key)
        self.state.window.Keyboard.LeaveKey(attribute)

    @keyword
    def press_keys(self, keys):
        """Press a key or keys.

        ``keys`` is the key or keys to press.

        Example:
        | Press Keys | a |
        | Press Keys | Text with special characters! |
        """
        self.state.window.Keyboard.Enter(keys)
