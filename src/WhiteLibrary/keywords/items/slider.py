from TestStack.White.UIItems import Slider
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class SliderKeywords(LibraryComponent):
    @keyword
    def set_slider_value(self, locator, value):
        """
        Sets a slider to the specified value.

        ``locator`` is the locator of the slider.
        
        ``value`` is the value to set.
        """
        slider = self.state._get_typed_item_by_locator(Slider, locator)
        slider.Value = float(value)

    @keyword
    def verify_slider_value(self, locator, expected):
        """
        Verifies a slider value.

        ``locator`` is the locator of the slider.

        ``expected`` is the expected value of the slider.
        """
        slider = self.state._get_typed_item_by_locator(Slider, locator)
        self.state._verify_value(float(expected), slider.Value)
