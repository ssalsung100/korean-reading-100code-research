param(
    [Parameter(Mandatory = $true)]
    [string]$Source,
    [Parameter(Mandatory = $true)]
    [string]$Output
)

$ErrorActionPreference = 'Stop'
$targetDir = Split-Path -Parent $Output
New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

$hwp = New-Object -ComObject HWPFrame.HwpObject
try {
    $hwp.XHwpWindows.Item(0).Visible = $false
    # An empty format lets Hancom detect legacy HWP 3.x files. Passing
    # "HWP" explicitly can reject those files even though modern HWP 5.x
    # documents open successfully.
    $opened = $hwp.Open($Source, '', 'lock:false;forceopen:true;versionwarning:false;')
    if (-not $opened) {
        throw "Failed to open HWP: $Source"
    }
    Write-Output ("OPEN True PAGES={0}" -f $hwp.PageCount)

    $saved = $hwp.SaveAs($Output, 'PDF', '')
    Write-Output ("SAVEAS={0} EXISTS={1}" -f $saved, (Test-Path -LiteralPath $Output))
    if (-not (Test-Path -LiteralPath $Output)) {
        throw "Failed to save PDF: $Output"
    }
}
finally {
    try { $hwp.Clear(1) } catch {}
    $hwp.Quit()
}
