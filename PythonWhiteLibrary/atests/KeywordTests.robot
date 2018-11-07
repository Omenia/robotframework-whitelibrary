*** Variables ***
${TEST APPLICATION}      UIAutomationTest${/}bin${/}Debug${/}app.publish${/}UIAutomationTest.exe


*** Settings ***
Library    OperatingSystem
Library    ../src/WhiteLibrary.py
#Library    WhiteLibrary    dev=${TRUE}
Suite Setup    Launch App
Suite Teardown    Close App
Test Setup    Attach Main Window
Test Teardown    Clean App


*** Test Cases ***
Verify Labels
    Verify Label    lblA    Value 1
    Verify Label    lblB    Value 2
    Verify Label    lblResult    Result

Write to Textbox
    Input Text To Textbox    txtA    Ismo
    Input Text To Textbox    txtB    Aro
    Input Text To Textbox   passwordBox    viisi

Verify Text
    Input Text To Textbox     txtA    Antti
    Verify Text In Textbox    txtA    Antti

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

Verify Button
    Verify Button    btnCalc    Calculate

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
    Calculate 7 % 3 Equals 1

Plus Calculation
    Calculate 1 + 4 Equals 5

Minus Calculation
    Calculate 5 - 1 Equals 4

Division Calculation
    [Tags]   unstable
    Calculate 6 / 2 Equals 3

Calculate When First Number is Missing
    Calculate 5 + ${EMPTY} Equals ${EMPTY}

Calculate When Second Number is Missing
    Calculate ${EMPTY} + 5 Equals ${EMPTY}

Calculate When First Number Is Alphabet
    Calculate a + 5 Equals ${EMPTY}

Calculate When Second Number Is Alphabet
    Calculate 1 + a Equals ${EMPTY}

Verify Radio Buttons
    Verify Radio Button    rb_peke    ${TRUE}
    Select Radio Button    rb_ismo
    Verify Radio Button    rb_ismo    ${TRUE}

Verify Slider
    Verify Slider Value    sladdu    0
    Set Slider Value       sladdu    4.20
    Verify Slider Value    sladdu    4.20

Verify Progressbar
    Verify Progressbar Value    proggis    78

Verify Check Boxes
    Verify Check Box    cb_omena    ${FALSE}
    Toggle Check Box    cb_omena
    Verify Check Box    cb_omena    ${TRUE}
    Verify Check Box    cb_omen    ${FALSE}
    Verify Check Box    cb_omenia    ${FALSE}

#Verify ListBox
    #Select Listbox Value    op    box_item_teppo

Calculate Using Index Locators
    Input Text To Textbox    index=0    1
    Select Combobox Value    index=0    +
    Input Text To Textbox    index=2    2
    Click Button    btnCalc
    Verify Text In Textbox    index=3    3

Take screenshots
    ${count_1}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Take Desktop Screenshot
    ${count_2}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Should Be True    ${count_2} > ${count_1}
    Take Desktop Screenshot
    ${count_3}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Should Be True    ${count_3} > ${count_2}

Take screenshot on failure
    ${count_1}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Run Keyword And Expect Error    *    Verify Text In Textbox    index=3    3
    ${count_2}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Should Be True    ${count_2} > ${count_1}

Disable and enable screenshots on failure
    ${count_1}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Take Screenshots On Failure    false
    Run Keyword And Expect Error    *    Verify Text In Textbox    index=3    3
    ${count_2}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Should Be Equal    ${count_2}    ${count_1}
    Take Screenshots On Failure    ${True}
    Run Keyword And Expect Error    *    Verify Text In Textbox    index=3    3
    ${count_3}=    Count Files In Directory    ${OUTPUTDIR}    whitelib_screenshot_*.png
    Should Be True    ${count_3} > ${count_2}

Switch Tab
    Select Tab Page    tabControl    Tab2
    [Teardown]    Select Tab Page    tabControl    Tab1

Handle Tree Nodes
    [Setup]    Run Keywords    Attach Main Window    AND    Select Tab Page    tabControl    Tab2
    @{node 1} =    Create List    Tree node 1
    @{node 2} =    Create List    Tree node 1    Tree node 1.1
    Select Tree Node    tree    @{node 1}
    Verify Label    selectionIndicatorLabel    Tree node 1 selected
    Expand Tree Node    tree    @{node 1}
    Verify Label    selectionIndicatorLabel    Tree node 1 expanded
    Double Click Tree Node    tree    @{node 1}
    Verify Label    selectionIndicatorLabel    Tree node 1 double-clicked
    Right Click Tree Node    tree    @{node 2}
    Verify Label    selectionIndicatorLabel    Tree node 1.1 right-clicked
    [Teardown]    Select Tab Page    tabControl    Tab1

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

Verify ${operator} In Operators
    Verify Combobox Item    op    ${operator}

Calculate ${num1} ${operator} ${num2} Equals ${result}
    Input Text To Textbox    txtA    ${num1}
    Select Combobox Value    op    ${operator}
    Input Text To Textbox    txtB    ${num2}
    Click Button    btnCalc
    Verify Text In Textbox    tbResult    ${result}
