*** Settings ***
Library    src/WhiteLibrary.py
Suite Setup	Launch App
Suite Teardown	Close App
Test Teardown	Clean App

*** Test Cases ***
Click Button
	Click Button	131

Erase Selected Value
	Click Button	135
	Click Button	83
	Verify Label	150	0

Plus Calculation
	Calculate 131 93 136 Equals 7

Minus Calculation
	Calculate 139 94 136 Equals 3

Division Calculation
	Calculate 135 91 132 Equals 2.5

Multiplication Calculation
	Calculate 132 92 133 Equals 6

Verify Different Calculator Types
	Click Menu Button	View
	Click Menu Button	Scientific
	Click Menu Button	View
	Click Menu Button	Programmer
	Click Menu Button	View
	Click Menu Button	Statistics
	Click Menu Button	View
	Click Menu Button	Unit conversion
	Click Menu Button	View
	Click Menu Button	Date calculation
	Click Menu Button	View
	Click Menu Button	Standard
	Click Menu Button	View
	Click Menu Button	Basic

Verify About Calculator Is Found
	Click Menu Button	Help
	Click Menu Button	About Calculator
	Select Modal Window	About Calculator
	Verify Label	13568	Microsoft Windows
	Click Button	1
	Attach Window	Calculator

*** Keywords ***
Launch App
	Set Logging Level	Warn
	Launch Application	C:\\Windows\\System32\\calc.exe
	Attach Window	Calculator

Close App
	Close Application

Clean App
	Click Button	82 

Calculate ${num1} ${op} ${num2} Equals ${result}
	Click Button	${num1}
	Click Button	${op}
	Click Button	${num2}
	Click Button	121
	Verify Label	150	${result}