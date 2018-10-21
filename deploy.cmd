mkdir %DEPLOYMENT%
copy PythonWhiteLibrary\src\WhiteLibrary.py %DEPLOYMENT%\
copy PythonWhiteLibrary\version.py %DEPLOYMENT%\
copy PythonWhiteLibrary\src\__init__.py %DEPLOYMENT%\
copy PythonWhiteLibrary\setup.py %DEPLOYMENT%\

copy %NUGET%\Castle.Core.3.3.0\lib\net45\Castle.Core.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.0.13.3\lib\net40\TestStack.White.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.Reporting.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.ScreenObjects.dll %DEPLOYMENT%\

copy build.info %DEPLOYMENT%\
