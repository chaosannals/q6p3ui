@echo off
set PYSIDE_DESIGNER_PLUGINS=%~dp0
echo %PYSIDE_DESIGNER_PLUGINS%
".\.pyv39\Lib\site-packages\PySide6\designer.exe"
