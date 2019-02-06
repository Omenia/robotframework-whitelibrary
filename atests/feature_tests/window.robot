*** Settings ***
Library    WhiteLibrary
Library    Process
Test Setup    Window Test Setup
Test Teardown    Window Test Teardown
Resource    ..${/}resource.robot

*** Test Cases ***
Get All Application Windows
    @{windows}=    List Application Windows
    Length Should Be    ${windows}    1
    Click Button    window_button
    Click Button    window_button
    @{windows}=    List Application Windows
    Length Should Be    ${windows}    3

Get All Desktop Windows
    @{windows}=    List Desktop Windows
    ${windows_len}=    Get Length    ${windows}
    Log    There are ${windows_len} windows in desktop



*** Keywords ***
Window Test Setup
    Attach Main Window
    Setup For Tab 2 Tests

Window Test Teardown
    Select Tab Page    tabControl    Tab1

Start Test Application
    ${handle} =    Start Process    ${TEST APPLICATION}
    Set Test Variable    ${handle}
    ${test application id} =    Get Process Id    ${handle}
    Set Test Variable    ${test application id}

Application Should Be Attached
    Attach Window    UI Automation Test Window
    Verify Label    lblA    Value 1
