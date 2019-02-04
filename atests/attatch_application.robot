*** Settings ***
Library    WhiteLibrary
Library    Process
Test Setup    Start Test Application
Test Teardown    Terminate Process    ${handle}    kill=true
Resource    resource.robot

*** Test Cases ***
Attach To A Running Application By Name
    Attach Application By Name    ${TEST APPLICATION NAME}
    Application Should Be Attached

Attach To A Running Application By Id
    Attach Application By Id    ${test application id}
    Application Should Be Attached

Attach Window Successfully
    Attach Application By Name    ${TEST APPLICATION NAME}
    Attach Main Window

Attach Nonexisting Window
    Attach Application By Id    ${test application id}
    Set White Find Window Timeout    2 s
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Attach Window    Bogus Window
    Should Contain    ${error_msg}    after waiting for 2 seconds
    Set White Find Window Timeout    30 s


*** Keywords ***
Start Test Application
    ${handle} =    Start Process    ${TEST APPLICATION}
    Set Test Variable    ${handle}
    ${test application id} =    Get Process Id    ${handle}
    Set Test Variable    ${test application id}

Application Should Be Attached
    Attach Window    UI Automation Test Window
    Verify Label    lblA    Value 1
