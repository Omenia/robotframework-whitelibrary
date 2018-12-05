@echo off
pushd %~dp0
REM remove files from possible previous installation
if exist "files.txt" (
  for /f "delims=" %%f in (files.txt) do (
    if exist "%%f" (
	  del "%%f"
	)
  )
)
REM install and list installed files to a file
call python setup.py install --record files.txt
set DEPLOYMENT=deploy
set NUGET=packages
REM create empty build.info
echo. 2> build.info
call deploy.cmd
call run_tests.cmd %*
popd