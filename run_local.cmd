@echo off
pushd %~dp0
set DEPLOYMENT=deploy
set NUGET=packages
echo > build.info
call deploy.cmd
call run_tests.cmd %*
popd