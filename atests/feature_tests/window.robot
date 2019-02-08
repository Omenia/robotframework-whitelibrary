*** Settings ***
Library    WhiteLibrary
Library    Process
Test Setup    Window Test Setup
Test Teardown    Window Test Teardown
Suite Setup    Window Test Suite Setup
Suite Teardown    Window Test Suite Teardown
Resource    ..${/}resource.robot

*** Test Cases ***
Get All Application Windows
    @{several_windows}=    List Application Windows
    Length Should Be    ${several_windows}    5
    Log    ${several_windows[0]}
    Log    ${several_windows[1]}
    Log    ${several_windows[2]}
    Log    ${several_windows[3]}
    Log    ${several_windows[4]}
    Should Be Equal As Strings     ${several_windows[0]}    Test title - 4
    Should Be Equal As Strings     ${several_windows[1]}    UI Automation Test Window
    Should Be Equal As Strings     ${several_windows[2]}    Test title - 3
    Should Be Equal As Strings     ${several_windows[3]}    Test title - 2
    Should Be Equal As Strings     ${several_windows[4]}    Test title - 1

Get All Desktop Windows
    @{windows}=    List Desktop Windows
    ${windows_len}=    Get Length    ${windows}
    Log    There are ${windows_len} windows in desktop

Get All Application Windows By Index
    Attach Window By Index    2
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 3

Attach Application Window By List Object
    @{several_windows}=    List Application Windows
    Attach Window    ${several_windows[2].Name}
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 3
    Log    ${several_windows[0]}
    Attach Window    ${several_windows[0].Name}
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 4

Attach Desktop Window By Name
    Attach Window    name:Test title - 1
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 1
    Attach Window    name:Test title - 2
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 2

Attach Desktop Window By Index
    Attach Window    index:1
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 4
    Attach Window    index:4
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 1

*** Keywords ***
Window Test Suite Setup
    Attach Main Window
    Setup For Tab 2 Tests
    Click Button    window_button
    Click Button    window_button
    Click Button    window_button
    Click Button    window_button

Window Test Suite Teardown
    Close Window    Test title - 4
    Close Window    Test title - 3
    Close Window    Test title - 2
    Close Window    Test title - 1

Window Test Setup
    No Operation

Window Test Teardown
    No Operation
