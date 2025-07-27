@echo off
net session >nul 2>&1

if %errorlevel% neq 0 (
    echo Starte mit Administratorrechten...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)