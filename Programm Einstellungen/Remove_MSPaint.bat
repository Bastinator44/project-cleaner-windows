@echo off
:: Entfernt Microsoft.MSPaint aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.MSPaint'"
pause