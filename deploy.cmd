mkdir %DEPLOYMENT%
mkdir %DEPLOYMENT%\keywords
mkdir %DEPLOYMENT%\keywords\items

copy PythonWhiteLibrary\src\WhiteLibrary.py %DEPLOYMENT%\
copy PythonWhiteLibrary\version.py %DEPLOYMENT%\
copy PythonWhiteLibrary\src\__init__.py %DEPLOYMENT%\
copy PythonWhiteLibrary\setup.py %DEPLOYMENT%\
copy PythonWhiteLibrary\src\keywords\__init__.py %DEPLOYMENT%\keywords\
copy PythonWhiteLibrary\src\keywords\application.py %DEPLOYMENT%\keywords\
copy PythonWhiteLibrary\src\keywords\keyboard.py %DEPLOYMENT%\keywords\
copy PythonWhiteLibrary\src\keywords\librarycomponent.py %DEPLOYMENT%\keywords\
copy PythonWhiteLibrary\src\keywords\robotlibcore.py %DEPLOYMENT%\keywords\
copy PythonWhiteLibrary\src\keywords\window.py %DEPLOYMENT%\keywords\
copy PythonWhiteLibrary\src\keywords\items\__init__.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\buttons.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\label.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\listcontrols.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\menu.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\progressbar.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\slider.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\tab.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\textbox.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\tree.py %DEPLOYMENT%\keywords\items\
copy PythonWhiteLibrary\src\keywords\items\uiitem.py %DEPLOYMENT%\keywords\items\

copy %NUGET%\Castle.Core.3.3.0\lib\net45\Castle.Core.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.0.13.3\lib\net40\TestStack.White.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.Reporting.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.ScreenObjects.dll %DEPLOYMENT%\

copy build.info %DEPLOYMENT%\
