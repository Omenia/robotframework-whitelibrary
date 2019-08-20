*** Settings ***
Library     WhiteLibrary
Resource    ../resource.robot
Suite Setup    Setup for Tab 2 Tests
Suite Teardown    Select Tab Page    tabControl    Tab1

*** Test Cases ***
Row Verification
    Listview Row Should Contain    list_view2    Title    Bible    ligious
    Listview Row Should Not Contain    list_view2    Title    Robinson Crusoe    Scienc
    Listview Row At Index Should Contain    list_view2    2    Programming
    Listview Row At Index Should Not Contain    list_view2    1    Donald

Cell Verification
    Listview Cell Text Should Be    list_view2    Title    2    The Art of Computer Programming
    Listview Cell Text Should Not Be    list_view2    Title    2    Robinson Crusoe
    Listview Cell Text At Index Should Be   list_view2    2    1    The Art of Computer Programming
    Listview Cell Text At Index Should Not Be    list_view2    2    1    Robinson Crusoe

    Listview Cell Should Contain    list_view2    Title    2    omputer P
    Listview Cell Should Not Contain    list_view2    Title    2    obinson
    Listview Cell At Index Should Contain    list_view2    2    1    omputer
    Listview Cell At Index Should Not Contain    list_view2    2    1    obinson

Unsuccessful Row Verification
    Run Keyword And Expect Error    Row defined by cell 'Title'='Bible' did not contain text 'abcd'
    ...                             Listview Row Should Contain    list_view2    Title    Bible    abcd
    Run Keyword And Expect Error    Row defined by cell 'Title'='Robinson Crusoe' should not have contained text 'Fiction'
    ...                             Listview Row Should Not Contain    list_view2    Title    Robinson Crusoe    Fiction
    Run Keyword And Expect Error    Row 2 did not contain text 'abcd'
    ...                             Listview Row At Index Should Contain    list_view2    2    abcd
    Run Keyword And Expect Error    Row 1 should not have contained text 'igious'
    ...                             Listview Row At Index Should Not Contain    list_view2    1    igious

Unsuccessful Cell Verification
    Run Keyword And Expect Error    Cell text should have been 'Hello', found 'The Art of Computer Programming'
    ...                             Listview Cell Text Should Be    list_view2    Title    2    Hello

    Run Keyword And Expect Error    Cell text should not have been 'The Art of Computer Programming'
    ...                             Listview Cell Text Should Not Be    list_view2    Title    2    The Art of Computer Programming

    Run Keyword And Expect Error    Cell (2, 1) text should have been 'Hello', found 'The Art of Computer Programming'
    ...                             Listview Cell Text At Index Should Be   list_view2    2    1    Hello

    Run Keyword And Expect Error    Cell (2, 1) text should not have been 'The Art of Computer Programming'
    ...                             Listview Cell Text At Index Should Not Be    list_view2    2    1    The Art of Computer Programming

    Run Keyword And Expect Error    Cell did not contain text 'obinson'
    ...                             Listview Cell Should Contain    list_view2    Title    2    obinson

    Run Keyword And Expect Error    Cell should not have contained text 'omputer'
    ...                             Listview Cell Should Not Contain    list_view2    Title    2    omputer

    Run Keyword And Expect Error    Cell (2, 1) did not contain text 'obinson'
    ...                             Listview Cell At Index Should Contain    list_view2    2    1    obinson

    Run Keyword And Expect Error    Cell (2, 1) should not have contained text 'omputer'
    ...                             Listview Cell At Index Should Not Contain    list_view2    2    1    omputer

Get Text From ListView
    ${expected}    Create List    Donald Knuth    The Art of Computer Programming    Science
    ${actual}    Get Listview Row Text    list_view2    Category    Science
    Should Be Equal    ${actual}    ${expected}

    ${expected}    Create List    Daniel Defoe    Robinson Crusoe    Fiction
    ${actual}    Get Listview Row Text By Index    list_view2    0
    Should Be Equal    ${actual}    ${expected}

    ${actual}    Get Listview Cell Text    list_view2    Author    0
    Should Be Equal    ${actual}    Daniel Defoe

    ${actual}    Get Listview Cell Text By Index    list_view2    2    2
    Should Be Equal    ${actual}    Science

