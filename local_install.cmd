@echo off
pushd %~dp0
REM install White dlls
nuget restore src\WhiteLibrary\packages.config -PackagesDirectory packages
nuget restore UIAutomationTest\packages.config -PackagesDirectory UIAutomationTest\packages

REM copy all dll packages into same location
mkdir src\WhiteLibrary\bin\

copy packages\Castle.Core.3.3.0\lib\net45\Castle.Core.dll src\WhiteLibrary\bin\
copy packages\Salabs.TestStack.White.0.13.4\lib\net40\TestStack.White.dll src\WhiteLibrary\bin\
copy packages\Salabs.TestStack.White.ScreenObjects.0.13.4\lib\net40\TestStack.White.Reporting.dll src\WhiteLibrary\bin\
copy packages\Salabs.TestStack.White.ScreenObjects.0.13.4\lib\net40\TestStack.White.ScreenObjects.dll src\WhiteLibrary\bin\

REM remove files from possible previous installation
if exist "files.txt" (
  for /f "delims=" %%f in (files.txt) do (
    if exist "%%f" (
	  del "%%f"
	)
  )
)
REM install WhiteLibrary and list installed files to a file
call python setup.py install --record files.txt
popd
