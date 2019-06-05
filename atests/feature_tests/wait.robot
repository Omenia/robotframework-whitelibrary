*** Settings ***
Resource    ../resource.robot
Suite Setup    Setup For Tab 2 Tests
Suite Teardown    Select Tab Page    tabControl    Tab1

*** Test Cases ***
Successful Wait Until Item Exists
    Select ListView Row By Index    birds    1
    Click Button    text:Slow alert
    Wait Until Item Exists    text:Slow alert occurred    6 seconds

Successful Wait Until Item Does Not Exist
    Click Button    text:Fast alert
    Wait Until Item Exists    text:Fast alert occurred    3 seconds
    Click Button    text:Slow alert
    Wait Until Item Does Not Exist    text:Fast alert occurred    6 seconds

Failing Wait Until Item Exists
    Fail    To be implemented

Failing Wait Until Item Does Not Exist
    Fail    To be implemented