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

Attach To A Running Application By Invalid Name
    Run Keyword And Expect Error  STARTS: Unable to locate application with identifier: ${INVALID TEST APPLICATION NAME}
    ...                           Attach Application By Name    ${INVALID TEST APPLICATION NAME}

Attach To A Running Application By Invalid Name With Timeout
    Run Keyword And Expect Error  STARTS: Unable to locate application with identifier: ${INVALID TEST APPLICATION NAME}
    ...                           Attach Application By Name    ${INVALID TEST APPLICATION NAME}    timeout=20 seconds

Attach To Application With Timeout
    [Setup]           Delayed Start Test Application
    [Timeout]         1 minute
    [Teardown]        Terminate Process   delayed   kill=true
    Attach Application By Name    ${TEST APPLICATION NAME}    timeout=1 minute
    Application Should Be Attached
    Close Application

*** Keywords ***
Delayed Start Test Application
    Start Process   ${DELAYED TEST APPLICATION}    alias=delayed   stdout=${EXECDIR}${/}output${/}stdout.txt   stderr=${EXECDIR}${/}output${/}stderr.txt

Start Test Application
    ${handle} =    Start Process    ${TEST APPLICATION}
    Set Test Variable    ${handle}
    ${test application id} =    Get Process Id    ${handle}
    Set Test Variable    ${test application id}

Application Should Be Attached
    Attach Window    UI Automation Test Window
    Verify Label    lblA    Value 1
