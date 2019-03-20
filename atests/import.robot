*** Settings ***
Library    OperatingSystem
Library    WhiteLibrary    ${SCREENSHOT_DIR}
Suite Setup    Remove Directory    ${SCREENSHOT_DIR}    recursive=True

*** Variables ***
${SCREENSHOT_DIR}    ${OUTPUT_DIR}/import-test/screenshots

*** Test Cases ***
Set Screenshot Directory At Library Import
    Run Keyword And Expect Error    *    Attach Application By Name    thisprocessdoesnotexistatleasthopefully
    Directory Should Exist    ${SCREENSHOT_DIR}
    ${item_count}    Count Items In Directory    ${SCREENSHOT_DIR}
    Should Be True    ${item_count} == 1
