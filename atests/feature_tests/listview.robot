*** Settings ***
Library    WhiteLibrary
Resource    ../resource.robot
Suite Setup    Setup for Tab 2 Tests
Suite Teardown    Select Tab Page    tabControl    Tab1

*** Test Cases ***
Verify ListView Row
    Listview Row Should Contain    list_view2    Title    Bible    ligious
    Listview Row Should Not Contain    list_view2    Title    Robinson Crusoe    Scienc
    Listview Row In Index Should Contain    list_view2    2    Programming
    Listview Row In Index Should Not Contain    list_view2    1    Donald

Verify ListView Cell
    Listview Cell Text Should Be    list_view2    Title    2    The Art of Computer Programming
    Listview Cell Text Should Not Be    list_view2    Title    2    Robinson Crusoe
    Listview Cell Text In Index Should Be   list_view2    2    1    The Art of Computer Programming
    Listview Cell Text In Index Should Not Be    list_view2    2    1    Robinson Crusoe

    Listview Cell Should Contain    list_view2    Title    2    omputer
    Listview Cell Should Not Contain    list_view2    Title    2    obinson
    Listview Cell In Index Should Contain    list_view2    2    1    omputer
    Listview Cell In Index Should Not Contain    list_view2    2    1    obinson

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

*** Keywords ***
Setup For Tab 2 Tests
    Attach Main Window
    Select Tab Page    tabControl    Tab2
