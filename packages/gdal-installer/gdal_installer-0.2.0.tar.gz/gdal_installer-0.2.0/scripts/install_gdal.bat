@echo off

REM Get script directory and change to it
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

REM Execute Python installer
python install-gdal