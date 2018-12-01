@echo on

pushd %~dp0
robot --outputdir output --noncritical unstable %* --loglevel DEBUG:INFO atests
popd