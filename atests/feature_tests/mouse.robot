*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Suite Setup    Setup For Tab 2 Tests
Suite Teardown	Select Tab Page    tabControl    Tab1
Resource          ..${/}resource.robot

*** Test Cases ***

Verify Mouse Position
    Set Mouse Location    300    90
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Should Be Equal As Numbers    300    ${MOUSE_X}
    Should Be Equal As Numbers    90    ${MOUSE_Y}

Verify Mouse Position Warning
    Set Mouse Location    -5000    -5000
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Should Not Be Equal As Numbers    -5000    ${MOUSE_X}
    Should Not Be Equal As Numbers    -5000    ${MOUSE_Y}


Verify Mouse Move
    Set Mouse Location    300    90
    Move Mouse    30    -30
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Should Be Equal As Numbers    330    ${MOUSE_X}
    Should Be Equal As Numbers    60    ${MOUSE_Y}

Verify Mouse Left Button Down
    Click Item    event_label
    Mouse Left Button Down
    Verify Label    selectionIndicatorLabel    left button down

Verify Mouse Left Button Down And Up
    Click Item    event_label
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Mouse Left Button Down    ${MOUSE_X}    ${MOUSE_Y}
    Sleep    1
    Mouse Left Button Up
    Verify Label    selectionIndicatorLabel    left button up

Verify Mouse Right Click
    Click Item    event_label
    Sleep    2
    Mouse Right Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Left Click
    Click Item    event_label
    Sleep    2
    Mouse Left Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    left button up

Verify Mouse Right Double Click
    Click Item    event_label
    Sleep    2
    Mouse Right Double Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Left Double Click
    Click Item    event_label
    Sleep    2
    Mouse Left Double Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    left button up
