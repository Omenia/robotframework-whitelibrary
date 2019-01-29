*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Test Setup    Attach Main Window
Test Teardown    Clean Application
Resource          ..${/}resource.robot

*** Test Cases ***

Calculate Using Index Locators
    Input Text To Textbox    index=0    1
    Select Combobox Value    index=0    +
    Input Text To Textbox    index=2    2
    Click Button    btnCalc
    Verify Text In Textbox    index=3    3

Calculate Using ':' As Locator Delimiter
    Input Text To Textbox    text:Calc1    1
    Select Combobox Value    index:0    +
    Input Text To Textbox    index:2    2
    Click Button    id:btnCalc
    Verify Text In Textbox    index:3    3

Calculate Using Native Property Locators
    Input Text To Textbox    help_text=First addend    12
    Select Combobox Value    index=0    +
    Input Text To Textbox    help_text=Second addend    21
    Click Button    btnCalc
    Verify Text In Textbox    help_text=Sum    33

Click Button With = In Locator Value
    Input Text To Textbox    txtA    1
    Select Combobox Value    op    +
    Input Text To Textbox    txtB    2
    Click Button    text=Calculate (=)
    Verify Text In Textbox    tbResult    3

Get Single UI Item
    ${item}    Get Item    control_type=Button
    ${item_type}    Evaluate    type($item).__name__
    Should Be Equal    ${item_type}    ButtonProxy

List UI Items
    ${items}    Get Items    control_type=Button
    ${count}    Get Length    ${items}
    Should Be True    ${count} > 1

Unexisting Locator
    ${error}    Run Keyword And Expect Error    *    Click Item    unexisting-locator=whatever
    Should Contain    ${error}    'unexisting-locator' is not a valid locator prefix
