@echo off
:: Entfernt Microsoft.WindowsAlarms aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.WindowsAlarms'"
pause