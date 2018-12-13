mkdir %DEPLOYMENT%
mkdir src\WhiteLibrary\bin\ 

copy %NUGET%\Castle.Core.3.3.0\lib\net45\Castle.Core.dll src\WhiteLibrary\bin\
copy %NUGET%\TestStack.White.0.13.3\lib\net40\TestStack.White.dll src\WhiteLibrary\bin\
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.Reporting.dll src\WhiteLibrary\bin\
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.ScreenObjects.dll src\WhiteLibrary\bin\

xcopy src %DEPLOYMENT%\ /s /a
copy setup.py %DEPLOYMENT%\
copy build.info %DEPLOYMENT%\
