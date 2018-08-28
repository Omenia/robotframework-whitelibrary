<html>
<head>
	<title></title>
</head>
<body>
<p><b>This library is still very much under construction.</b></p>

<p>&nbsp;</p>

<p><b><b>WhiteLibrary will give a way to test Windows UI technologies with Robot Framework. WhiteLibrary wraps White test automation framework [1] </b></b></p>

<p><b><b><b>Techonologies</b></b></b></p>

<ul>
	<li><b><b>Win32</b></b></li>
	<li><b><b>WinForms</b></b></li>
	<li><b><b>WPF (Windows Presentation Foundation)</b></b></li>
	<li><b><b>Silverlight</b></b></li>
	<li><b><b>SWT (Java) platforms</b></b></li>
</ul>

<p><b><b><b>Development Environment</b></b></b></p>

<ul>
	<li><b><b>Install Visual Studio: https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx<br />
	Python Tools are required but they&#39;re now part of Visual Studio 2017 installer, see details what to select when installing Visual Studio: <a href="https://github.com/Microsoft/PTVS">https://github.com/Microsoft/PTVS</a></b></b></li>
	<li><b><b>Clone project from Github</b></b>
	<ul>
		<li><b><b><del>Howto: http://rickrainey.com/2013/07/27/visual-studio-and-gitub-the-basics-of-working-with-existing-repositories-2/</del> (currently unavailable)<br />
		Howto: https://docs.microsoft.com/en-us/vsts/git/gitquickstart?view=vsts&amp;tabs=visual-studio </b></b></li>
		<li><b><b>Repository https://github.com/Omenia/robotframework-whitelibrary</b></b></li>
	</ul>
	</li>
	<li><strong>Open solution file using Visual studio.</strong>
	<ul>
		<li><strong>RobotFrameworkWhiteLibrary.sln</strong></li>
	</ul>
	</li>
	<li><strong>Build the project to obtain all the related libraries</strong>
	<ul>
		<li><strong>In VS Solution explorer panel -&gt; right click the solution file -&gt; Build</strong></li>
		<li><strong>Result shoild show success and also should download proper libraries/binaries under </strong>
		<ul>
			<li><strong>UIAutomationTest\bin</strong></li>
			<li><strong>WhiteLibrary\bin</strong></li>
		</ul>
		</li>
	</ul>
	</li>
</ul>

<p><b><b><b>Running tests with Robot</b></b></b></p>

<ul>
	<li><b><b>Install Python27 (as of this writing the tests wont run using Python37)</b></b>

	<ul>
		<li><strong>If you have installed multiple Python versions you need to verify that Python27 is defined in the Windows Path environment variable to&nbsp;point to &quot;python.exe&quot;</strong></li>
		<li><strong>If&nbsp;you do not want to use previous definition&nbsp;you can run the tests command line&nbsp;by&nbsp;manually selecting the python exexutable</strong>&nbsp;</li>
	</ul>
	</li>
	<li><b><b>Install Robot Framework and Python for .NET: pip install robotframework pythonnet</b></b>
	<ul>
		<li><strong>Install these for Python27</strong></li>
	</ul>
	</li>
	<li><strong>If you use Windows 10 please install the old calculator application. The tests use calculator as a system under test and require the old calculation application.</strong>
	<ul>
		<li><strong>Instructions: </strong>https://windowsreport.com/download-old-calculator-windows-10/</li>
	</ul>
	</li>
	<li><b><b>Inside the solution execute tests from folder: \PythonWhiteLibrary execute: &quot;run_tests.cmd&quot;. Single test cases can be run with command &quot;run_tests.cmd -t &quot;Test case name&quot;&quot;</b></b>
	<ul>
		<li><strong>If you need to manually select the python executable you can also run:</strong><br />
		python -m robot --outputdir&nbsp;[your log folder]&nbsp;--noncritical unstable -P PythonWhiteLibrary\src -P WhiteLibrary\bin&nbsp; --loglevel DEBUG:INFO PythonWhiteLibrary/atests</li>
	</ul>
	</li>
	<li><strong>Tests currently feature a bug. In division operation the result is expected to be in European comma format. However, if your Windows is configured to use English the calculator uses dot as a decimal separator causing these tests fail.</strong></li>
</ul>

<p><b><b>[1] https://github.com/TestStack/White </b></b></p>
</body>
</html>
