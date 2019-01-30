from TestStack.White.InputDevices import Mouse
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class DragDropKeywords(LibraryComponent):
    @keyword
    def drag_and_drop(self, locator1, locator2):
        """ Drags item under locator1 to item under locator2.

        ``locator1`` is the locator of the draggable object (TODO: check if needs to be draggable).
        ``locator2`` is the locator of the target for the draggable object.
        """

        draggable_object = self.state._get_item_by_locator(locator1)
        target_object = self.state._get_item_by_locator(locator2)
        Mouse.Instance.DragAndDrop(draggable_object, target_object)
