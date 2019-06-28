*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Suite Setup    Setup For Tab 2 Tests
Suite Teardown    Select Tab Page    tabControl    Tab1
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

Verify Mouse Right Button Down
    Click Item    event_label
    Mouse Right Button Down
    Verify Label    selectionIndicatorLabel    right button down

Verify Mouse Right Button Down And Up
    Click Item    event_label
    ${MOUSE_X}    ${MOUSE_Y}    Get Mouse Location
    Mouse Right Button Down    ${MOUSE_X}    ${MOUSE_Y}
    Sleep    1
    Mouse Right Button Up
    Verify Label    selectionIndicatorLabel    right button up

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
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Click
    Click Item    event_label
    Sleep    2
    Mouse Click
    Verify Label    selectionIndicatorLabel    left button up

Verify Mouse Click With Offset
    Click Item    event_label    3    3
    Verify Label    selectionIndicatorLabel    left button up

Verify Mouse Click With Negative Offset
    Click Item    event_label    -10    -10
    Verify Label    selectionIndicatorLabel    left button up

Verify Mouse Click With Out Of Bounds Offset
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Click Item    event_label    -100    -100
    Should Contain    ${error_msg}    click location out of bounds

Verify Mouse Right Click With Offset
    Right Click Item    event_label     3    3
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Right Click With Negative Offset
    Right Click Item    event_label    -10    -10
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Right Click With Out Of Bounds Offset
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Right Click Item    event_label    -100    -100
    Should Contain    ${error_msg}    click location out of bounds

Verify Mouse Double Click With Offset
    Double Click Item    event_label     3    3
    Verify Label    selectionIndicatorLabel    left button up

Verify Mouse Double Click With Negative Offset
    Double Click Item    event_label    -10    -10
    Verify Label    selectionIndicatorLabel    left button up

Verify Mouse Double Click With Out Of Bounds Offset
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Double Click Item    event_label    -100    -100
    Should Contain    ${error_msg}    click location out of bounds

Verify Mouse Right Double Click
    Click Item    event_label
    Sleep    1
    Mouse Right Double Click
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Double Click
    Click Item    event_label
    Sleep    1
    Mouse Double Click
    Verify Label    selectionIndicatorLabel    left button up

Verify Incomplete Mouse Position Exception
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Mouse Click    300
    Should Contain    ${error_msg}    Either x or y value missing
