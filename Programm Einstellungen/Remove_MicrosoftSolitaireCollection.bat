@echo off
:: Entfernt Microsoft.MicrosoftSolitaireCollection aus der Provisioned-App-Liste (für neue Benutzer)
powershell -command "Remove-AppxProvisionedPackage -Online -PackageName 'Microsoft.MicrosoftSolitaireCollection'"
pause