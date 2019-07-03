*** Settings ***
Library    String
Library    WhiteLibrary

*** Variables ***
${TEST APPLICATION}      ${EXECDIR}${/}UIAutomationTest${/}bin${/}Debug${/}UIAutomationTest.exe
${TEST APPLICATION NAME}    UIAutomationTest
${INVALID TEST APPLICATION NAME}    UIAutomationTestThatDoesNotExist
${TEST APPLICATION WINDOW TITLE}    UI Automation Test Window
${TEST WHITE APPLICATION}      ${EXECDIR}${/}WhiteTestApp${/}WpfTestApplication.exe
${TEST WHITE APPLICATION NAME}    MainWindow


*** Keywords ***

Launch Application For Test
    [Arguments]    ${args}=${EMPTY}
    Set Log Level    Info
    Launch Application    ${TEST APPLICATION}    ${args}
    Attach Main Window

Attach Main Window
    Attach Window    ${TEST APPLICATION WINDOW TITLE}

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

Setup For Tab 2 Tests
    Attach Main Window
    Select Tab Page    tabControl    Tab2

Selction Indicator Should Be
    [Arguments]    ${node label}    ${status}
    [Documentation]    Note that node label is case sensitive
    ${status}=    Convert To Lowercase    ${status}
    Verify Label    selectionIndicatorLabel    ${node label} ${status}
