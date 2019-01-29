*** Settings ***
Documentation     These tests launch application and run some
...    failed dummy keyword. After this screenshot must be created
...    in application folder.

Library    OperatingSystem
Library    String
Library    WhiteLibrary
Suite Setup    Launch Application For Test
Suite Teardown    Close Application
Test Setup    Attach Main Window
Test Teardown    Clean Application
Resource          resource.robot

*** Test Cases ***
Take screenshots
    [Setup]    Screenshot Setup
    Take Desktop Screenshot
    New Screenshot Should Be Created
    Take Desktop Screenshot
    New Screenshot Should Be Created

Take Screenshot On failure
    [Setup]    Screenshot Setup
    Run Keyword And Expect Error    *    Should Be True    ${FALSE}
    New Screenshot Should Be Created

Disable And Enable Screenshots On Failure
    [Setup]    Screenshot Setup
    Take Screenshots On Failure    false
    Run Keyword And Expect Error    *    Should Be True    ${FALSE}
    New Screenshot Should Not Be Created
    Take Screenshots On Failure    ${True}
    Run Keyword And Expect Error    *    Should Be True    ${FALSE}
    New Screenshot Should Be Created

*** Keywords ***

Screenshot Setup
    Attach Main Window
    ${COUNT}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Set Test Variable    ${COUNT}

New Screenshot Should Be Created
    ${new_count}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Should Be Equal    ${new_count}    ${COUNT+1}
    Set Test Variable    ${COUNT}    ${new_count}

New Screenshot Should Not Be Created
    ${new_count}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Should Be Equal    ${new_count}    ${COUNT}

