@echo off
:: Entfernt Microsoft.ZuneMusic aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.ZuneMusic'"
pause