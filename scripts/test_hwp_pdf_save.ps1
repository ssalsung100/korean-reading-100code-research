param(
    [Parameter(Mandatory = $true)]
    [string]$Source,
    [Parameter(Mandatory = $true)]
    [string]$Output
)
$ErrorActionPreference = 'Stop'
$targetDir = Split-Path -Parent $Output
New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
$hwp = New-Object -ComObject HWPFrame.HwpObject.2
try {
    $hwp.XHwpWindows.Item(0).Visible = $false
    Write-Output ("OPEN " + $hwp.Open($Source, '', 'lock:false;forceopen:true;versionwarning:false;'))
    Write-Output ("LOCK_FileSaveAsPdf " + $hwp.IsCommandLock('FileSaveAsPdf'))
    Write-Output ("LOCK_FileSaveAsPDF " + $hwp.IsCommandLock('FileSaveAsPDF'))
    Write-Output ("DEFAULT " + $hwp.HAction.GetDefault('FileSaveAsPDF', $hwp.HParameterSet.HFileOpenSave.HSet))
    $hwp.HParameterSet.HFileOpenSave.FileName = $Output
    $hwp.HParameterSet.HFileOpenSave.Format = 'PDF'
    $hwp.HParameterSet.HFileOpenSave.Attributes = 0
    Write-Output ("SAVE " + $hwp.HAction.Execute('FileSaveAsPDF', $hwp.HParameterSet.HFileOpenSave.HSet))
    Write-Output ("EXISTS " + (Test-Path -LiteralPath $Output))
}
finally {
    $hwp.Clear(1)
    $hwp.Quit()
}
