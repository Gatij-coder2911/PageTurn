@echo off
echo Installing Python 3.10.11
echo x=msgbox("Please Check the Add to PATH option", 48, "Important") > msgbox.vbs
start /wait msgbox.vbs
del "./msgbox.vbs"
echo.
start /wait ./python-3.10.11-amd64.exe
echo.

echo Installing django Module
echo.
start /wait pip install django
echo.

echo Installing Pillow Module
echo.
start /wait pip install Pillow
echo.

echo Installing mysqlclient Module
echo.
start /wait pip install mysqlclient
echo.


echo All Dependencies Installed...

pause