from TestStack.White.UIItems import ListView
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class ListViewKeywords(LibraryComponent):
    @keyword
    def right_click_listview_cell(self, locator, column_name, row_index):
        """Right clicks a listview cell using its column name and row index.

        ``locator`` is the locator of the listview.

        ``column_name`` is the name of the column.

        ``row_index`` is the index of the row.

        Example:
        | Right Click Listview Cell | id:userList | Name | 0 |
        """
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        cell = listview.Cell(column_name, int(row_index))
        cell.RightClick()

    @keyword
    def select_listview_row_by_index(self, locator, row_index):
        """Selects a row from a listview.

        ``locator`` is the locator of the listview.

        ``row_index`` is the index to select.
        """
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        listview.Select(int(row_index))

    @keyword
    def get_listview_row_text(self, locator, column_name, cell_text):
        """Returns text of a listview row as a list.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        return listview.Rows.Get(column_name, cell_text).Text

    @keyword
    def get_listview_row_text_by_index(self, locator, row_index):
        """Returns text of a listview row as a list.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        return listview.Rows.Get(int(row_index)).Text

    @keyword
    def get_listview_cell_text(self, locator, column_name, row_index):
        """Returns text of a listview cell.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        return listview.Cell(column_name, row_index).Text

    @keyword
    def get_listview_cell_text_by_index(self, locator, row_index, column_index):
        """Returns text of a listview cell.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        return listview.Cell(row_index, column_index).Text

    @keyword
    def listview_row_should_contain(self, locator, column_name, cell_text, expected):
        """Verifies that text is present in listview row.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        row = listview.Rows.Get(column_name, cell_text)
        for cell in row.Cells:
            if expected in cell.Text:
                return
        raise AssertionError("Row defined by cell '{}'='{}' did not contain expected value '{}'"
                             .format(column_name, cell_text, expected))

    @keyword
    def listview_row_should_not_contain(self, locator, column_name, cell_text, expected):
        """Verifies that text is present in listview row.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        row = listview.Rows.Get(column_name, cell_text)
        for cell in row.Cells:
            if expected in cell.Text:
                raise AssertionError("Row defined by cell '{}'='{}' contained value '{}' but it should not"
                                     .format(column_name, cell_text, expected))

    @keyword
    def listview_row_in_index_should_contain(self, locator, row_index, expected):
        """Verifies that text is present in listview row.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        row = listview.Rows.Get(int(row_index))
        for cell in row.Cells:
            if expected in cell.Text:
                return
        raise AssertionError("Row defined by cell '{}'='{}' did not contain expected value '{}'"
                             .format(column_name, cell_text, expected))

    @keyword
    def listview_row_in_index_should_not_contain(self, locator, row_index, expected):
        """Verifies that text is present in listview row.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        row = listview.Rows.Get(int(row_index))
        for cell in row.Cells:
            if expected in cell.Text:
                raise AssertionError("Row defined by cell '{}'='{}' did not contain expected value '{}'"
                                     .format(column_name, cell_text, expected))

    @keyword
    def listview_cell_text_should_be(self, column_name, row_index):
        """Verifies text in listview cell.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)

    @keyword
    def listview_cell_text_in_index_should_be(self, row_index, column_index):
        """Verifies text in listview cell.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)

    @keyword
    def listview_cell_should_contain(self, column_name, row_index):
        """Verifies that text is present in listview cell.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)

    @keyword
    def listview_cell_should_not_contain(self, column_name, row_index):
        """Verifies that text is present in listview cell.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)

    @keyword
    def listview_cell_in_index_should_contain(self, row_index, column_index):
        """Verifies that text is present in listview cell.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)

    @keyword
    def listview_cell_in_index_should_not_contain(self, row_index, column_index):
        """Verifies that text is present in listview cell.

        ``locator`` is the locator of the listview."""
        listview = self.state._get_typed_item_by_locator(ListView, locator)
