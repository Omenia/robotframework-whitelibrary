*** Settings ***
Library    WhiteLibrary
Test Teardown    Clean Application
Resource    ../resource.robot

*** Test Cases ***
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

Combobox Selected Text
    Select Combobox Value    op    -
    ${selected_value}    Get Combobox Selected Text    op
    Should Be Equal    ${selected_value}    -

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

Try Select In Disabled Combobox
    Run Keyword And Expect Error    Could not select item 'can't select this' because the ComboBox was disabled
    ...                             Select Combobox Value    disabled_combo    can't select this
    Run Keyword And Expect Error    Could not select item at 3 because the ComboBox was disabled
    ...                             Select Combobox Index    disabled_combo    3

Listbox Selected Text
    Select Listbox Value    list_box    Teppo
    ${selected_value}    Get Listbox Selected Text    list_box
    Should Be Equal    ${selected_value}    Teppo

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
