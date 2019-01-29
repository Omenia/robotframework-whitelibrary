*** Variables ***
${EMPTY_STRING}    "${SPACE}${SPACE}${SPACE}"
${EMPTY_STRING2}    ${SPACE}${SPACE}${SPACE}

*** Settings ***
Library    WhiteLibrary
Library    Process
Library    OperatingSystem
Library    String
Resource    resource.robot

*** Test Cases ***
Launch Application With No Arguments
    Launch Application For Test
    Command Line Arguments Should Be    No command line args provided
    Close Application

Launch Application With Empty Argument
    Launch Application For Test    ""
    Command Line Arguments Should Be    ${EMPTY}
    Close Application

Launch Application With Space Argument
    Launch Application For Test    ${EMPTY_STRING}
    Command Line Arguments Should Be    ${EMPTY_STRING2}
    Close Application

Launch Application With Single Argument
    Launch Application For Test    -single_argument
    Command Line Arguments Should Be    -single_argument
    Close Application

Launch Application With Single Argument With Space
    Launch Application For Test    "-single argument"
    Command Line Arguments Should Be    -single argument
    Close Application

Launch Application With Two Arguments
    Launch Application For Test    -argument1 -argument2
    Command Line Arguments Should Be    -argument1;-argument2
    Close Application

Launch Application With Two Arguments With Space
    Launch Application For Test    "-argument 1" "-argument 2"
    Command Line Arguments Should Be    -argument 1;-argument 2
    Close Application

Launch Application With Three Arguments
    Launch Application For Test    -argument1 -argument2 -argument3
    Command Line Arguments Should Be    -argument1;-argument2;-argument3
    Close Application

Launch Application With Three Arguments With Space
    Launch Application For Test    "-argument 1" "-argument 2" "-argument 3"
    Command Line Arguments Should Be    -argument 1;-argument 2;-argument 3
    Close Application

Launch Application With File Paths
    Launch Application For Test    test/test2.txt test\\test2.exe
    Command Line Arguments Should Be    test/test2.txt;test\\test2.exe
    Close Application

Launch Application With File Paths2
    Launch Application For Test    test${/}test2.txt test\\test2.exe
    Command Line Arguments Should Be    test\\test2.txt;test\\test2.exe
    Close Application

Launch Application With Special Characters2
    Launch Application For Test    \# ? \\ / - _ \$
    Command Line Arguments Should Be    \#;?;\\;/;-;_;\$
    Close Application

*** Keywords ***
Command Line Arguments Should Be
    [Arguments]    ${value}
    Verify Text In Textbox    command_line_arguments_value    ${value}
