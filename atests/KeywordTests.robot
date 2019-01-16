*** Variables ***
${TEST APPLICATION}      ${EXECDIR}${/}UIAutomationTest${/}bin${/}Debug${/}UIAutomationTest.exe

*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Suite Setup    Launch App
Suite Teardown    Close App
Test Setup    Attach Main Window
Test Teardown    Clean App

*** Test Cases ***
Verify Labels
    Verify Label    lblA    Value 1
    Verify Label    lblB    Value 2
    Verify Label    lblResult    Result

Verify Get Text From Label
    ${txt}=   Get Text From Label   lblResult
    Should Be Equal As Strings    ${txt}    Result

Write to Textbox
    Input Text To Textbox    txtA    Ismo
    Input Text To Textbox    txtB    Aro
    Input Text To Textbox    text=Calc1    Ismo!
    Input Text To Textbox    passwordBox    viisi

Verify Text
    Input Text To Textbox     txtA    Antti
    Verify Text In Textbox    txtA    Antti

Verify Get Text
    ${input_txt}=    Set Variable    Kilroy Was Here!
    Input Text To Textbox     txtA    ${input_txt}
    ${output_txt}=   Get Text From Textbox     txtA
    Should Be Equal As Strings    ${output_txt}    ${input_txt}

Verify Operation Selections
    Select Combobox Value    op    +
    Verify + In Operators
    Select Combobox Value    op    -
    Verify - In Operators
    Select Combobox Value    op    *
    Verify * In Operators
    Select Combobox Value    op    /
    Verify / In Operators
    Select Combobox Value    op    %
    Verify % In Operators
    Select Combobox Index    index=0    1    #multiplication
    Verify * In Operators

Verify Button
    Verify Button    btnCalc    Calculate (=)

Verify Button Text Should Be
    Button Text Should Be   btnCalc    Calculate (=)
    Button Text Should Be   btnCalc    calculate (=)    case_sensitive=False

Verify Button Text Should Contain
    Button Text Should Contain   btnCalc    alcu    case_sensitive=True
    Button Text Should Contain   btnCalc    ULaTE   case_sensitive=False

Verify Menu
    Verify Menu          text=Help    Help
    Click Menu Button    text=Help
    Verify Menu          text=About    About

Open About And Verify Text
    Click Menu Button    text=Help
    Click Menu Button    text=About
    Select Modal Window    About
    Verify Label    65535    This is basic calculator application for testing white library
    Click Button    2
    Attach Window    UI Automation Test Window

Multiplication Calculation
    Calculate 5 * 2 Equals 10

Quotient Calculation
    [Tags]    no_ci
    Calculate 7 % 3 Equals 1

Plus Calculation
    [Tags]    no_ci
    Calculate 1 + 4 Equals 5

Minus Calculation
    [Tags]    no_ci
    Calculate 5 - 1 Equals 4

Division Calculation
    [Tags]   no_ci
    Calculate 6 / 2 Equals 3

Calculate When First Number is Missing
    Calculate 5 + ${EMPTY} Equals ${EMPTY}

Calculate When Second Number is Missing
    [Tags]    no_ci
    Calculate ${EMPTY} + 5 Equals ${EMPTY}

Calculate When First Number Is Alphabet
    Calculate a + 5 Equals ${EMPTY}

Calculate When Second Number Is Alphabet
    [Tags]    no_ci
    Calculate 1 + a Equals ${EMPTY}

Verify Radio Buttons
    Verify Radio Button    rb_peke    ${TRUE}
    Select Radio Button    rb_ismo
    Verify Radio Button    rb_ismo    ${TRUE}

Verify Get Radio Button State
    ${old_button_state}=    Get Radio Button State   rb_ismo
    Select Radio Button     rb_ismo
    ${new_button_state}=    Get Radio Button State   rb_ismo
    Should Not Be Equal     ${old_button_state}   ${new_button_state}

Verify Slider
    Verify Slider Value    sladdu    0
    Set Slider Value       sladdu    4.20
    Verify Slider Value    sladdu    4.20

Verify Get Slider Value
    Set Slider Value       sladdu    4.2
    ${slider_value}=  Get Slider Value    sladdu
    Should Be Equal     ${slider_value}   ${4.2}

