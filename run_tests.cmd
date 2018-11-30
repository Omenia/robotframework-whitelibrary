@echo on
if "%NUGET%" == "" (
  set NUGET=packages
)
if "%DEPLOYMENT%" == "" (
  set PP=-P %NUGET%\Castle.Core.3.3.0\lib\net45\ -P %NUGET%\TestStack.White.0.13.3\lib\net40 -P %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40 -P src\WhiteLibrary\keywords -P src\WhiteLibrary\keywords\items -P src
) else (
  set PP=-P %DEPLOYMENT% -P %DEPLOYMENT%\keywords -P %DEPLOYMENT%\keywords\items
)
pushd %~dp0
robot --outputdir output --noncritical unstable %PP% %* --loglevel DEBUG:INFO atests
popd