@echo off
:: Entfernt Microsoft.Todos aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.Todos'"
pause