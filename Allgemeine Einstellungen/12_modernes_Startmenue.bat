@echo off

reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FlyoutMenuSettings" /v UseWin32TrayNotification /f >nul 2>&1

taskkill /f /im explorer.exe >nul
start explorer.exe