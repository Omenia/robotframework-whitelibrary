from System.Windows import Point
from TestStack.White.UIA import RectX
from TestStack.White.InputDevices import Mouse


class Clicks:
    # Low level function to handle offset click.
    @staticmethod
    def click(item, x_offset, y_offset):
        if x_offset == 0 and y_offset == 0:
            item.Click()
        else:
            offset_position = Clicks._get_offset_point(item, x_offset, y_offset)
            Mouse.Instance.Click(offset_position)

    # Low level helper function to handle offset right click.
    @staticmethod
    def right_click(item, x_offset, y_offset):
        if x_offset == 0 and y_offset == 0:
            item.RightClick()
        else:
            offset_position = Clicks._get_offset_point(item, x_offset, y_offset)
            Mouse.Instance.Location = offset_position
            Mouse.Instance.RightClick()

    # Low level helper function to handle offset double click.
    @staticmethod
    def double_click(item, x_offset, y_offset):
        if x_offset == 0 and y_offset == 0:
            item.DoubleClick()
        else:
            offset_position = Clicks._get_offset_point(item, x_offset, y_offset)
            Mouse.Instance.DoubleClick(offset_position)

    # Helper function to translate item center to offset point
    @staticmethod
    def _get_offset_point(item, x_offset, y_offset):
        item_bounds = item.Bounds
        item_center = RectX.Center(item_bounds)
        offset_point = Point(int(item_center.X) + int(x_offset), int(item_center.Y) + int(y_offset))
        if not item_bounds.Contains(offset_point):
            raise AssertionError("click location out of bounds")
        return offset_point
