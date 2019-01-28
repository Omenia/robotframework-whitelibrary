*** Variables ***
${TEST APPLICATION}      ${EXECDIR}${/}UIAutomationTest${/}bin${/}Debug${/}UIAutomationTest.exe
${EMPTY_STRING}    "${SPACE}${SPACE}${SPACE}"
${EMPTY_STRING2}    ${SPACE}${SPACE}${SPACE}

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

Launch Application With Empty Argument
    Launch App    ""
    Command Line Arguments Should Be    ${EMPTY}
    Close Application

Launch Application With Space Argument
    Launch App    ${EMPTY_STRING}
    Command Line Arguments Should Be    ${EMPTY_STRING2}
    Close Application

Launch Application With Single Argument
    Launch App    -single_argument
    Command Line Arguments Should Be    -single_argument
    Close Application

Launch Application With Single Argument With Space
    Launch App    "-single argument"
    Command Line Arguments Should Be    -single argument
    Close Application

Launch Application With Two Arguments
    Launch App    -argument1 -argument2
    Command Line Arguments Should Be    -argument1;-argument2
    Close Application

Launch Application With Two Arguments With Space
    Launch App    "-argument 1" "-argument 2"
    Command Line Arguments Should Be    -argument 1;-argument 2
    Close Application

Launch Application With Three Arguments
    Launch App    -argument1 -argument2 -argument3
    Command Line Arguments Should Be    -argument1;-argument2;-argument3
    Close Application

Launch Application With Three Arguments With Space
    Launch App    "-argument 1" "-argument 2" "-argument 3"
    Command Line Arguments Should Be    -argument 1;-argument 2;-argument 3
    Close Application

Launch Application With File Paths
    Launch App    test/test2.txt test\\test2.exe
    Command Line Arguments Should Be    test/test2.txt;test\\test2.exe
    Close Application

Launch Application With File Paths2
    Launch App    test${/}test2.txt test\\test2.exe
    Command Line Arguments Should Be    test\\test2.txt;test\\test2.exe
    Close Applicatio

Launch Application With Special Characters2
    Launch App    \# ? \\ / - _ \$
    Command Line Arguments Should Be    \#;?;\\;/;-;_;\$
    Close Application

*** Keywords ***
Launch App
    [Arguments]    ${args}=${EMPTY}
    Set Log Level    Info
    Launch Application    ${TEST APPLICATION}    ${args}
    Attach Window    UI Automation Test Window

Command Line Arguments Should Be
    [Arguments]    ${value}
    Verify Text In Textbox    command_line_arguments_value    ${value}
