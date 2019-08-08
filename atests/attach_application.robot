*** Settings ***
Library    WhiteLibrary
Library    Process
Library    OperatingSystem
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

Attach To A Running Application By Invalid Name
    Run Keyword And Expect Error  Unable to locate application via identifier: ${INVALID TEST APPLICATION NAME}
    ...                           Attach Application By Name    ${INVALID TEST APPLICATION NAME}

Attach To Application With Timeout
  [Setup]       Delayed Start Test Application
  [Teardown]    Terminate Process   alias=delayed
  Attach Application By Name    ${TEST APPLICATION NAME}    timeout=10000
  Application Should Be Attached

*** Keywords ***
Delayed Start Test Application
    Start Process   ping 127.0.0.1 -n 6 & $(TEST APPLICATION)   shell=True  alias=delayed

Start Test Application
    ${handle} =    Start Process    ${TEST APPLICATION}
    Set Test Variable    ${handle}
    ${test application id} =    Get Process Id    ${handle}
    Set Test Variable    ${test application id}

Application Should Be Attached
    Attach Window    UI Automation Test Window
    Verify Label    lblA    Value 1
