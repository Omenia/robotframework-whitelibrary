WhiteLibrary provides the means to test Windows GUI technologies with Robot Framework. WhiteLibrary wraps White test automation framework [\[1\]](#white).

# Technologies #
* Win32
* WinForms
* WPF (Windows Presentation Foundation)
* SWT (Java) platforms

# Stable version #
```
pip install --upgrade robotframework-whitelibrary
```
# Development version # 
```
pip install --upgrade --pre robotframework-whitelibrary
```
# Documentation #
Keyword [documentation](http://omenia.github.io/robotframework-whitelibrary/keywords.html) 

# Development Environment #
## Prerequisities ##
* Install [Visual Studio](https://visualstudio.microsoft.com/). It is needed for modifying and building the System Under Test (SUT). The SUT is a WPF application developed with C#.
* If you want to edit Python with Visual Studio, Python Tools are required. They're part of Visual Studio 2017 installer, see details about what to select during installation: https://github.com/Microsoft/PTVS
* Install [NuGet Command Line Interface (CLI)](https://docs.microsoft.com/en-us/nuget/tools/nuget-exe-cli-reference) to install White DLL packages.
* Install [Python](https://www.python.org/downloads/), if not already installed. Versions 2.7, 3.5 and 3.6 are supported at the moment.
* To install Robot Framework and Python for .NET, run
```
pip install robotframework pythonnet
```
## WhiteLibrary installation ##
* To install WhiteLibrary, in the root folder of the project run
```
local_install.cmd
```
* Open `UIAutomationTest\UIAutomationTest.sln` and build the solution in Visual Studio. This will create the SUT executable, `UIAutomationTest\bin\Debug\UIAutomationTest.exe`.

## Running tests with Robot Framework ##
* To execute the test suite against SUT, in the root folder of the project run
```
robot --outputdir output --exclude no_ci --loglevel DEBUG:INFO atests
```
* To execute a single test case called "Example Test Case", run
```
robot --outputdir output --exclude no_ci --loglevel DEBUG:INFO -t "Example Test Case" atests
```
* The test suite tagged with `no_ci` will run tests against the old (Win32) version of Windows calculator, and is typically excluded from test runs.

# References #

\[1\] <a name="white">https://github.com/TestStack/White</a>