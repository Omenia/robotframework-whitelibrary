*** Settings ***
Resource    ../resource.robot
Suite Setup    Setup For Tab 2 Tests
Suite Teardown    Select Tab Page    tabControl    Tab1

*** Variables ***
${SLOW_ALERT_BTN}    text:Slow alert
${FAST_ALERT_BTN}    text:Fast alert
${SLOW_ALERT}    text:Slow alert occurred
${FAST_ALERT}    text:Fast alert occurred

*** Test Cases ***
Successful Wait Until Item Exists
    Click And Wait For Fast Alert
    Click Slow Alert
    Wait Until Item Exists    ${SLOW_ALERT}    7 seconds

Successful Wait Until Item Does Not Exist
    Click And Wait For Fast Alert
    Click Slow Alert
    Wait Until Item Does Not Exist    ${FAST_ALERT}    6 seconds

Failing Wait Until Item Exists
    Click And Wait For Fast Alert
    Click Slow Alert
    ${error_msg}    Run Keyword And Expect Error    *    Wait Until Item Exists    ${SLOW_ALERT}    2 seconds
    Should Contain    ${error_msg}    Item with locator '${SLOW_ALERT}' was not visible in 2.0 seconds
    [Teardown]    Wait Until Item Exists     ${SLOW_ALERT}    6 seconds

Failing Wait Until Item Does Not Exist
    Click And Wait For Fast Alert
    Click Slow Alert
    ${error_msg}    Run Keyword And Expect Error    *    Wait Until Item Does Not Exist    ${FAST_ALERT}    2 seconds
    Should Contain    ${error_msg}    Item with locator '${FAST_ALERT}' did not disappear in 2.0 seconds
    [Teardown]    Wait Until Item Exists     ${SLOW_ALERT}    6 seconds

*** Keywords ***
Click And Wait For Fast Alert
    Click Button    ${FAST_ALERT_BTN}
    Wait Until Item Exists    ${FAST_ALERT}    3 seconds

Click Slow Alert
    Click Button    ${SLOW_ALERT_BTN}
