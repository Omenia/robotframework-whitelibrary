*** Variables ***
${TEST APPLICATION}      UIAutomationTest/bin/Debug/UIAutomationTest.exe
${TEST APPLICATION NAME}    UIAutomationTest

*** Settings ***
Library    WhiteLibrary
Library    Process
Test Setup    Start Test Application
Test Teardown    Terminate Process    ${handle}    kill=true

*** Test Cases ***
Attach To A Running Application By Name
    Attach Application By Name    ${TEST APPLICATION NAME}
    Application Should Be Attached

Attach To A Running Application By Id
    Attach Application By Id    ${test application id}
    Application Should Be Attached

*** Keywords ***
Start Test Application
    ${handle} =    Start Process    ${TEST APPLICATION}
    Set Test Variable    ${handle}
    ${test application id} =    Get Process Id    ${handle}
    Set Test Variable    ${test application id}

Application Should Be Attached
    Attach Window    UI Automation Test Window
    Verify Label    lblA    Value 1
