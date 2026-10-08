$ErrorActionPreference = 'Stop'
$hwp = New-Object -ComObject HWPFrame.HwpObject
try {
    Write-Output ("HWP_COM_OK " + $hwp.Version)
    $registryPaths = @(
        'Registry::HKEY_CURRENT_USER\Software\HNC\HwpAutomation\Modules',
        'Registry::HKEY_LOCAL_MACHINE\Software\HNC\HwpAutomation\Modules',
        'Registry::HKEY_LOCAL_MACHINE\Software\WOW6432Node\HNC\HwpAutomation\Modules'
    )
    foreach ($registryPath in $registryPaths) {
        if (Test-Path $registryPath) {
            Write-Output ("MODULE_REGISTRY " + $registryPath)
            Get-ItemProperty -Path $registryPath | Format-List | Out-String | Write-Output
            Get-ChildItem -Path $registryPath -Recurse | ForEach-Object {
                Write-Output ("MODULE_KEY " + $_.PSChildName)
                Get-ItemProperty -Path $_.PSPath | Format-List | Out-String | Write-Output
            }
        }
    }
}
finally {
    $hwp.Quit()
}
