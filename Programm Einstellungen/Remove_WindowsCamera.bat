@echo off
:: Entfernt Microsoft.WindowsCamera aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.WindowsCamera'"
pause