Verify Progressbar
    Verify Progressbar Value    proggis    4
    Click Button    progressBtn
    Verify Progressbar Value    proggis    24

Verify Get Progressbar Value
    ${progressbar_value}=   Get Progressbar Value    proggis
    Should Be Equal   ${progressbar_value}  ${4.0}
    Click Button    progressBtn
    ${progressbar_value}=   Get Progressbar Value    proggis
    Should Be Equal   ${progressbar_value}  ${24}

Verify Check Boxes
    Verify Check Box    cb_omena    ${FALSE}
    Toggle Check Box    cb_omena
    Verify Check Box    cb_omena    ${TRUE}
    Verify Check Box    cb_omen    ${FALSE}
    Verify Check Box    cb_omenia    ${FALSE}

Verify Get Check Box State
    ${old_check_box_state}=   Get Check Box State   cb_omena
    Toggle Check Box    cb_omena
    ${new_check_box_state}=   Get Check Box State   cb_omena
    Should Not Be Equal     ${old_check_box_state}   ${new_check_box_state}

Verify ListBox
    Select Listbox Index    list_box    1
    Listbox Selection Should Be    list_box    Toni
    Select Listbox Value    list_box    Teppo
    Listbox Selection Should Be    list_box    Teppo
    Run Keyword And Expect Error    Expected listbox selection to be Yamis, was Teppo
    ...                             Listbox Selection Should Be    list_box    Yamis

Click An Item
    Click Item    rb_ismo
    Verify Radio Button    rb_ismo    ${TRUE}

Calculate Using Index Locators
    Input Text To Textbox    index=0    1
    Select Combobox Value    index=0    +
    Input Text To Textbox    index=2    2
    Click Button    btnCalc
    Verify Text In Textbox    index=3    3

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

Unexisting Locator
    ${error}    Run Keyword And Expect Error    *    Click Item    unexisting-locator=whatever
    Should Contain    ${error}    'unexisting-locator' is not a valid locator prefix

Take screenshots
    [Setup]    Screenshot Setup
    Take Desktop Screenshot
    New Screenshot Should Be Created
    Take Desktop Screenshot
    New Screenshot Should Be Created

Take screenshot on failure
    [Setup]    Screenshot Setup
    Run Keyword And Expect Error    *    Should Be True    ${FALSE}
    New Screenshot Should Be Created

Disable and enable screenshots on failure
    [Setup]    Screenshot Setup
    Take Screenshots On Failure    false
    Run Keyword And Expect Error    *    Should Be True    ${FALSE}
    New Screenshot Should Not Be Created
    Take Screenshots On Failure    ${True}
    Run Keyword And Expect Error    *    Should Be True    ${FALSE}
    New Screenshot Should Be Created

Switch Tab
    Select Tab Page    tabControl    Tab2
    Verify Label    selectionIndicatorLabel    nothing selected
    [Teardown]    Select Tab Page    tabControl    Tab1

Open Menu By Holding Keys
    Hold Special Key    ALT
    Press Keys    h
    Leave Special Key    ALT
    Verify Menu    text=About    About

Handle Tree Nodes
    [Setup]    Setup for Tab 2 Tests
    Select Tree Node    tree    @{Tree node 1}
    Tree node 1 Should Be Selected
    Expand Tree Node    tree    @{Tree node 1}
    Tree node 1 Should Be Expanded
    Double Click Tree Node    tree    @{Tree node 1}
    Tree node 1 Should Be Double-clicked
    Right Click Tree Node    tree    @{Tree node 1.1}
    Tree node 1.1 Should Be Right-clicked
    [Teardown]    Select Tab Page    tabControl    Tab1

Handle ToolStripButtons
    [Setup]    Setup for Tab 2 Tests
    Click Button    text=Toolstrip button 1
    Toolstrip button 1 Should Be Clicked
    Click Button    text=Toolstrip button 2
    Toolstrip button 2 Should Be Clicked
    Click Button    text=Toolstrip button 3
    Toolstrip button 3 Should Be Clicked
    [Teardown]    Select Tab Page    tabControl    Tab1

