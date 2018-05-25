*** Settings ***
# install oldcalcwin10 first!
Force Tags     no_ci
Library    WhiteLibrary
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
	Calculate 135 91 132 Equals 2,5

Multiplication Calculation
	Calculate 132 92 133 Equals 6

Verify Different Calculator Types
	Click Menu Button	text=View
	Click Menu Button	text=Scientific
	Click Menu Button	text=View
	Click Menu Button	text=Programmer
	Click Menu Button	text=View
	Click Menu Button	text=Statistics
	Click Menu Button	text=View
	Click Menu Button	text=Unit conversion
	Click Menu Button	text=View
	Click Menu Button	text=Date calculation
	Click Menu Button	text=View
	Click Menu Button	text=Standard
	Click Menu Button	text=View
	Click Menu Button	text=Basic

Verify About Calculator Is Found
	Click Menu Button	text=Help
	Click Menu Button	text=About Calculator
	Select Modal Window	About Calculator
	Verify Label	13568	Microsoft Windows
	Click Button	1
	Attach Window	Calculator

*** Keywords ***
Launch App
	Set Logging Level	Warn
	LOG    Install calculator for Windows 7/8: http://winaero.com/download.php?view.1795
	Launch Application	 C:\\Windows\\System32\\calc1.exe
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
