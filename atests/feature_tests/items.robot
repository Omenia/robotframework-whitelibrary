*** Variables ***
${TEST APPLICATION}      ${EXECDIR}/UIAutomationTest/bin/Debug/UIAutomationTest.exe
${ARGUMENTS}    "generic_argument"
@{Tree node 1}    Tree node 1
@{Tree node 1.1}    Tree node 1    Tree node 1.1

*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Test Setup    Attach Main Window
Test Teardown    Clean Application
Resource    ../resource.robot

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
    Verify Combobox Selection    op    +
    Select Combobox Value    op    -
    Verify Combobox Selection    op    -
    Select Combobox Value    op    *
    Verify Combobox Selection    op    *
    Select Combobox Value    op    /
    Verify Combobox Selection    op    /
    Select Combobox Value    op    %
    Verify Combobox Selection    op    %
    Select Combobox Index    index=0    1    #multiplication
    Verify Combobox Selection    op    *

Combobox Contains
    Combobox Should Contain    op    +
    Combobox Should Contain    op    /
    Combobox Should Contain    op    %
    Run Keyword And Expect Error    ComboBox with locator 'op' did not contain '&'
    ...                             Combobox Should Contain    op    &
    Run Keyword And Expect Error    ComboBox with locator 'op' did not contain 'plus'
    ...                             Combobox Should Contain    op    plus
    Combobox Should Not Contain    op    &
    Combobox Should Not Contain    op    plus
    Run Keyword And Expect Error    ComboBox with locator 'op' should not have contained '+'
    ...                             Combobox Should Not Contain    op    +

Verify Button
    Button Text Should Contain    btnCalc    Calculate (=)

Verify Button Text Should Be
    Button Text Should Be   btnCalc    Calculate (=)
    Button Text Should Be   btnCalc    calculate (=)    case_sensitive=False
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Button Text Should Be   btnCalc    calculate (=)
    Should Contain    ${error_msg}    Expected value calculate (=), but found Calculate (=)

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
    Calculate 2 * 5 Equals 10

Calculate When First Number is Missing
    Calculate ${EMPTY} + 5 Equals ${EMPTY}

Calculate When First Number Is Alphabet
    Calculate a + 5 Equals ${EMPTY}

Verify Radio Buttons
    Verify Radio Button    rb_peke    ${TRUE}
    Select Radio Button    rb_ismo
    Verify Radio Button    rb_ismo    ${TRUE}

Verify Radio Buttons By Item Reference
    ${item}=    Get Item    rb_peke
    Select Radio Button    ${item}
    Verify Radio Button    rb_peke    ${TRUE}
    ${item}=    Get Item    rb_ismo
    Select Radio Button    ${item}
    Verify Radio Button    rb_ismo    ${TRUE}

Verify Get Radio Button State
    ${old_button_state}=    Get Radio Button State    rb_ismo
    Select Radio Button     rb_ismo
    ${new_button_state}=    Get Radio Button State    rb_ismo
    Should Not Be Equal     ${old_button_state}    ${new_button_state}

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

ListBox Contains
    Listbox Should Contain    list_box    Toni
    Run Keyword And Expect Error    ListBox with locator 'list_box' did not contain 'Donald Trump'
    ...                             Listbox Should Contain    list_box    Donald Trump
    Listbox Should Not Contain    list_box    Donald Trump
    Run Keyword And Expect Error    ListBox with locator 'list_box' should not have contained 'Toni'
    ...                             Listbox Should Not Contain    list_box    Toni

Click An Item
    Click Item    rb_ismo
    Verify Radio Button    rb_ismo    ${TRUE}

Switch Tab
    Select Tab Page    tabControl    Tab2
    Verify Label    selectionIndicatorLabel    nothing selected
    [Teardown]    Select Tab Page    tabControl    Tab1

Switch Tab With Index
    Select Tab Page By Index    tabControl    1
    Verify Label    selectionIndicatorLabel    nothing selected
    Select Tab Page By Index    tabControl    0
    Verify Label    eventIndicatorLabel    Double click me
    Select Tab Page By Index    tabControl    0
    Verify Label    eventIndicatorLabel    Double click me
    Select Tab Page By Index    tabControl    1
    Verify Label    selectionIndicatorLabel    nothing selected
    [Teardown]    Select Tab Page    tabControl    Tab1

Switch Tabs Using Tab List
    @{tabs}=    Get Tab Pages    tabControl
    ${tabs_len}=    Get Length    ${tabs}
    Should Be True    ${tabs_len} == 2
    FOR    ${tab}    IN    @{tabs}
        Select Tab Page    tabControl    ${tab.Name}
    END
    Verify Label    selectionIndicatorLabel    nothing selected
    Select Tab Page    tabControl    ${tabs[0].Name}
    Verify Label    eventIndicatorLabel    Double click me
    [Teardown]    Select Tab Page    tabControl    Tab1

