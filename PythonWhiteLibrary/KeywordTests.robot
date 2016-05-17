*** Settings ***
Library    src/WhiteLibrary.py
Suite Setup	Launch App
Suite Teardown	Close App
Test Setup	Attach Main Window
Test Teardown	Clean App

*** Test Cases ***
Verify Labels
	Verify Label	lblA	Value 1
	Verify Label	lblB	Value 2
	Verify Label	lblResult	Result

Write to Textbox
    Input Text To Textbox	txtA    Ismo
    Input Text To Textbox  txtB	Aro

Verify Text
	Input Text To Textbox	txtA	Antti
	Verify Text In Textbox	txtA	Antti

Verify Operation Selections
	Select Combobox Value	op	+
	Verify + In Operators
	Select Combobox Value	op	-
	Verify - In Operators
	Select Combobox Value	op	*
	Verify * In Operators
	Select Combobox Value	op	/
	Verify / In Operators
	Select Combobox Value	op	%
	Verify % In Operators

Verify Button
	Verify Button	btnCalc	Calculate

Verify Menu
	Verify Menu	Help	Help
	Click Menu Button	Help
	Verify Menu	About	About

Open About And Verify Text
	Click Menu Button	Help
	Click Menu Button	About
	Select Modal Window	About
	Verify Label	65535	This is basic calculator application for testing white library
	Click Button	2
	Attach Window	UI Automation Test Window
	
Multiplication Calculation
	Calculate 5 * 2 Equals 10

Quotient Calculation
	Calculate 7 % 3 Equals 1

Plus Calculation
	Calculate 1 + 4 Equals 5

Minus Calculation
	Calculate 5 - 1 Equals 4

Division Calculation
	Calculate 5 / 2 Equals 2,5

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

*** Keywords ***
Launch App
	Set Logging Level	Warn
	Launch Application	..\\UIAutomationTest\\bin\\Debug\\UIAutomationTest.exe
	Attach Window	UI Automation Test Window

Close App
	Close Application

Attach Main Window
	Attach Window	UI Automation Test Window

Clean App
	Input Text To Textbox	txtA	${EMPTY}
	Input Text To Textbox	txtB	${EMPTY}
	Select Combobox Index	op	0
	Input Text To Textbox	tbResult	${EMPTY}

Verify ${operator} In Operators
	Verify Combobox Item	op	${operator}

Calculate ${num1} ${operator} ${num2} Equals ${result}
	Input Text To Textbox	txtA	${num1}
	Select Combobox Value	op	${operator}
	Input Text To Textbox	txtB	${num2}
	Click Button	btnCalc
	Verify Text In Textbox	tbResult	${result}