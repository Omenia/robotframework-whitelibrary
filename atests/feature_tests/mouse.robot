*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Test Setup    Setup For Tab 2 Tests
#Test Teardown    Tab2 Test Teardown
Resource          ..${/}resource.robot

*** Test Cases ***

Verify Mouse Position
    Set Mouse Location    0    0
    ${WINDOW_LEFT}    ${WINDOW_TOP}    Get Mouse Location
    Set Mouse Location    300    90
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    ${RESULT_X}    Evaluate    ${MOUSE_X}-${WINDOW_LEFT}
    ${RESULT_Y}    Evaluate    ${MOUSE_Y}-${WINDOW_TOP}
    Should Be Equal As Numbers    300    ${RESULT_X}
    Should Be Equal As Numbers    90    ${RESULT_Y}

Verify Mouse Right Button Down
    Click Item    event_label
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Mouse Right Button Down
    Verify Label    selectionIndicatorLabel    right button down

Verify Mouse Left Button Down
    Click Item    event_label
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Mouse Left Button Down
    Verify Label    selectionIndicatorLabel    left button down

Verify Mouse Right Button Down And Up
    Click Item    event_label
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Mouse Right Button Down    ${MOUSE_X}    ${MOUSE_Y}
    Sleep    2
    Mouse Right Button Up
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Left Button Down And Up
    Click Item    event_label
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Mouse Left Button Down    ${MOUSE_X}    ${MOUSE_Y}
    Sleep    2
    Mouse Left Button Up
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Right Click
    Click Item    event_label
    Sleep    2
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Mouse Right Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Left Click
    Click Item    event_label
    Sleep    2
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Mouse Left Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    left button up


*** Keywords ***
Tab2 Test Teardown
    Select Tab Page    tabControl    Tab
