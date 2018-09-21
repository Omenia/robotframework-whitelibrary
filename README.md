This library is still very much under construction.
WhiteLibrary will give a way to test Windows UI technologies with Robot Framework. WhiteLibrary wraps White test automation framework [1]

# Pre-release version available # 
```
pip install --pre robotframework-whitelibrary
```
# Techonologies #
* Win32
* WinForms
* WPF (Windows Presentation Foundation)
* SWT (Java) platforms

# Development Environment #
* Install Visual Studio: https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx
* Python Tools are required but they're now part of Visual Studio 2017 installer, see details what to select when installing Visual Studio: https://github.com/Microsoft/PTVS

# Running tests with Robot #
* Install Python
* Install Robot Framework and Python for .NET
```
pip install robotframework pythonnet
```
* Inside the solution execute tests from folder: \PythonWhiteLibrary execute: "run_tests.cmd". Single test cases can be run with command 
```
run_tests.cmd -t "Test case name"
```
[1] https://github.com/TestStack/White

