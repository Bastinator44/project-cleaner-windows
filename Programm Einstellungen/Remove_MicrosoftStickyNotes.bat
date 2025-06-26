@echo off
:: Entfernt Microsoft.MicrosoftStickyNotes aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.MicrosoftStickyNotes'"
pause