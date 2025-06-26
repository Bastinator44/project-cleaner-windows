@echo off
:: Entfernt Microsoft.People aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.People'"
pause