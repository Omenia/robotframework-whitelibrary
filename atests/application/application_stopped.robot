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
    Close Application
    Wait Until Application Has Stopped    ${PROCESS_NAME}     1
