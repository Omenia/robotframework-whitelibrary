pushd %~dp0
ping 127.0.0.1 -n 6
start /B bin\Debug\UIAutomationTest.exe
popd
