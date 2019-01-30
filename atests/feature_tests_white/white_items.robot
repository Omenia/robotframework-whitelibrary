*** Variables ***

*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Test Setup    Attach White Main Window
Resource          ..${/}resource.robot

*** Test Cases ***
DragDrop ScenarioS
    Click Button    DragDropScenario
    Attach Window    DragAndDropTestWindow
    Drag And Drop    TextBox    Button
    Verify Label    DragDropResults    TextBoxDraggedOntoButton
