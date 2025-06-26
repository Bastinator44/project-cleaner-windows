@echo off
:: Entfernt Microsoft.ZuneVideo aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.ZuneVideo'"
pause