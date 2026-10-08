param(
    [Parameter(Mandatory = $true)]
    [string]$Source,
    [Parameter(Mandatory = $true)]
    [string]$Output
)

$ErrorActionPreference = 'Stop'
$hwp = New-Object -ComObject HWPFrame.HwpObject
try {
    $opened = $hwp.Open($Source, 'HWP', 'forceopen:true;versionwarning:false;')
    Write-Output ("OPEN={0} COUNT={1}" -f $opened, $hwp.PageCount)
    $attempts = @(
        @(0, 0, 0, 0),
        @(0, 144, 0, 0),
        @(1, 144, 0, 0),
        @(0, 1200, 1600, 0)
    )
    foreach ($values in $attempts) {
        try {
            $candidate = "{0}_{1}_{2}_{3}_{4}.png" -f $Output, $values[0], $values[1], $values[2], $values[3]
            $result = $hwp.CreatePageImage($candidate, $values[0], $values[1], $values[2], $values[3])
            Write-Output ("CALL={0},{1},{2},{3} RESULT={4} EXISTS={5}" -f $values[0], $values[1], $values[2], $values[3], $result, (Test-Path -LiteralPath $candidate))
        }
        catch {
            Write-Output ("CALL={0},{1},{2},{3} ERROR={4}" -f $values[0], $values[1], $values[2], $values[3], $_.Exception.Message)
        }
    }
}
finally {
    $hwp.Clear(1)
    $hwp.Quit()
}
