@echo off
REM This is a test to mimic bug search on Windows CMD
REM This checks if "成功關鍵字" appears in output of main.py

python main.py | findstr "成功關鍵字" >nul
IF %ERRORLEVEL% EQU 0 (
    EXIT /B 0
) ELSE (
    EXIT /B 1
)
