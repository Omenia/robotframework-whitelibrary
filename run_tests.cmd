@echo on
if "%NUGET%" == "" (
  set NUGET=packages
)
if "%DEPLOYMENT%" == "" (
  set PP=-P %NUGET%\Castle.Core.3.3.0\lib\net45\ -P %NUGET%\TestStack.White.0.13.3\lib\net40 -P %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40 -P PythonWhiteLibrary\src\keywords -P PythonWhiteLibrary\src\keywords\items -P PythonWhiteLibrary\src -P PythonWhiteLibrary
) else (
  set PP=-P %DEPLOYMENT%
)
robot --outputdir output --noncritical unstable %PP% %* --loglevel DEBUG:INFO PythonWhiteLibrary/atests
