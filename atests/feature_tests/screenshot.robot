*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Test Setup    Attach Main Window
Test Teardown    Clean Application
Resource    ../resource.robot

*** Test Cases ***
Take screenshots
    [Setup]    Screenshot Setup
    Take Desktop Screenshot
    New Screenshot Should Be Created
    Take Desktop Screenshot
    New Screenshot Should Be Created

Take Screenshot On failure
    [Setup]    Screenshot Setup
    Run Keyword And Expect Error    *    Click Item    unexisting-locator=whatever
    New Screenshot Should Be Created

Disable And Enable Screenshots On Failure
    [Setup]    Screenshot Setup
    Take Screenshots On Failure    false
    Run Keyword And Expect Error    *    Click Item    unexisting-locator=whatever
    New Screenshot Should Not Be Created
    Take Screenshots On Failure    ${True}
    Run Keyword And Expect Error    *    Click Item    unexisting-locator=whatever
    New Screenshot Should Be Created

Set Screenshot Directory
    [Setup]    Run Keywords
    ...        Set Test Variable    ${dir}    ${OUTPUTDIR}${/}screenshots    AND
    ...        Remove Directory    ${dir}    recursive=True
    Set Screenshot Directory    ${dir}
    Take Desktop Screenshot
    ${item_count}    Count Items In Directory    ${dir}
    Should Be True    ${item_count} == 1
    ${prev}    Set Screenshot Directory    ${NONE}
    Should Be Equal    ${prev}    ${dir}
    [Teardown]    Set Screenshot Directory    ${NONE}

Only One Screenshot Is Generated With Nested Keywords
    [Setup]    Screenshot Setup
    Run Keyword And Expect Error    *    Dummy Keyword First Level
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


Dummy Keyword Final Level
  Click Item    unexisting-locator=whatever


Dummy Keyword Second Level
  Dummy Keyword Final Level

Dummy Keyword First Level
  Dummy Keyword Second Level
