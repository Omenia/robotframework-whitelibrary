*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Test Setup    Setup For Tab 2 Tests
#Test Teardown    Tab2 Test Teardown
Resource          ..${/}resource.robot

*** Test Cases ***

Verify Mouse Position
    Set Mouse Location    300    90
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Verify Label    cursorPosition    292,59

Verify Mouse Right Button Down
    Set Mouse Location    273    353
    Mouse Right Click    273    353
    Verify Label    selectionIndicatorLabel    right button up


*** Keywords ***
Tab2 Test Teardown
    Select Tab Page    tabControl    Tab