Handle ListView
    [Setup]    Setup for Tab 2 Tests
    Select ListView Row By Index    list_view    1
    Bible Should Be Selected
    Select ListView Row By Index    list_view    2
    The Art of Computer Programming Should Be Selected

    Repeat Keyword    2    Right Click Listview Cell    list_view2    Title    1
    Bible Should Be Right Clicked
    Repeat Keyword    2    Right Click Listview Cell    list_view2    Author    0
    Daniel Defoe Should Be Right Clicked
    [Teardown]    Select Tab Page    tabControl    Tab1

Handle Delayed Actions
    [Tags]    under_test
    [Setup]    Setup for Tab 2 Tests
    Set White Busy Timeout    5
    Click Button    text=Fast alert
    Fast Alert Should Be Right Occurred
    Click Button    text=Slow alert
    Slow Alert Should Be Right Occurred
    [Teardown]    Select Tab Page    tabControl    Tab1

Right Click An Item
    Right Click Item    text=Teppo
    Click Menu Button    text=Change Name
    Verify Label    65535    Not implemented yet.\nWhat's wrong with Teppo anyway?
    Click Button    text=OK

Double Click An Item
    Double Click Item    eventIndicatorLabel
    Verify Label    eventIndicatorLabel    Double-clicked 1 times

Click Button By Pressing Special Keys
    Input 1 + 2 To Calculator
    Use Special Keys To Press Calculate Button
    Calculation Result Should Be    3

Try To Press Unsupported Special Key
    [Setup]    Run Keywords    Attach Main Window    AND    Take Screenshots On Failure    false
    Run Keyword And Expect Error    AttributeError: Allowed special keys are*    Press Special Key    PANIC
    [Teardown]    Run Keywords    Take Screenshots On Failure    true    AND    Clean App

Write To Textbox By Pressing Keys
    Activate Textbox    txtA
    Press Keys    Text and (123}!
    Verify Text In Textbox    txtA    Text and (123}!

List UI Items
    ${items}    Get Items    control_type=Button
    ${count}    Get Length    ${items}
    Should Be True    ${count} > 1

*** Keywords ***
Launch App
    Set Log Level    Info
    Launch Application    ${TEST APPLICATION}
    Attach Window    UI Automation Test Window

Close App
    Close Application

Attach Main Window
    Attach Window    UI Automation Test Window

Clean App
    Input Text To Textbox    txtA    ${EMPTY}
    Input Text To Textbox    txtB    ${EMPTY}
    Select Combobox Index    op    0
    Input Text To Textbox    tbResult    ${EMPTY}
    Click Button    progressResetBtn
    Select Radio Button    rb_peke

Verify ${operator} In Operators
    Verify Combobox Item    op    ${operator}

Calculate ${num1} ${operator} ${num2} Equals ${result}
    Input Text To Textbox    txtA    ${num1}
    Select Combobox Value    op    ${operator}
    Input Text To Textbox    txtB    ${num2}
    Click Button    btnCalc
    Verify Text In Textbox    tbResult    ${result}

Activate Textbox
    [Documentation]    Note that this empties the textbox
    [Arguments]    ${locator}
    Input Text To Textbox    ${locator}    ${EMPTY}

Input ${num1} ${operator} ${num2} To Calculator
    Input Text To Textbox    txtA    ${num1}
    Input Text To Textbox    txtB    ${num2}
    # Use combobox last to leave focus at the right place
    Select Combobox Value    op    ${operator}

Use Special Keys To Press Calculate Button
    Press Special Key    TAB
    Press Special Key    RETURN

Calculation Result Should Be
    [Arguments]    ${result}
    Verify Text In Textbox    tbResult    ${result}

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

Setup For Tab 2 Tests
    Attach Main Window
    Select Tab Page    tabControl    Tab2
    @{Tree node 1} =    Create List    Tree node 1
    @{Tree node 1.1} =    Create List    Tree node 1    Tree node 1.1
    Set Test Variable    @{Tree node 1}
    Set Test Variable    @{Tree node 1.1}

${node label} Should Be ${status}
    [Documentation]    Note that node label is case sensitive
    ${status}=    Convert To Lowercase    ${status}
    Verify Label    selectionIndicatorLabel    ${node label} ${status}
