from TestStack.White.UIItems.TreeItems import Tree
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class TreeKeywords(LibraryComponent):
    @keyword
    def select_tree_node(self, locator, *node_path):
        """Selects a tree node.

        ``locator`` is the locator of the tree or Tree item object.
        Locator syntax is explained in `Item locators`.

        ``node_path`` is the path the to node to select.

        Example tree (tree locator is tree_id):
        | root
        | |
        | |---parent_node
        | |   |
        | |   |---child_node
        | |   |
        | |   |---sibling_node
        | |
        | |---other parent

        Example usage to select ``sibling node``:
        | Select Tree Node | tree_id | root | parent_node | sibling_node |
        """
        tree = self.state._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).Select()

    @keyword
    def expand_tree_node(self, locator, *node_path):
        """Expands a tree node.

        ``locator`` is the locator of the tree or Tree item object.
        Locator syntax is explained in `Item locators`.

        ``node_path`` is the path the to node to expand.

        See examples of the node path in `Select Tree Node` documentation.
        """
        tree = self.state._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).Expand()

    @keyword
    def double_click_tree_node(self, locator, *node_path):
        """Double-clicks a tree node.

        ``locator`` is the locator of the tree or Tree item object.
        Locator syntax is explained in `Item locators`.

        ``node_path`` is the path the to node to double-click.

        See examples of the node path in `Select Tree Node` documentation.
        """
        tree = self.state._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).DoubleClick()

    @keyword
    def right_click_tree_node(self, locator, *node_path):
        """Right-clicks a tree node.

        ``locator`` is the locator of the tree or Tree item object.
        Locator syntax is explained in `Item locators`.

        ``node_path`` is the path the to node to right-click.

        See examples of the node path in `Select Tree Node` documentation.
        """
        tree = self.state._get_typed_item_by_locator(Tree, locator)
        tree.Nodes.GetItem(node_path).RightClick()
