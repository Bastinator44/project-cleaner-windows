@echo off
:: Entfernt Microsoft.WindowsCalculator aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.WindowsCalculator'"
pause