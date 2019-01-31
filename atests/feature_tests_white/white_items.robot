*** Variables ***

*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Test Setup    Mouse Event Test Setup
Test Teardown    Close Window
Resource          ..${/}resource.robot

*** Test Cases ***
DragDrop Scenarios
    Click Button    DragDropScenario
    Attach Window    DragAndDropTestWindow
    Drag And Drop    TextBox    Button
    Verify Label    DragDropResults    TextBoxDraggedOntoButton
    Sleep    5

Drag Splitter Rightwards
    [Tags]    not_working
    Click Button    OpenHorizontalSplitterButton
    Attach Window    HorizontalGridSplitter
    Sleep    5
    Drag Horizontally    Splitter    100
    Sleep    5
    Drag Horizontally    Splitter    50
    Sleep    5

Drag Splitter Leftwards
    [Tags]    not_working
    Click Button    OpenHorizontalSplitterButton
    Attach Window    HorizontalGridSplitter
    Drag Horizontally    Splitter    -100
    Sleep    5


*** Keywords ***
Mouse Event Test Setup
    Attach White Main Window

Mouse Event Test Teardown
    Close Window
    Close Application
