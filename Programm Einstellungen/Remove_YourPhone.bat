@echo off
:: Entfernt Microsoft.YourPhone aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.YourPhone'"
pause