@echo off
:: Entfernt Microsoft.WindowsCommunicationsApps aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.WindowsCommunicationsApps'"
pause