from TestStack.White.UIItems import ListView
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class ListViewKeywords(LibraryComponent):
    @keyword
    def double_click_listview_cell(self, locator, column_name, row_index):
        """Double clicks a listview cell.

        ``locator`` is the locator of the listview.

        ``column_name`` is the name of the column.

        ``row_index`` is the zero-based row index.

        Example:
        | Double Click Listview Cell | id:addressList | Street | 0 | # double click cell in the column "Street" of the first row |
        """
        cell = self._get_cell(locator, column_name, row_index)
        cell.DoubleClick()

    @keyword
    def double_click_listview_cell_by_index(self, locator, row_index, column_index):
        """Double clicks a listview cell at index.

        ``locator`` is the locator of the listview.

        ``row_index`` is the zero-based row index.

        ``column_index`` is the zero-based column index.

        Example:
        | Double Click Listview Cell By Index | id:addressList | 0 | 0 |
        """
        cell = self._get_cell_by_index(locator, row_index, column_index)
        cell.DoubleClick()

    @keyword
    def double_click_listview_row(self, locator, column_name, cell_text):
        """Double clicks a listview row.

        ``locator`` is the locator of the listview.

        ``column_name`` and ``cell_text`` define the row. Row is the first matching row where text in column
        ``column_name`` is ``cell_text``.

        Example:
        | Double Click Listview Row | id:addressList | City | Helsinki | # double click row that has the text "Helsinki" in the column "City" |
        """
        row = self._get_row(locator, column_name, cell_text)
        row.DoubleClick()

    @keyword
    def double_click_listview_row_by_index(self, locator, row_index):
        """Double clicks a listview row at index.

        ``locator`` is the locator of the listview.

        ``row_index`` is the zero-based row index.

        Example:
        | Double Click Listview Row By Index | id:addressList | 4 |
        """
        row = self._get_row_by_index(locator, row_index)
        row.DoubleClick()

    @keyword
    def get_listview_cell_text(self, locator, column_name, row_index):
        """Returns text of a listview cell.

        See `Double Click Listview Cell` for details about arguments ``locator``, ``column_name``, and ``row_index``.
        """
        cell = self._get_cell(locator, column_name, row_index)
        return cell.Text

    @keyword
    def get_listview_cell_text_by_index(self, locator, row_index, column_index):
        """Returns text of a listview cell at index.

        See `Double Click Listview Cell By Index` for details about arguments ``locator``, ``row_index``, and ``column_index``.
        """
        cell = self._get_cell_by_index(locator, row_index, column_index)
        return cell.Text

    @keyword
    def get_listview_row_text(self, locator, column_name, cell_text):
        """Returns a list containing text of each cell in a listview row.

        See `Double Click Listview Row` for details about the arguments ``locator``, ``column_name``, and ``cell_text``.
        """
        row = self._get_row(locator, column_name, cell_text)
        return [cell.Text for cell in row.Cells]

    @keyword
    def get_listview_row_text_by_index(self, locator, row_index):
        """Returns text of a listview row as a list.

        See `Double Click Listview Row By Index` for details about arguments ``locator`` and ``row_index``.
        """
        row = self._get_row_by_index(locator, row_index)
        return [cell.Text for cell in row.Cells]

    @keyword
    def listview_cell_at_index_should_contain(self, locator, row_index, column_index, expected):
        """Verifies that the given listview cell contains text ``expected``.

        See `Double Click Listview Cell By Index` for details about arguments ``locator``, ``row_index``, and ``column_index``.
        """
        cell = self._get_cell_by_index(locator, row_index, column_index)
        if expected not in cell.Text:
            raise AssertionError("Cell ({}, {}) did not contain text '{}'"
                                 .format(row_index, column_index, expected))

    @keyword
    def listview_cell_at_index_should_not_contain(self, locator, row_index, column_index, expected):
        """Verifies that the given listview cell does not contain text ``expected``.

        See `Double Click Listview Cell By Index` for details about arguments ``locator``, ``row_index``, and ``column_index``.
        """
        cell = self._get_cell_by_index(locator, row_index, column_index)
        if expected in cell.Text:
            raise AssertionError("Cell ({}, {}) should not have contained text '{}'"
                                 .format(row_index, column_index, expected))

    @keyword
    def listview_cell_should_contain(self, locator, column_name, row_index, expected):
        """Verifies that the given listview cell contains text ``expected``.

        See `Double Click Listview Cell` for details about arguments ``locator``, ``column_name``, and ``row_index``.
        """
        cell = self._get_cell(locator, column_name, row_index)
        if expected not in cell.Text:
            raise AssertionError("Cell did not contain text '{}'"
                                 .format(expected))

    @keyword
    def listview_cell_should_not_contain(self, locator, column_name, row_index, expected):
        """Verifies that the given listview cell does not contain text ``expected``.

        See `Double Click Listview Cell` for details about arguments ``locator``, ``column_name``, and ``row_index``.
        """
        cell = self._get_cell(locator, column_name, row_index)
        if expected in cell.Text:
            raise AssertionError("Cell should not have contained text '{}'"
                                 .format(expected))

    @keyword
    def listview_cell_text_at_index_should_be(self, locator, row_index, column_index, expected):
        """Verifies that listview cell text is ``expected``.

        See `Double Click Listview Cell By Index` for details about arguments ``locator``, ``row_index``, and ``column_index``.
        """
        cell = self._get_cell_by_index(locator, row_index, column_index)
        if cell.Text != expected:
            raise AssertionError("Cell ({}, {}) text should have been '{}', found '{}'"
                                 .format(row_index, column_index, expected, cell.Text))

    @keyword
    def listview_cell_text_at_index_should_not_be(self, locator, row_index, column_index, expected):
        """Verifies that listview cell text is not ``expected``.

        See `Double Click Listview Cell By Index` for details about arguments ``locator``, ``row_index``, and ``column_index``.
        """
        cell = self._get_cell_by_index(locator, row_index, column_index)
        if cell.Text == expected:
            raise AssertionError("Cell ({}, {}) text should not have been '{}'"
                                 .format(row_index, column_index, expected))

    @keyword
    def listview_cell_text_should_be(self, locator, column_name, row_index, expected):
        """Verifies that listview cell text is ``expected``.

        See `Double Click Listview Cell` for details about arguments ``locator``, ``column_name``, and ``row_index``.
        """
        cell = self._get_cell(locator, column_name, row_index)
        if cell.Text != expected:
            raise AssertionError("Cell text should have been '{}', found '{}'".format(expected, cell.Text))

    @keyword
    def listview_cell_text_should_not_be(self, locator, column_name, row_index, expected):
        """Verifies that listview cell text is not ``expected``.

        See `Double Click Listview Cell` for details about arguments ``locator``, ``column_name``, and ``row_index``.
        """
        cell = self._get_cell(locator, column_name, row_index)
        if cell.Text == expected:
            raise AssertionError("Cell text should not have been '{}'"
                                 .format(expected))

    @keyword
    def listview_row_at_index_should_contain(self, locator, row_index, expected):
        """Verifies that any cell in the given listview row contains text ``expected``.

        See `Double Click Listview Row By Index` for details about arguments ``locator`` and ``row_index``.
        """
        row = self._get_row_by_index(locator, row_index)
        for cell in row.Cells:
            if expected in cell.Text:
                return
        raise AssertionError("Row {} did not contain text '{}'"
                             .format(row_index, expected))

    @keyword
    def listview_row_at_index_should_not_contain(self, locator, row_index, expected):
        """Verifies that any cell in the given listview row does not contain text ``expected``.

        See `Double Click Listview Row By Index` for details about arguments ``locator`` and ``row_index``.
        """
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        row = listview.Rows.Get(int(row_index))
        for cell in row.Cells:
            if expected in cell.Text:
                raise AssertionError("Row {} should not have contained text '{}'"
                                     .format(row_index, expected))

    @keyword
    def listview_row_should_contain(self, locator, column_name, cell_text, expected):
        """Verifies that the given listview row contains text ``expected``.

        See `Double Click Listview Row` for details about the arguments ``locator``, ``column_name``, and ``cell_text``.
        """
        row = self._get_row(locator, column_name, cell_text)
        for cell in row.Cells:
            if expected in cell.Text:
                return
        raise AssertionError("Row defined by cell '{}'='{}' did not contain text '{}'"
                             .format(column_name, cell_text, expected))

    @keyword
    def listview_row_should_not_contain(self, locator, column_name, cell_text, expected):
        """Verifies that the given listview row does not contain text ``expected``.

        See `Double Click Listview Row` for details about the arguments ``locator``, ``column_name``, and ``cell_text``.
        """
        row = self._get_row(locator, column_name, cell_text)
        for cell in row.Cells:
            if expected in cell.Text:
                raise AssertionError("Row defined by cell '{}'='{}' should not have contained text '{}'"
                                     .format(column_name, cell_text, expected))

    @keyword
    def right_click_listview_cell(self, locator, column_name, row_index):
        """Right clicks a listview cell using its column name and row index.

        See `Double Click Listview Cell` for details about arguments ``locator``, ``column_name``, and ``row_index``.
        """
        cell = self._get_cell(locator, column_name, row_index)
        cell.RightClick()

    @keyword
    def right_click_listview_cell_by_index(self, locator, row_index, column_index):
        """Right clicks a listview cell at index.

        See `Double Click Listview Cell By Index` for details about arguments ``locator``, ``row_index``, and ``column_index``.
        """
        cell = self._get_cell_by_index(locator, row_index, column_index)
        cell.RightClick()

    @keyword
    def right_click_listview_row(self, locator, column_name, cell_text):
        """Right clicks a listview row that has given text in given column.

        See `Double Click Listview Row` for details about the arguments ``locator``, ``column_name``, and ``cell_text``.
        """
        row = self._get_row(locator, column_name, cell_text)
        row.RightClick()

    @keyword
    def right_click_listview_row_by_index(self, locator, row_index):
        """Right clicks a listview row at index.

        See `Double Click Listview Row By Index` for details about arguments ``locator`` and ``row_index``.
        """
        row = self._get_row_by_index(locator, row_index)
        row.RightClick()

    @keyword
    def select_listview_cell(self, locator, column_name, row_index):
        """Selects a listview cell.

        See `Double Click Listview Cell` for details about arguments ``locator``, ``column_name``, and ``row_index``.
        """
        cell = self._get_cell(locator, column_name, row_index)
        cell.Click()

    @keyword
    def select_listview_cell_by_index(self, locator, row_index, column_index):
        """Selects a listview cell at index.

        See `Double Click Listview Cell By Index` for details about arguments ``locator``, ``row_index``, and ``column_index``.
        """
        cell = self._get_cell_by_index(locator, row_index, column_index)
        cell.Click()

    @keyword
    def select_listview_row(self, locator, column_name, cell_text):
        """Selects a listview row.

        See `Double Click Listview Row` for details about the arguments ``locator``, ``column_name``, and ``cell_text``.
        """
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        listview.Select(column_name, cell_text)

    @keyword
    def select_listview_row_by_index(self, locator, row_index):
        """Selects a listview row at index.

        See `Double Click Listview Row By Index` for details about arguments ``locator`` and ``row_index``.
        """
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        listview.Select(int(row_index))

    def _get_row(self, locator, column_name, cell_text):
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        return listview.Rows.Get(column_name, cell_text)

    def _get_row_by_index(self, locator, index):
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        return listview.Rows.Get(int(index))

    def _get_cell(self, locator, column_name, row_index):
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        return listview.Cell(column_name, int(row_index))

    def _get_cell_by_index(self, locator, row, column):
        listview = self.state._get_typed_item_by_locator(ListView, locator)
        return listview.Rows.Get(int(row)).Cells[int(column)]
