import subprocess

def get_provisioned_packages():
    cmd = [
        "powershell",
        "-Command",
        "Get-AppxProvisionedPackage -Online | Select-Object -ExpandProperty PackageName"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.splitlines()

def get_installed_packages():
    cmd = [
        "powershell",
        "-Command",
        "Get-AppxPackage | Select-Object -ExpandProperty Name"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.splitlines()

# Beispielaufruf:
provisioned = get_provisioned_packages()
installed = get_installed_packages()

print("Provisioned Packages:", provisioned)
print("Installed Packages:", installed)