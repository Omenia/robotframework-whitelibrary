mkdir %DEPLOYMENT%
mkdir %DEPLOYMENT%\keywords
mkdir %DEPLOYMENT%\keywords\items

copy src\WhiteLibrary\version.py %DEPLOYMENT%\
copy src\WhiteLibrary\__init__.py %DEPLOYMENT%\
copy setup.py %DEPLOYMENT%\
copy src\WhiteLibrary\keywords\__init__.py %DEPLOYMENT%\keywords\
copy src\WhiteLibrary\keywords\application.py %DEPLOYMENT%\keywords\
copy src\WhiteLibrary\keywords\keyboard.py %DEPLOYMENT%\keywords\
copy src\WhiteLibrary\keywords\librarycomponent.py %DEPLOYMENT%\keywords\
copy src\WhiteLibrary\keywords\robotlibcore.py %DEPLOYMENT%\keywords\
copy src\WhiteLibrary\keywords\window.py %DEPLOYMENT%\keywords\
copy src\WhiteLibrary\keywords\screenshot.py %DEPLOYMENT%\keywords\
copy src\WhiteLibrary\keywords\items\__init__.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\buttons.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\label.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\listcontrols.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\menu.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\progressbar.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\slider.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\tab.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\textbox.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\tree.py %DEPLOYMENT%\keywords\items\
copy src\WhiteLibrary\keywords\items\uiitem.py %DEPLOYMENT%\keywords\items\

copy %NUGET%\Castle.Core.3.3.0\lib\net45\Castle.Core.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.0.13.3\lib\net40\TestStack.White.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.Reporting.dll %DEPLOYMENT%\
copy %NUGET%\TestStack.White.ScreenObjects.0.13.3\lib\net40\TestStack.White.ScreenObjects.dll %DEPLOYMENT%\

copy build.info %DEPLOYMENT%\