Select Listview Row
    Select ListView Row By Index    birds    1
    Selection Indicator Should Be     Row 1    Selected
    Select ListView Row By Index    list_view    2
    Selection Indicator Should Be    Row 2     Selected
    Select ListView Row    list_view    Title    Robinson Crusoe
    Selection Indicator Should Be    Row 0     Selected
    Select Listview Row By Text    list_view    The Art of Computer Programming
    Selection Indicator Should Be     Row 2     Selected

Select Listview Cell
    Select Listview Cell    list_view2    Author    1
    Selection Indicator Should Be    Various Artists     Selected
    Select Listview Cell By Index    list_view2    2    2
    Selection Indicator Should Be    Science    Selected

Right Click Listview Row
    # click twice because first click selects the row
    Repeat Keyword    2    Right Click Listview Row    birds    Bird    Dodo
    Selection Indicator Should Be     Row 2     Right Clicked
    Repeat Keyword    2    Right Click Listview Row By Index    birds    0
    Selection Indicator Should Be    Row 0     Right Clicked
    Repeat Keyword    2    Right Click Listview Row By Text    birds    Varpuspöllö
    Selection Indicator Should Be     Row 3     Right Clicked

Right Click Listview Cell
    Repeat Keyword    2    Right Click Listview Cell    list_view2    Title    1
    Selection Indicator Should Be    Bible     Right Clicked
    Repeat Keyword    2    Right Click Listview Cell By Index    list_view2    0    0
    Selection Indicator Should Be    Daniel Defoe     Right Clicked

Double Click Listview Row
    Double Click ListView Row    birds    Bird    Dodo
    Selection Indicator Should Be    Row 2     Double Clicked
    Double Click ListView Row By Index    birds    1
    Selection Indicator Should Be    Row 1     Double Clicked
    Double Click Listview Row By Text    list_view    The Art of Computer Programming
    Selection Indicator Should Be    Row 2    Double Clicked

Double Click Listview Cell
    Double Click Listview Cell    list_view2    Author    2
    Selection Indicator Should Be    Donald Knuth    Double Clicked
    Double Click Listview Cell By Index    list_view2    0    2
    Selection Indicator Should Be    Fiction    Double Clicked

Listview Row With Non-Ascii Chars
    Run Keyword And Expect Error    Cell did not contain text 'pölö'
    ...                             Listview Cell Should Contain    birds    Bird    3    pölö
    Run Keyword And Expect Error    Cell should not have contained text 'pöllö'
    ...                             ListView Cell Should Not Contain    birds    Bird    3    pöllö
    Run Keyword And Expect Error    Cell (3, 0) did not contain text 'pölö'
    ...                             ListView Cell At Index Should Contain    birds    3    0    pölö
    Run Keyword And Expect Error    Cell (3, 0) should not have contained text 'pöllö'
    ...                             ListView Cell At Index Should Not Contain    birds    3    0    pöllö

    Run Keyword And Expect Error    Cell text should have been 'pölö', found 'Varpuspöllö'
    ...                             Listview Cell Text Should Be    birds    Bird    3    pölö
    Run Keyword And Expect Error    Cell text should not have been 'Varpuspöllö'
    ...                             Listview Cell Text Should Not Be    birds    Bird    3    Varpuspöllö
    Run Keyword And Expect Error    Cell (3, 0) text should have been 'pölö', found 'Varpuspöllö'
    ...                             Listview Cell Text At Index Should Be   birds    3    0    pölö
    Run Keyword And Expect Error    Cell (3, 0) text should not have been 'Varpuspöllö'
    ...                             Listview Cell Text At Index Should Not Be    birds    3    0    Varpuspöllö
