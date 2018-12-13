from TestStack.White.UIItems.TreeItems import Tree
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class TreeKeywords(LibraryComponent):
    @keyword
    def select_tree_node(self, locator, *node_path):
        """ Selects a tree node. """
        tree = self.state._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).Select()
        
    @keyword
    def expand_tree_node(self, locator, *node_path):
        """ Expands a tree node. """
        tree = self.state._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).Expand()
        
    @keyword
    def double_click_tree_node(self, locator, *node_path):
        """ Double-clicks a tree node. """
        tree = self.state._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).DoubleClick()
        
    @keyword
    def right_click_tree_node(self, locator, *node_path):
        """ Right-clicks a tree node. """
        tree = self.state._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).RightClick()
