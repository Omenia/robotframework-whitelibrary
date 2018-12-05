@echo off
pushd %~dp0
set DEPLOYMENT=deploy
set NUGET=packages
echo. 2> build.info
call deploy.cmd
call run_tests.cmd %*
popd