@echo off
:: Entfernt Microsoft.WindowsSoundRecorder aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.WindowsSoundRecorder'"
pause