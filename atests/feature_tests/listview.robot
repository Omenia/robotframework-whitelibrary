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
    Listview Cell Text Should Be
    Listview Cell Text Should Not Be
    Listview Cell Text In Index Should Be
    Listview Cell Text In Index Should Not Be

    Listview Cell Should Contain
    Listview Cell Should Not Contain
    Listview Cell In Index Should Contain
    Listview Cell In Index Should Not Contain

Get Text From ListView
    ${text}    Get Listview Row Text    list_view2    Category    Science
    Should Be Equal    ${text}    ...

    ${text}    Get Listview Row Text By Index    list_view2    0
    Should Be Equal    ${text}    ...

    ${text}    Get Listview Cell Text    list_view2
    Should Be Equal    ${text}    ...

    ${text}    Get Listview Cell Text By Index
    Should Be Equal    ${text}    ...

*** Keywords ***
Setup For Tab 2 Tests
    Attach Main Window
    Select Tab Page    tabControl    Tab2
