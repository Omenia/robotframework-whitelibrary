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

Verify Mouse Click
    Click Item    event_label
    Sleep    2
    Mouse Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    left button up

Verify Mouse Click With Offset
    [Tags]    under_test
    Click Button    test_button    3    3
    Sleep    2
    Verify Label    selectionIndicatorLabel    left clicked

Verify Mouse Click With Negative Offset
    [Tags]    under_test
    Click Button    test_button    -13    -13
    Sleep    2
    Verify Label    selectionIndicatorLabel    left clicked

Verify Mouse Click With Out Of Bounds Offset
    [Tags]    under_test
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Click Button    test_button    -100    -100
    Should Contain    ${error_msg}    click location out of bounds


Verify Mouse Right Double Click
    Click Item    event_label
    Sleep    2
    Mouse Right Double Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    right button up

Verify Mouse Double Click
    Click Item    event_label
    Sleep    2
    Mouse Double Click
    Sleep    2
    Verify Label    selectionIndicatorLabel    left button up

Verify Incomplete Mouse Position Exception
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Mouse Click    300
    Should Contain    ${error_msg}    Either x or y value missing
