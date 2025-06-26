@echo off
:: Entfernt Microsoft.BingWeather aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.BingWeather'"
pause