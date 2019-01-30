*** Variables ***
${TEST APPLICATION}      ${EXECDIR}${/}UIAutomationTest${/}bin${/}Debug${/}UIAutomationTest.exe
${TEST APPLICATION NAME}    UIAutomationTest

${TEST WHITE APPLICATION}      ${EXECDIR}${/}WhiteStackTestApp${/}WpfTestApplication.exe
${TEST WHITE APPLICATION NAME}    MainWindow

*** Keywords ***

Launch Application For Test
    [Arguments]    ${args}=${EMPTY}
    Set Log Level    Info
    Launch Application    ${TEST APPLICATION}    ${args}
    Attach Window    UI Automation Test Window

Attach Main Window
    Attach Window    UI Automation Test Window

Launch White Application For Test
    Set Log Level    Info
    Launch Application    ${TEST WHITE APPLICATION}
    Attach Window    ${TEST WHITE APPLICATION NAME}

Attach White Main Window
    Attach Window    ${TEST WHITE APPLICATION NAME}


Clean Application
    Input Text To Textbox    txtA    ${EMPTY}
    Input Text To Textbox    txtB    ${EMPTY}
    Select Combobox Index    op    0
    Input Text To Textbox    tbResult    ${EMPTY}
    Click Button    progressResetBtn
    Select Radio Button    rb_peke
