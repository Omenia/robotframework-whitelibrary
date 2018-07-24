<p> <b>This library is still very much under construction.<p> <b>
<p>WhiteLibrary will give a way to test Windows UI technologies with Robot Framework. WhiteLibrary wraps White test automation framework [1] </p>
<p><b>Techonologies</b></p>
<ul>
<li>Win32</li>
<li>WinForms</li>
<li>WPF (Windows Presentation Foundation)</li>
<li>Silverlight</li>
<li>SWT (Java) platforms</li>
</ul>
<p><b>Development Environment</b></p>
<ul>
<li>Install Visual Studio: https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx</br>
Python Tools are required but they're now part of Visual Studio 2017 installer, see details what to select when installing Visual Studio: https://github.com/Microsoft/PTVS
</li>
<li>Clone project from Github</li>
<ul>
<li><del>Howto: http://rickrainey.com/2013/07/27/visual-studio-and-gitub-the-basics-of-working-with-existing-repositories-2/</del> (currently unavailable)</br>
Howto: https://docs.microsoft.com/en-us/vsts/git/gitquickstart?view=vsts&tabs=visual-studio
</li>
<li>Repository https://github.com/Omenia/robotframework-whitelibrary</li>
</ul>
</ul>
<p><b>Running tests with Robot</b></p>
<ul>
<li>Install Python</li>
<li>Install Robot Framework and Python for .NET: pip install robotframework pythonnet</li>
<li>Inside the solution execute tests from folder: \PythonWhiteLibrary execute: "run_tests.cmd". Single test cases can be run with command "run_tests.cmd -t "Test case name""</li>
</ul>
[1] https://github.com/TestStack/White
