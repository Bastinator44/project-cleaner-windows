@echo off
:: Entfernt Microsoft.SkypeApp aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.SkypeApp'"
pause