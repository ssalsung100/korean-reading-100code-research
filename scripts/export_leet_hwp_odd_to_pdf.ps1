param(
    [Parameter(Mandatory = $true)]
    [string]$WorkspaceRoot,
    [Parameter(Mandatory = $true)]
    [string]$CorpusManifest,
    [Parameter(Mandatory = $true)]
    [string]$OutputRoot
)

$ErrorActionPreference = 'Stop'
$manifest = Get-Content -LiteralPath $CorpusManifest -Raw -Encoding UTF8 | ConvertFrom-Json
$entries = @($manifest.records | Where-Object {
    $_.kind -eq 'question_odd' -and
    $_.method -eq 'hwp5txt_direct' -and
    [int]$_.year -le 2021 -and
    [IO.Path]::GetExtension($_.source_file) -ieq '.hwp'
} | Sort-Object @{ Expression = {[int]$_.year} }, label)

New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null
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
        $yearDir = Join-Path $OutputRoot ([string]$entry.label)
        New-Item -ItemType Directory -Force -Path $yearDir | Out-Null
        $target = Join-Path $yearDir ("{0}_question_odd.pdf" -f $entry.label)
        $opened = $hwp.Open($source, '', 'lock:false;forceopen:true;versionwarning:false;')
        if (-not $opened) {
            throw "Failed to open HWP: $source"
        }
        try {
            $pageCount = [int]$hwp.PageCount
            $null = $hwp.HAction.GetDefault('FileSaveAsPDF', $hwp.HParameterSet.HFileOpenSave.HSet)
            $hwp.HParameterSet.HFileOpenSave.FileName = $target
            $hwp.HParameterSet.HFileOpenSave.Format = 'PDF'
            $hwp.HParameterSet.HFileOpenSave.Attributes = 0
            $saved = $hwp.HAction.Execute('FileSaveAsPDF', $hwp.HParameterSet.HFileOpenSave.HSet)
            if (-not $saved -or -not (Test-Path -LiteralPath $target)) {
                throw "Failed to save PDF: $target"
            }
            $relativePdf = $target.Substring($WorkspaceRoot.Length + 1).Replace('\', '/')
            $records += [PSCustomObject]@{
                label = $entry.label
                year = [int]$entry.year
                kind = $entry.kind
                source_file = $entry.source_file
                source_sha256 = $entry.source_sha256
                pdf_file = $relativePdf
                page_count = $pageCount
                bytes = (Get-Item -LiteralPath $target).Length
                status = 'rendered_from_official_hwp_by_hancom'
            }
            Write-Output ("RENDERED {0} pages={1}" -f $entry.label, $pageCount)
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
    note = 'Page-faithful verification PDFs rendered from the official odd-form HWP files through Hancom Office automation.'
    records = $records
}
$manifestOut | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $OutputRoot 'manifest.json') -Encoding UTF8
Write-Output ("WROTE {0}/{1} records module={2}" -f $records.Count, $entries.Count, $moduleRegistered)