Open Menu By Holding Keys
    Hold Special Key    ALT
    Press Keys    h
    Leave Special Key    ALT
    Verify Menu    text=About    About

Right Click An Item
    Right Click Item    text=Teppo
    Click Menu Button    text=Change Name
    Verify Label    65535    Not implemented yet.\nWhat's wrong with Teppo anyway?
    Click Button    text=OK

Double Click An Item
    Double Click Item    eventIndicatorLabel
    Verify Label    eventIndicatorLabel    Double-clicked 1 times

Double Click An Item With Item Reference
    ${item}=    Get Item    eventIndicatorLabel
    Double Click Item    ${item}
    Verify Label    eventIndicatorLabel    Double-clicked 2 times

Click An Item With Incorrect Item Reference
    ${item}=    Get Item    eventIndicatorLabel
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Click Button    ${item}
    Should Contain    ${error_msg}    Assumed that locator item is of type item_type

Click Button By Pressing Special Keys
    Input Text To Textbox    txtA    1
    Input Text To Textbox    txtB    2
    # Use combobox last to leave focus at the right place
    Select Combobox Value    op    +
    # Using keys to execute calculation
    Press Special Key    TAB
    Press Special Key    RETURN
    Verify Text In Textbox    tbResult    3

Write To Textbox By Pressing Keys
    Input Text To Textbox    txtA    ${EMPTY}
    Press Keys    Text and (123}!
    Verify Text In Textbox    txtA    Text and (123}!

Try To Press Unsupported Special Key
    Take Screenshots On Failure    false
    Run Keyword And Expect Error    AttributeError: Allowed special keys are*    Press Special Key    PANIC
    Take Screenshots On Failure    true

# Tab-2 tests #########################
Handle Tree Nodes
    [Setup]    Setup for Tab 2 Tests
    Select Tree Node    tree    @{Tree node 1}
    Selction Indicator Should Be     Tree node 1     Selected
    Expand Tree Node    tree    @{Tree node 1}
    Selction Indicator Should Be    Tree node 1     Expanded
    Double Click Tree Node    tree    @{Tree node 1}
    Selction Indicator Should Be    Tree node 1    Double-clicked
    Right Click Tree Node    tree    @{Tree node 1.1}
    Selction Indicator Should Be    Tree node 1.1    Right-clicked
    [Teardown]    Select Tab Page    tabControl    Tab1

Handle ToolStripButtons
    [Setup]    Setup for Tab 2 Tests
    Click Button    text=Toolstrip button 1
    Selction Indicator Should Be    Toolstrip button 1     Clicked
    Click Button    text=Toolstrip button 2
    Selction Indicator Should Be     Toolstrip button 2     Clicked
    Click Button    text=Toolstrip button 3
    Selction Indicator Should Be    Toolstrip button 3    Clicked
    [Teardown]    Select Tab Page    tabControl    Tab1

Popup menu with subitems
    [Setup]    Setup for Tab 2 Tests
    Right Click ListView Row By Index    list_view    2
    Click Item In Popup Menu    Delete
    Click Button    text=OK

    Right Click ListView Row    list_view    Title    Robinson Crusoe
    Click Item In Popup Menu    Have you read it?    Yes
    Click Button    text=OK
    [Teardown]    Select Tab Page    tabControl    Tab1

Button Is Enabled
    [Setup]    Setup for Tab 2 Tests
    Item Should Be Enabled    enabled_disabled
    ${status}    ${error_msg}    Run Keyword And Ignore Error	Item Should Be Disabled    enabled_disabled
    Should Contain    ${error_msg}    Expected disabled item but found enabled
    [Teardown]    Select Tab Page    tabControl    Tab1

Button Is Disabled
    [Setup]    Setup for Tab 2 Tests
    Click Button    enabled_disabled
    Item Should Be Disabled    enabled_disabled
    ${status}    ${error_msg}    Run Keyword And Ignore Error    Item Should Be Enabled    enabled_disabled
    Should Contain    ${error_msg}    Expected enabled item but found disabled
    [Teardown]    Select Tab Page    tabControl    Tab1

*** Keywords ***
Calculate ${num1} ${operator} ${num2} Equals ${result}
    Input Text To Textbox    txtA    ${num1}
    Select Combobox Value    op    ${operator}
    Input Text To Textbox    txtB    ${num2}
    Click Button    btnCalc
    Verify Text In Textbox    tbResult    ${result}
