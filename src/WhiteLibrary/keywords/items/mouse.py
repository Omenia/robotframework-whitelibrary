from robot.api import logger
from TestStack.White.InputDevices import Mouse
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from System.Windows import Point


class MouseKeywords(LibraryComponent):
    @keyword
    def set_mouse_location(self, x, y):
        """Sets mouse position to (``x``, ``y``).

        Position is relative to application window top left.
        """
        window_location = self.state.window.Bounds.TopLeft
        x_target = int(x) + window_location.X
        y_target = int(y) + window_location.Y
        point = Point(x_target, y_target)
        Mouse.Instance.Location = point

        if int(x_target) != int(Mouse.Instance.Location.X):
            logger.warn(
                "Mouse X position tried to be set outside of the screen. Wanted: {} result: {}".format(
                    x_target, Mouse.Instance.Location.X
                ),
                True,
            )
        if int(y_target) != int(Mouse.Instance.Location.Y):
            logger.warn(
                "Mouse Y position tried to be set outside of the screen. Wanted: {} result: {}".format(
                    y_target, Mouse.Instance.Location.Y
                ),
                True,
            )

    @staticmethod
    @keyword
    def move_mouse(x, y):
        """Add (``x``, ``y``) to current mouse location."""
        current_location = Mouse.Instance.Location
        point = Point(int(x) + current_location.X, int(y) + current_location.Y)
        Mouse.Instance.Location = point

    @keyword
    def get_mouse_location(self):
        """Returns mouse position as tuple (x, y).

        Position is relative to application window top left.
        If mouse is outside the application window the return values is either negative or bigger than window dimensions.

        Example:
        | ${x} | ${y} | Get Mouse Location |
        """
        window_location = self.state.window.Bounds.TopLeft
        point = Mouse.Instance.Location
        return point.X - window_location.X, point.Y - window_location.Y

    @keyword
    def mouse_left_button_down(self, x=None, y=None):
        """Presses left mouse button down at given position.

        Position (``x``, ``y``) is relative to application window top left.
        If no coordinates are given it uses current mouse position.
        """
        self._check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.LeftDown()
        else:
            self._set_mouse_point(x, y)
            Mouse.Instance.LeftDown()

    @keyword
    def mouse_left_button_up(self, x=None, y=None):
        """Releases left mouse button up at given position.

        Position (``x``, ``y``) is relative to application window top left.
        If no coordinates are given it uses current mouse position.
        """
        self._check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.LeftUp()
        else:
            self._set_mouse_point(x, y)
            Mouse.Instance.LeftUp()

    @keyword
    def mouse_right_click(self, x=None, y=None):
        """Right clicks mouse at given position.

        Position (``x``, ``y``) is relative to application window top left.
        If no coordinates are given it uses current mouse position.
        """
        self._check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.RightClick()
        else:
            self._set_mouse_point(x, y)
            Mouse.Instance.RightClick()

    @keyword
    def mouse_click(self, x=None, y=None):
        """Clicks mouse at given position.

        Position (``x``, ``y``) is relative to application window top left.
        If no coordinates are given it uses current mouse position.
        """
        self._check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.Click(Mouse.Instance.Location)
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.Click(point)

    @keyword
    def mouse_right_double_click(self, x=None, y=None):
        """Right double clicks mouse at given position.

        Position (``x``, ``y``) is relative to application window top left.
        If no coordinates are given it uses current mouse position.
        """
        self._check_valid_x_y(x, y)
        if (x is not None) and (y is not None):
            self._set_mouse_point(x, y)
        Mouse.Instance.RightClick()
        Mouse.Instance.RightClick()

    @keyword
    def mouse_double_click(self, x=None, y=None):
        """Double clicks mouse at given position.

        Position (``x``, ``y``) is relative to application window top left.
        If no coordinates are given it uses current mouse position.
        """
        self._check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.DoubleClick(Mouse.Instance.Location)
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.DoubleClick(point)

    @keyword
    def drag_and_drop(self, locator1, locator2):
        """Drags item with locator ``locator1`` to item with locator ``locator2``.

        ``locator1`` is the locator of the draggable object or draggable item.

        ``locator2`` is the locator of the target for the draggable object or target item itself.

        Locator syntax is explained in `Item locators`.
        """
        draggable_object = self.state._get_item_by_locator(locator1)
        target_object = self.state._get_item_by_locator(locator2)
        Mouse.Instance.DragAndDrop(draggable_object, target_object)

    @staticmethod
    def _check_valid_x_y(x, y):
        if (x is not None and y is None) or (x is None and y is not None):
            raise ValueError("MouseKeywords::check_valid_x_y: Either x or y value missing x=" + str(x) + " y=" + str(y))

    def _set_mouse_point(self, x, y):
        window_location = self.state.window.Bounds.TopLeft
        point = Point(int(x) + window_location.X, int(y) + window_location.Y)
        Mouse.Instance.Location = point
