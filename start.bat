@echo off 
set work_disk=%~d0
set work_path=%~dp0

taskkill /F /IM xxx_server.exe

::检查是否安装了git-base
set GIT_PATH=""
for /f %%I in ('where git') do echo %%I findstr 'git' && set GIT_PATH=%%I
echo -----ok
if %GIT_PATH% == "" goto Install_env

set python_name=plugins_py3
set dist_path=%USERPROFILE%\.proj-plugins\plugins\%python_name%
echo -----2
echo %dist_path%
if exist %dist_path% (
    echo %dist_path%
) else (
    goto Install_env
)

set python3_path=""
for /f %%I in ('where python') do echo %%I findstr 'python37' && set python3_path=%%I
echo %python3_path%

if %python3_path% == "" (
	rmdir /Q /S %dist_path%
	goto Install_env
) else (
	goto Run
)

::安装python,创建python虚拟环境
:Install_env
start /wait "install" cmd /c call python_install.bat

::后台启动程序 xxx_server.exe
:Run
cd %work_path%
%work_disk%
::
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin
xxx_server.exe
