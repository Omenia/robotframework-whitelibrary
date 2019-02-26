*** Settings ***
Library    WhiteLibrary
Library    Process
Suite Setup    Window Test Suite Setup
Suite Teardown    Window Test Suite Teardown
Resource    ../resource.robot

*** Test Cases ***
Get All Application Windows
    @{several_windows}=    List Application Windows
    Length Should Be    ${several_windows}    5
    Should Be Equal As Strings     ${several_windows[0]}    Test title - 4
    Should Be Equal As Strings     ${several_windows[1]}    UI Automation Test Window
    Should Be Equal As Strings     ${several_windows[2]}    Test title - 3
    Should Be Equal As Strings     ${several_windows[3]}    Test title - 2
    Should Be Equal As Strings     ${several_windows[4]}    Test title - 1

Get All Desktop Windows
    @{windows}=    List Desktop Windows
    ${windows_len}=    Get Length    ${windows}
    Should Be True    ${windows_len} >= 5

Attach Application Window By Id
    Attach Window    Test title - 3
    Attach Window    id:mainWindow
    Window Title Should Be    UI Automation Test Window

Attach Application Window By ClassName
    Attach Window    UI Automation Test Window
    Attach Window    class_name:NavigationWindow
    Window Title Should Contain    Test Title -

Attach Window Object
    Attach Window    UI Automation Test Window
    @{windows}=    List Application Windows
    Attach Window    ${windows[3]}
    Window Title Should Be    Test title - 2

*** Keywords ***
Window Test Suite Setup
    Attach Main Window
    Setup For Tab 2 Tests
    Repeat Keyword    4    Click Button    window_button

Window Test Suite Teardown
    Close Window    Test title - 4
    Close Window    Test title - 3
    Close Window    Test title - 2
    Close Window    Test title - 1
