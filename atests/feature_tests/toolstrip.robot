*** Settings ***
Library     WhiteLibrary
Resource    ../resource.robot
Suite Setup    Setup for Tab 2 Tests
Suite Teardown    Select Tab Page    tabControl    Tab1

*** Test Cases ***
Click Toolstrip Buttons By Index
    Click Toolstrip Button By Index    tools    1
    Verify Label    selectionIndicatorLabel    Toolstrip button 1 clicked
    Click Toolstrip Button By Index    tools    2
    Verify Label    selectionIndicatorLabel    Toolstrip button 2 clicked
    Click Toolstrip Button By Index    tools    3
    Verify Label    selectionIndicatorLabel    Toolstrip button 3 clicked

Click Nonexisting Toolstrip Index
    ${error}    Run Keyword And Expect Error    *    Click Toolstrip Button By Index    tools    4
    Should Be Equal    ${error}    IndexError: Invalid ToolStrip button index '4'