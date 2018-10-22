@echo on
if "%DEPLOYMENT%" == "" (
  if "%NUGET%" == "" (
    set NUGET=packages
  )
  set PP=-P PythonWhiteLibrary\src -P PythonWhiteLibrary -P %NUGET%\Castle.Core.3.3.0\lib\net45\ -P %NUGET%\TestStack.White.0.13.3\lib\net40 -P %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40
) else (
  set PP=-P %DEPLOYMENT%
)
robot --outputdir output --noncritical unstable %PP% %* --loglevel DEBUG:INFO PythonWhiteLibrary/atests
