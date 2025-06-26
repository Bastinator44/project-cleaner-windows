@echo off
:: Entfernt Microsoft.XboxGamingOverlay aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.XboxGamingOverlay'"
pause