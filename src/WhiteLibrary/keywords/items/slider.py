from TestStack.White.UIItems import Slider
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class SliderKeywords(LibraryComponent):
    @keyword
    def set_slider_value(self, locator, value):
        """
        Write slider to value double
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | value | inserted value (must be between scale) | M |
        """
        slider = self.state._get_typed_item_by_locator(Slider, locator)
        slider.Value = float(value)

    @keyword
    def verify_slider_value(self, locator, expected):
        """
        Verify slider value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected double | M |
        """
        slider = self.state._get_typed_item_by_locator(Slider, locator)
        self.state._verify_value(float(expected), slider.Value)
