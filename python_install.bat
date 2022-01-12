@echo off
set work_disk=%~d0
set work_path=%~dp0
set hide_work=%1
echo %hide_work%
echo %work_disk%
echo %work_path%
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"
	REM reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f
	echo add success
	echo %errorlevel%

echo **********1
copy /y %work_path%\start_plugins.exe c:\windows

::检查是否安装了git-base
set GIT_PATH=""
for /f %%I in ('where git') do echo %%I findstr 'git' && set GIT_PATH="%%I"

if %GIT_PATH% == "" (
	ECHO Start to install Git-2.23.0-64-bit.exe win32......
	start /wait %~dp0\Git-2.23.0-64-bit.exe /quiet
	ECHO install Git-2.23.0-64-bit.exe successfully......
) else (
	echo git-base has been already installed!
)

echo **********2
set tmp_pip3=Scripts\pip3.exe
set python3_path=""
set pip3_path=""

::检查python3.7是否已经安装
for /f %%I in ('where python') do echo %%I findstr 'python37' && set python3_path=%%I
echo 88888888888888888
echo %python3_path%
echo %python3_path%
echo %python3_path%
if exist %python3_path% (
    echo python3.7 has been already installed!
) else (
	:Install_Python
	ECHO Start to install python-3.7.3-amd64.exe win32......
	start /wait %~dp0\python-3.7.3-amd64.exe /quiet InstallAllUsers=1 TargetDir=c:\python37 Include_pip=0 Include_test=0 PrependPath=1 
	ECHO install python-3.7.3-amd64.exe successfully......
	::获取python3.7的路径
	for /f %%I in ('where python') do echo %%I findstr 'python37' && set python3_path=%%I
	
)
for %%A in ("%python3_path%") do (
	Set Folder=%%~dpA
	Set Name=%%~nxA
)

echo **********3
::是否有pip3
set pip3_path=%Folder%%tmp_pip3%
echo %Folder%
echo %Name%
echo %pip3_path%


if exist %pip3_path% (
        echo has %pip3_path%
) else (
	::没有pip3, 安装pip3
	cd bin
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	%python3_path% get-pip.py
	cd ..
)


set pip3_path=%Folder%%tmp_pip3%
if exist %pip3_path% (
	::安装 virtualenv
	%pip3_path% install virtualenv
) else (
	echo 找不到pip, 请检查python3环境
)



echo **********4
::创建plugins_py3虚拟环境
set dist_path=%USERPROFILE%\.proj-plugins\plugins
set user_root=%HOMEDRIVE%
set python_name=plugins_py3

if exist %dist_path% (
    echo dir %dist_path% already exist!
) else (
    md %dist_path%
    echo mkdir %dist_path% success
)

echo %dist_path%

echo %user_root%
echo %python_name%


::切换到目标路径
for %%A in ("%dist_path%") do (
    Set Disk=%%~dA
)
echo --------------
cd %dist_path%
%Disk%
echo ---------- 1
echo %cd%

echo **********5
set virtual_python3=%dist_path%\%python_name%
echo %virtual_python3%

if exist %virtual_python3% (
    echo python virtuaenv %python_name% already exist!
) else (
    %Folder%\Scripts\virtualenv -p %python3_path% %python_name%    
)
cd %virtual_python3%
cd Scripts
echo %cd%
call activate
echo create python virtualenv success
echo virtualenv path %cd%
call deactivate


echo %errorlevel%
if %errorlevel% == 0 (
    echo python3 virtuaenv available
) else (
	echo error run python virtualenv error
    echo please check python virtualenv[%virtual_python3%]
    
    exit
)
echo **********end
