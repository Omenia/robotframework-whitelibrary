*** Variables ***
${TEST APPLICATION}      ${EXECDIR}${/}UIAutomationTest${/}bin${/}Debug${/}UIAutomationTest.exe

*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Suite Setup    None
Test Teardown    White Configuration Parameters Restore

*** Test Cases ***
Set White Busy Timeout
    Set White Busy Timeout    10 s
    ${BUSY_TIMEOUT}    Get White Busy Timeout
    Should Be Equal   ${BUSY_TIMEOUT}    10000 milliseconds

Set White Find Window Timeout
    Set White Find Window Timeout    10 s
    ${WHITE FIND WINDOW_TIMEOUT}    Get White Find Window Timeout
    Should Be Equal    ${WHITE FIND WINDOW_TIMEOUT}    10000 milliseconds

Set White Double Click Timeout
    Set White Double Click Interval    0.05 seconds
    ${WHITE_DOUBLE_CLICK_INTERVAL}    Get White Double Click Interval
    Should Be Equal    ${WHITE_DOUBLE_CLICK_INTERVAL}    50 milliseconds

Set White Drag Step Count
    Set White Drag Step Count    3
    ${WHITE_DRAG_STEP_COUNT}    Get White Drag Step Count
    Should Be Equal    ${WHITE_DRAG_STEP_COUNT}    ${3}

*** Keywords ***
White Configuration Parameters Restore
    #These defaults are defined in White Stack source code.
    Set White Busy Timeout    5000 ms
    Set White Find Window Timeout    30000 ms
    Set White Double Click Interval    0 ms
