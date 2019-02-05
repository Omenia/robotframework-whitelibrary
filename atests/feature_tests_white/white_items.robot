*** Variables ***

*** Settings ***
Library    OperatingSystem
Library    String
Library    WhiteLibrary
Resource          ..${/}resource.robot

*** Test Cases ***
DragDrop Scenarios
    Click Button    DragDropScenario
    Attach Window    DragAndDropTestWindow
    Drag And Drop    TextBox    Button
    Verify Label    DragDropResults    TextBoxDraggedOntoButton
