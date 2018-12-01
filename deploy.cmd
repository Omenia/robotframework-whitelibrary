mkdir %DEPLOYMENT%

copy %NUGET%\Castle.Core.3.3.0\lib\net45\Castle.Core.dll src\WhiteLibrary\bin
copy %NUGET%\TestStack.White.0.13.3\lib\net40\TestStack.White.dll src\WhiteLibrary\bin
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.Reporting.dll src\WhiteLibrary\bin
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.ScreenObjects.dll src\WhiteLibrary\bin

xcopy /s src\WhiteLibrary %DEPLOYMENT% 

copy build.info %DEPLOYMENT%\
