*** Variables ***
${EMPTY_STRING}    "${SPACE}${SPACE}${SPACE}"
${EMPTY_STRING2}    ${SPACE}${SPACE}${SPACE}

*** Settings ***
Library    WhiteLibrary
Library    Process
Library    OperatingSystem
Library    String
Resource    resource.robot

Test Template     Launch Application With Arguments

*** Test Cases ***              Arguments            Expected result
No Arguments                    ${EMPTY}             No command line args provided
Empty String	                ""                   ${EMPTY}
Space                           ${EMPTY_STRING}      ${EMPTY_STRING2}
Single Argument                 -single_argument     -single_argument
Single Argument With Space      "-single argument"   -single argument
Two Arguments                   -argument1 -argument2    -argument1;-argument2
Two Arguments With Space        "-argument 1" "-argument 2"    -argument 1;-argument 2
Three Arguments                 -argument1 -argument2 -argument3    -argument1;-argument2;-argument3
Three Arguments With Space      "-argument 1" "-argument 2" "-argument 3"    -argument 1;-argument 2;-argument 3
File Paths                      test/test2.txt test\\test2.exe    test/test2.txt;test\\test2.exe
File Paths2                     test${/}test2.txt test\\test2.exe    test\\test2.txt;test\\test2.exe
Special Characters              \# ? \\ / - _ \$    \#;?;\\;/;-;_;\$


*** Keywords ***
Launch Application With Arguments
    [Arguments]    ${arguments}    ${result}
    Launch Application For Test    ${arguments}
    Command Line Arguments Should Be    ${result}
    Close Application

Command Line Arguments Should Be
    [Arguments]    ${value}
    Verify Text In Textbox    command_line_arguments_value    ${value}
