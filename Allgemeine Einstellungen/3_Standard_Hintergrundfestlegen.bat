@echo off

set "WALLPAPER=C:\Windows\Web\Wallpaper\Windows\img0.jpg"
REG ADD "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "%WALLPAPER%" /f
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters