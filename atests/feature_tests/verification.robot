*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Test Setup    Attach Main Window
Test Teardown    Clean Application
Resource    ../resource.robot

*** Test Cases ***
Failing Contains String Value With Non Ascii
    Run Keyword And Expect Error    Expected value åäö not found in Calculate (=)
    ...                             Button Text Should Contain    btnCalc    åäö

Failing Verify String Value With Non Ascii
    Run Keyword And Expect Error    Expected value åäö, but found Calculate (=)
    ...                             Button Text Should Be    btnCalc    åäö

Failing Verify Value With Non Ascii
    ${error}    Run Keyword And Expect Error    *        Verify Combobox Selection    op    åäö
    Should Contain    ${error}    Expected value åäö, but found