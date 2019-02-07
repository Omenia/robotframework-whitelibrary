*** Settings ***
Library    WhiteLibrary
Library    Process
Test Setup    Window Test Setup
Test Teardown    Window Test Teardown
Resource    ..${/}resource.robot

*** Test Cases ***
Get All Application Windows
    @{single_window}=    List Application Windows
    Length Should Be    ${single_window}    1
    Click Button    window_button
    Click Button    window_button
    Click Button    window_button
    Click Button    window_button
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
    ${temp}=    Set Variable    ${several_windows[2].Name}
    ${title_type}=    Evaluate    type($temp).__name__
    Log    ${temp} type is ${title_type}
    Attach Window    ${several_windows[2].Name}
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 3
    Log    ${several_windows[0]}
    #TODO: Why several_windows ordering changes. Document the behavior correctly.
    Attach Window    ${several_windows[0].Name}
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    UI Automation Test Window

Attach Desktop Window By Name
    Attach Desktop Window By Name    Test title - 1
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Test title - 1

*** Keywords ***
Window Test Setup
    Attach Main Window
    Setup For Tab 2 Tests

Window Test Teardown
    Attach Main Window
    Select Tab Page    tabControl    Tab1
