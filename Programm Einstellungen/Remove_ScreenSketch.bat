@echo off
:: Entfernt Microsoft.ScreenSketch aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.ScreenSketch'"
pause