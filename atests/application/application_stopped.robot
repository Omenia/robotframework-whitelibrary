*** Settings ***
Library    WhiteLibrary
Resource    ../resource.robot
Test Setup    Launch Application    ${TEST_APPLICATION}

*** Variables ***
${PROCESS_NAME}    UIAutomationTest

*** Test Cases ***
Wait Until Application Has Stopped
    Close Application
    Wait Until Application Has Stopped    ${PROCESS_NAME}     20

Failing Wait Until Application Has Stopped
    Run Keyword And Expect Error    Application 'UIAutomationTest' did not exit within 1 second    Wait Until Application Has Stopped    ${PROCESS_NAME}     1
    [Teardown]    Close Application
