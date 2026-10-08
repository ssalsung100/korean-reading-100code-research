param(
    [Parameter(Mandatory = $true)]
    [string]$WorkspaceRoot,
    [Parameter(Mandatory = $true)]
    [string]$CorpusManifest,
    [Parameter(Mandatory = $true)]
    [string]$OutputRoot,
    [int]$Resolution = 144,
    [int]$Limit = 0,
    [string]$Label = ''
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$manifest = Get-Content -LiteralPath $CorpusManifest -Raw -Encoding UTF8 | ConvertFrom-Json
$entries = @($manifest.records | Where-Object {
    $_.kind -eq 'question_odd' -and
    $_.method -eq 'hwp5txt_direct' -and
    [int]$_.year -le 2021 -and
    [IO.Path]::GetExtension($_.source_file) -ieq '.hwp'
} | Sort-Object @{ Expression = {[int]$_.year} }, label)
if ($Label) {
    $entries = @($entries | Where-Object { [string]$_.label -eq $Label })
}
if ($Limit -gt 0) {
    $entries = @($entries | Select-Object -First $Limit)
}

New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null
$asciiRoot = Join-Path $env:TEMP 'leet_hwp_page_export'
New-Item -ItemType Directory -Force -Path $asciiRoot | Out-Null

$hwp = New-Object -ComObject HWPFrame.HwpObject
$records = @()
$moduleRegistered = $false
try {
    $hwp.XHwpWindows.Item(0).Visible = $false
    try {
        $moduleRegistered = [bool]$hwp.RegisterModule('FilePathCheckDLL', 'FilePathCheckerModule')
    }
    catch {
        $moduleRegistered = $false
    }

    foreach ($entry in $entries) {
        $source = Join-Path $WorkspaceRoot ($entry.source_file -replace '/', '\')
        $label = [string]$entry.label
        $safeLabel = $label -replace '[^0-9A-Za-z_-]', '_'
        $tempDir = Join-Path $asciiRoot $safeLabel
        $targetDir = Join-Path $OutputRoot $label
        New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
        New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

        $opened = $hwp.Open($source, '', 'lock:false;forceopen:true;versionwarning:false;')
        if (-not $opened) {
            throw "Failed to open HWP: $source"
        }
        try {
            $pageCount = [int]$hwp.PageCount
            $pageRecords = @()
            for ($pageIndex = 0; $pageIndex -lt $pageCount; $pageIndex++) {
                $baseName = 'page_{0:D3}' -f ($pageIndex + 1)
                $tempFile = Join-Path $tempDir ($baseName + '.bmp')
                $targetFile = Join-Path $targetDir ($baseName + '.png')
                if (Test-Path -LiteralPath $tempFile) {
                    Remove-Item -LiteralPath $tempFile -Force
                }
                $created = $hwp.CreatePageImage($tempFile, $pageIndex, $Resolution, 24, 'bmp')
                if (-not $created -or -not (Test-Path -LiteralPath $tempFile)) {
                    throw "Failed to render page $($pageIndex + 1) of $label"
                }
                $bitmap = [System.Drawing.Image]::FromFile($tempFile)
                try {
                    $bitmap.Save($targetFile, [System.Drawing.Imaging.ImageFormat]::Png)
                    $width = $bitmap.Width
                    $height = $bitmap.Height
                }
                finally {
                    $bitmap.Dispose()
                }
                Remove-Item -LiteralPath $tempFile -Force
                $item = Get-Item -LiteralPath $targetFile
                $relativeFile = $targetFile.Substring($WorkspaceRoot.Length + 1).Replace('\', '/')
                $pageRecords += [PSCustomObject]@{
                    page = $pageIndex + 1
                    file = $relativeFile
                    bytes = $item.Length
                    width = $width
                    height = $height
                }
            }
            $records += [PSCustomObject]@{
                label = $label
                year = [int]$entry.year
                source_file = $entry.source_file
                source_sha256 = $entry.source_sha256
                page_count = $pageCount
                resolution_dpi = $Resolution
                color_depth = 24
                format = 'png'
                pages = $pageRecords
                status = 'rendered_from_official_hwp_by_hancom_create_page_image'
            }
            Write-Output ("RENDERED {0} pages={1}" -f $label, $pageCount)
        }
        finally {
            $hwp.Clear(1)
        }
    }
}
finally {
    try { $hwp.Quit() } catch {}
}

$manifestOut = [PSCustomObject]@{
    status = if ($records.Count -eq $entries.Count) { 'complete' } else { 'partial' }
    expected_records = $entries.Count
    record_count = $records.Count
    file_path_check_module_registered = $moduleRegistered
    renderer = 'Hancom HWPFrame.HwpObject.CreatePageImage'
    note = 'Page-faithful bitmap images rendered from official odd-form HWP files. Page numbering is one-based in this manifest.'
    records = $records
}
$manifestPath = Join-Path $OutputRoot 'manifest.json'
$manifestOut | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $manifestPath -Encoding UTF8
Write-Output ("WROTE {0}/{1} records manifest={2}" -f $records.Count, $entries.Count, $manifestPath)
