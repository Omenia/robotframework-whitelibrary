from TestStack.White.InputDevices import Mouse
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from System.Windows import Point
from robot.api import logger

class MouseKeywords(LibraryComponent):

    @keyword
    def set_mouse_location(self, x, y):
        """ Sets mouse position to (x, y) Position is relative to application window top left.

        """
        window_location = self.state.window.Bounds.TopLeft
        x_target = int(x)+ window_location.X
        y_target = int(y)+ window_location.Y
        point = Point(x_target, y_target)
        Mouse.Instance.Location = point

        if int(x_target) != int(Mouse.Instance.Location.X):
            logger.warn("Mouse X position tried to be set outside of the screen. Wanted: " + str(int(x_target)) + " result:" + str(Mouse.Instance.Location.X), True)
        if int(y_target) != int(Mouse.Instance.Location.Y):
            logger.warn("Mouse Y position tried to be set outside of the screen. Wanted: " + str(y_target) + " result:" + str(Mouse.Instance.Location.Y), True)

    @keyword
    def move_mouse(self, x, y):
        """ Add (x,y) to current mouse location.

        """
        current_location = Mouse.Instance.Location
        point = Point(int(x) + current_location.X, int(y) + current_location.Y)
        Mouse.Instance.Location = point

    @keyword
    def get_mouse_location(self):
        """ Gets mouse position. Position is relative to application window.
        If mouse is outside the application window the return values is either negative or bigger than window dimensions.

        """
        window_location = self.state.window.Bounds.TopLeft
        point = Mouse.Instance.Location
        return point.X - window_location.X, point.Y - window_location.Y

    @keyword
    def mouse_left_button_down(self, x=None, y=None):
        """ Presses left mouse position down. Position is relative to screen.
        If no coordinates are given it uses current mouse position.

        """
        self.check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.LeftDown()
        else:
            self.set_mouse_point(x, y, self.state.window.Bounds.TopLeft)
            Mouse.Instance.LeftDown()

    @keyword
    def mouse_left_button_up(self, x=None, y=None):
        """ Releases left mouse position up. Position is relative to screen.
        If no coordinates are given it uses current mouse position.

        """
        self.check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.LeftUp()
        else:
            self.set_mouse_point(x, y, self.state.window.Bounds.TopLeft)
            Mouse.Instance.LeftUp()

    @keyword
    def mouse_right_click(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.
        If no coordinates are given it uses current mouse position.

        """
        self.check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.RightClick()
        else:
            self.set_mouse_point(x, y, self.state.window.Bounds.TopLeft)
            Mouse.Instance.RightClick()

    @keyword
    def mouse_left_click(self, x=None, y=None):
        """ Left clicks mouse position. Position is relative to screen.
        If no coordinates are given it uses current mouse position.

        """

        self.check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.Click(Mouse.Instance.Location)
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.Click(point)

    @keyword
    def mouse_right_double_click(self, x=None, y=None):
        """ Right double clicks mouse position. Position is relative to screen.
        If no coordinates are given it uses current mouse position.

        """
        self.check_valid_x_y(x, y)
        if (x is not None) and (y is not None):
            self.set_mouse_point(x, y, self.state.window.Bounds.TopLeft)
        Mouse.Instance.RightClick()
        Mouse.Instance.RightClick()


    @keyword
    def mouse_left_double_click(self, x=None, y=None):
        """ Left double clicks mouse position. Position is relative to screen.
        If no coordinates are given it uses current mouse position.

        """

        self.check_valid_x_y(x, y)
        if (x is None) and (y is None):
            Mouse.Instance.DoubleClick(Mouse.Instance.Location)
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.DoubleClick(point)

    @keyword
    def drag_and_drop(self, locator1, locator2):
        """ Drags item under locator1 to item under locator2.

        ``locator1`` is the locator of the draggable object.
        ``locator2`` is the locator of the target for the draggable object.
        """

        draggable_object = self.state._get_item_by_locator(locator1)
        target_object = self.state._get_item_by_locator(locator2)
        Mouse.Instance.DragAndDrop(draggable_object, target_object)


    def check_valid_x_y(self, x, y):
        if (x is not None and y is None) or (x is None and y is not None):
            raise Exception("MouseKeywords::check_valide_x_y: Either x or y value missing x=" + str(x) + " y=" + str(y))

    def set_mouse_point(self, x, y, window_location):
        window_location = self.state.window.Bounds.TopLeft
        point = Point(int(x) + window_location.X, int(y) + window_location.Y)
        Mouse.Instance.Location = point
