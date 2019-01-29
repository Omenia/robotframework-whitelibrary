*** Variables ***
${TEST APPLICATION}      ${EXECDIR}${/}UIAutomationTest${/}bin${/}Debug${/}UIAutomationTest.exe
${TEST APPLICATION NAME}    UIAutomationTest

*** Keywords ***

Launch Application For Test
    Set Log Level    Info
    Launch Application    ${TEST APPLICATION}
    Attach Window    UI Automation Test Window

Attach Main Window
    Attach Window    UI Automation Test Window

Clean Application
    Input Text To Textbox    txtA    ${EMPTY}
    Input Text To Textbox    txtB    ${EMPTY}
    Select Combobox Index    op    0
    Input Text To Textbox    tbResult    ${EMPTY}
    Click Button    progressResetBtn
    Select Radio Button    rb_peke
