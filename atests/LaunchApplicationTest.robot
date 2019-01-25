*** Variables ***
${TEST APPLICATION}      ${EXECDIR}${/}UIAutomationTest${/}bin${/}Debug${/}UIAutomationTest.exe

*** Settings ***
Library    WhiteLibrary
Library    Process
Library    OperatingSystem
Library    String

*** Test Cases ***
Launch Application With No Arguments
    Launch App
    Command Line Arguments Should Be    No command line args provided
    Close Application

Launch Application With Single Argument
    Launch App    single_argument
    Command Line Arguments Should Be    single_argument
    Close Application

Launch Application With Two Arguments
    Launch App    argument1    argument2
    Command Line Arguments Should Be    argument1;argument2
    Close Application

Launch Application With Three Arguments
    Launch App    argument1    argument2    argument3
    Command Line Arguments Should Be    argument1;argument2;argument3
    Close Application

*** Keywords ***
Launch App
    [Arguments]    @{args}
    Set Log Level    Info
    ${count}    Get Length    @{args}
    Log    Count was ${count}
    Launch Application    ${TEST APPLICATION}    @{args}
    Attach Window    UI Automation Test Window

Command Line Arguments Should Be
    [Arguments]    ${value}
    Verify Text In Textbox    command_line_arguments_value    ${value}
