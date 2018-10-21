@echo on
robot --outputdir output --noncritical unstable -P %DEPLOYMENT% %* --loglevel DEBUG:INFO PythonWhiteLibrary/atests
