*** Settings ***
Library    WhiteLibrary
Library    Process
Suite Setup    Window Test Suite Setup
Suite Teardown    Window Test Suite Teardown
Resource    ../resource.robot

*** Test Cases ***
Get All Application Windows
    @{windows}=    Get Application Windows
    Length Should Be    ${windows}    5
    Should Be Equal As Strings     ${windows[0]}    Test title - 4
    Should Be Equal As Strings     ${windows[1]}    UI Automation Test Window
    Should Be Equal As Strings     ${windows[2]}    Test title - 3
    Should Be Equal As Strings     ${windows[3]}    Test title - 2
    Should Be Equal As Strings     ${windows[4]}    Test title - 1

Get All Desktop Windows
    @{windows}=    Get Desktop Windows
    ${windows_len}=    Get Length    ${windows}
    Should Be True    ${windows_len} >= 5

Attach Application Window By Id
    Attach Window    Test title - 3
    Attach Window    id:mainWindow
    Window Title Should Be    UI Automation Test Window

Attach Application Window By ClassName
    Attach Window    UI Automation Test Window
    Attach Window    class_name:NavigationWindow
    Window Title Should Contain    Test title -

Attach Window Object
    Attach Window    UI Automation Test Window
    @{windows}=    Get Application Windows
    Attach Window    ${windows[3]}
    Window Title Should Be    Test title - 2

Attach Nonexisting Window
    Set White Find Window Timeout    2 s
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Attach Window    Bogus Window
    Should Contain    ${error_msg}    after waiting for 2.0 seconds
    [Teardown]    Set White Find Window Timeout    30 s

Close Nonexisting Window
    Set White Find Window Timeout    2 s
    Attach Main Window
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Close Window    Bogus Window
    Should Contain    ${error_msg}    after waiting for 2.0 seconds
    [Teardown]    Set White Find Window Timeout    30 s

Minimize Current Window
    Maximize Window
    Minimize Window
    Window Should Be Minimized    ${TEST APPLICATION WINDOW TITLE}
    [Teardown]    Restore Window

Maximize Current Window
    Minimize Window
    Maximize Window
    Window Should Be Maximized
    [Teardown]    Restore Window

Restore Current Window
    Maximize Window
    Restore Window
    Window Should Be Restored
    [Teardown]    Restore Window

Failing Restored Check
    Maximize Window
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Window Should Be Restored
    Should Contain    ${error_msg}    Expected window state to be Restored, but found Maximized
    [Teardown]    Restore Window

Failing Minimized Check
    Restore Window
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Window Should Be Minimized
    Should Contain    ${error_msg}    Expected window state to be Minimized, but found Restored
    [Teardown]    Restore Window

Failing Maximized Check
    Minimize Window
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Window Should Be Maximized
    Should Contain    ${error_msg}    Expected window state to be Maximized, but found Minimized
    [Teardown]    Restore Window

*** Keywords ***
Window Test Suite Setup
    Attach Main Window
    Setup For Tab 2 Tests
    Repeat Keyword    4    Click Button    window_button

Window Test Suite Teardown
    @{windows}=    Get Application Windows
    FOR    ${window}    IN    @{windows}
        Close Window    ${window}
    END
