@echo off

reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FlyoutMenuSettings" /v UseWin32TrayNotification /t REG_DWORD /d 1 /f

taskkill /f /im explorer.exe >nul
start explorer.exe