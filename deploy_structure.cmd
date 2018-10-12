mkdir %DEPLOYMENT_BASE%
mkdir %DEPLOYMENT_BIN%

copy build.info  %DEPLOYMENT_BASE%\
copy PythonWhiteLibrary/src/WhiteLibrary.py %DEPLOYMENT_BASE%\
copy PythonWhiteLibrary/version.py %DEPLOYMENT_BASE%\
copy PythonWhiteLibrary/src/__init__.py %DEPLOYMENT_BASE%\
copy PythonWhiteLibrary/setup.py %DEPLOYMENT_BASE%\

copy %NUGET_BASE%/bin/Castle.Core.dll %DEPLOYMENT_BIN%\
copy %NUGET_BASE%/bin/TestStack.White.dll %DEPLOYMENT_BIN%\
copy %NUGET_BASE%/bin/TestStack.White.Reporting.dll %DEPLOYMENT_BIN%\
copy %NUGET_BASE%/bin/TestStack.White.ScreenObjects.dll %DEPLOYMENT_BIN%\
copy %NUGET_BASE%/bin/CSWhiteLibrary.dll %DEPLOYMENT_BIN%\
