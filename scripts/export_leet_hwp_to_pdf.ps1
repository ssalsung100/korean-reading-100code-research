param(
    [Parameter(Mandatory = $true)]
    [string]$WorkspaceRoot,
    [Parameter(Mandatory = $true)]
    [string]$CorpusRoot,
    [Parameter(Mandatory = $true)]
    [string]$OutputRoot,
    [int]$Limit = 0
)

$ErrorActionPreference = 'Stop'
$manifestPath = Join-Path $corpusRoot 'manifest.json'
$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
$entries = @($manifest.entries | Where-Object {
    $_.kind -like 'question*' -and [IO.Path]::GetExtension($_.file) -ieq '.hwp'
})
if ($Limit -gt 0) {
    $entries = @($entries | Select-Object -First $Limit)
}

$hwp = New-Object -ComObject HWPFrame.HwpObject
$records = @()
try {
    $hwp.XHwpWindows.Item(0).Visible = $false
    foreach ($entry in $entries) {
        $relativeSource = ($entry.file -replace '/', '\')
        $source = Join-Path $WorkspaceRoot $relativeSource
        $yearDir = Join-Path $outputRoot ([string]$entry.label)
        New-Item -ItemType Directory -Force -Path $yearDir | Out-Null
        $base = "{0}_{1}" -f $entry.label, $entry.kind
        $target = Join-Path $yearDir ($base + '.pdf')

        $opened = $hwp.Open($source, 'HWP', 'forceopen:true')
        if (-not $opened) {
            throw "Failed to open HWP: $source"
        }
        try {
            $saved = $hwp.SaveAs($target, 'PDF', '')
            if (-not $saved -or -not (Test-Path -LiteralPath $target)) {
                throw "Failed to save PDF: $target"
            }
            $records += [PSCustomObject]@{
                label = $entry.label
                kind = $entry.kind
                source_file = $entry.file
                source_sha256 = $entry.sha256
                pdf_file = $target.Substring($WorkspaceRoot.Length + 1).Replace('\', '/')
                bytes = (Get-Item -LiteralPath $target).Length
                status = 'rendered_from_official_hwp'
            }
            Write-Output "RENDERED $base"
        }
        finally {
            $hwp.Clear(1)
        }
    }
}
finally {
    $hwp.Quit()
}

$manifestOut = [PSCustomObject]@{
    records = $records
    note = 'Verification PDF rendered from the official HWP through Hancom Office automation.'
}
$manifestOut | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $outputRoot 'manifest.json') -Encoding UTF8
Write-Output ("WROTE {0} records" -f $records.Count)
