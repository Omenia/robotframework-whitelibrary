mkdir %DEPLOYMENT%
mkdir %DEPLOYMENT%\src\
mkdir src\WhiteLibrary\bin\ 

copy %NUGET%\Castle.Core.3.3.0\lib\net45\Castle.Core.dll src\WhiteLibrary\bin\
copy %NUGET%\TestStack.White.0.13.3\lib\net40\TestStack.White.dll src\WhiteLibrary\bin\

rmdir docs /s /q

python src/WhiteLibrary/version.py > temp.txt
set /p CMDOUT=<temp.txt

IF "%CMDOUT%" == "True" (
    mkdir docs
    python -m robot.libdoc src\WhiteLibrary docs\keywords.html
    xcopy docs %DEPLOYMENT%\docs\ /s /a
)

xcopy src %DEPLOYMENT%\src\ /s /a
copy setup.py %DEPLOYMENT%\
copy requirements.txt %DEPLOYMENT%\
copy MANIFEST* %DEPLOYMENT%\
copy LICENSE %DEPLOYMENT%\
copy README.md %DEPLOYMENT%\
copy build.info %DEPLOYMENT%\
copy requirements.txt %DEPLOYMENT%\
