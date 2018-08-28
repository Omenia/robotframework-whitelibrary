<html>
<head>
</head>
<body>
<p><b>This library is still very much under construction.</b></p>

<p><b><b>WhiteLibrary will give a way to test Windows UI technologies with Robot Framework. WhiteLibrary wraps White test automation framework [1] </b></b></p>

<p><b><b><b>Techonologies</b></b></b></p>

<ul>
	<li><b>Win32</b></li>
	<li><b>WinForms</b></li>
	<li><b>WPF (Windows Presentation Foundation)</b></li>
	<li><b>Silverlight</b></li>
	<li><b>SWT (Java) platforms</b></li>
</ul>

<p><b>Development Environment</b></p>

<ul>
	<li><b>Install Visual Studio: https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx<br />
	Python Tools are required but they&#39;re now part of Visual Studio 2017 installer, see details what to select when installing Visual Studio: <a href="https://github.com/Microsoft/PTVS">https://github.com/Microsoft/PTVS</a></b></li>
	<li><b>Clone project from Github</b>
	<ul>
		<li><b>Howto: http://rickrainey.com/2013/07/27/visual-studio-and-gitub-the-basics-of-working-with-existing-repositories-2/</del> (currently unavailable)<br />
		Howto: https://docs.microsoft.com/en-us/vsts/git/gitquickstart?view=vsts&amp;tabs=visual-studio </b></li>
		<li><b>Repository https://github.com/Omenia/robotframework-whitelibrary</b></li>
	</ul>
	</li>
	<li>Open solution file using Visual studio.
	<ul>
		<li>RobotFrameworkWhiteLibrary.sln</li>
	</ul>
	</li>
	<li>Build the project to obtain all the related libraries
	<ul>
		<li>In VS Solution explorer panel -&gt; right click the solution file -&gt; Build</li>
		<li>Result shoild show success and also should download proper libraries/binaries under 
		<ul>
			<li>UIAutomationTest\bin</li>
			<li>WhiteLibrary\bin</li>
		</ul>
		</li>
	</ul>
	</li>
</ul>

<p><b>Running tests with Robot</b></p>

<ul>
	<li><b>Install Python27 (as of this writing the tests wont run using Python37)</b>

	<ul>
		<li>If you have installed multiple Python versions you need to verify that Python27 is defined in the Windows Path environment variable to point to python.exe</li>
		<li>If you do not want to use previous definition you can run the tests command line by manually selecting the python exexutable</li>
	</ul>
	</li>
	<li><b>Install Robot Framework and Python for .NET: pip install robotframework pythonnet</b>
	<ul>
		<li>Install these for Python27</li>
	</ul>
	</li>
	<li>If you use Windows 10 please install the old calculator application. The tests use calculator as a system under test and require the old calculation application.
	<ul>
		<li><strong>Instructions: </strong>https://windowsreport.com/download-old-calculator-windows-10/</li>
	</ul>
	</li>
	<li><b><b>Inside the solution execute tests from folder: \PythonWhiteLibrary execute: run_tests.cmd. Single test cases can be run with command run_tests.cmd -t Test case name</b></b>
	<ul>
		<li>If you need to manually select the python executable you can also run:<br />
		python -m robot --outputdir [your log folder] --noncritical unstable -P PythonWhiteLibrary\src -P WhiteLibrary\bin --loglevel DEBUG:INFO PythonWhiteLibrary/atests</li>
	</ul>
	</li>
	<li>Tests currently feature a bug. In division operation the result is expected to be in European comma format. However, if your Windows is configured to use English the calculator uses dot as a decimal separator causing these tests fail.</li>
</ul>

<p><b><b>[1] https://github.com/TestStack/White </b></b></p>
</body>
</html>
