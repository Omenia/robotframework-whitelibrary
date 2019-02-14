# Introduction

WhiteLibrary provides the means to automate Windows GUI technologies with Robot Framework. 
WhiteLibrary wraps the [White automation framework](https://github.com/TestStack/White).

Supported technologies include:
* Win32
* WinForms
* WPF (Windows Presentation Foundation)
* SWT (Java) platforms

# Installation

### Stable version
Installing the latest stable release:
```
pip install --upgrade robotframework-whitelibrary
```

[Release notes](https://github.com/Omenia/robotframework-whitelibrary/releases)

### Development version
Installing the version containing the latest updates in ``master``:
```
pip install --upgrade --pre robotframework-whitelibrary
```
# Documentation
* [Keyword documentation](http://omenia.github.io/robotframework-whitelibrary/keywords.html) 

# Development environment
This section contains instructions for developing WhiteLibrary.

### Prerequisities
* Install [NuGet Command Line Interface (CLI)](https://docs.microsoft.com/en-us/nuget/tools/nuget-exe-cli-reference) to install required DLL packages (TestStack.White and Castle.Core).
* Install [Python](https://www.python.org/downloads/), if not already installed. Versions 2.7, 3.5 and 3.6 are supported at the moment.
* To install Robot Framework and Python for .NET, run
```
pip install robotframework pythonnet
```
or alternatively you could use the provided requirements files (requirements.txt or requirements-dev.txt):
```
pip install -r requirements-dev.txt
```


* To make modifications to and build the test application (UIAutomationTest.exe), install [Visual Studio](https://visualstudio.microsoft.com/). The test application is a WPF application developed with C#.
* If you want to edit Python with Visual Studio, Python Tools are required. They're part of Visual Studio 2017 installer, see details about what to select during installation: https://github.com/Microsoft/PTVS
### WhiteLibrary installation
* To install WhiteLibrary from source, in the root folder of the project run
```
local_install.cmd
```

### Building the test application
Open `UIAutomationTest\UIAutomationTest.sln` in Visual Studio and build the solution in Visual Studio. 
This will create the executable used in the Robot test suite, `UIAutomationTest\bin\Debug\UIAutomationTest.exe`.

### Running tests with Robot Framework
* To execute the test suite against SUT, in the root folder of the project run
```
robot --outputdir output --exclude no_ci --loglevel DEBUG:INFO atests
```
* To execute a single test case called "Example Test Case", run
```
robot --outputdir output --exclude no_ci --loglevel DEBUG:INFO -t "Example Test Case" atests
```
* The test suite tagged with `no_ci` will run tests against the old (Win32) version of Windows calculator, and is typically excluded from test runs.

### Running Static Analysis
Project relies on flake8 and pylint for static analysis. In order to run those locally, one has to install them  (automatically installed if dependencies are installed via requirements-dev.txt):

```
pip install flake8 pylint
```

to run either one, go into to root of the project run execute analyzer, like this:

```
flake8
pylint src/
```

