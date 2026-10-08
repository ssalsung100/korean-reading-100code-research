param(
    [Parameter(Mandatory = $true)]
    [string]$Source,
    [Parameter(Mandatory = $true)]
    [string]$Output
)

$ErrorActionPreference = 'Stop'
$hwp = New-Object -ComObject HWPFrame.HwpObject
$rows = @()
$pageCount = 0
try {
    $hwp.XHwpWindows.Item(0).Visible = $false
    try { $null = $hwp.RegisterModule('FilePathCheckDLL', 'FilePathCheckerModule') } catch {}
    $opened = $hwp.Open($Source, '', 'lock:false;forceopen:true;versionwarning:false;')
    if (-not $opened) { throw "Failed to open HWP: $Source" }
    $pageCount = [int]$hwp.PageCount

    $ctrl = $hwp.HeadCtrl
    $order = 0
    while ($null -ne $ctrl) {
        $order++
        $ctrlId = [string]$ctrl.CtrlID
        if ($true) {
            $anchor = $ctrl.GetAnchorPos(0)
            $list = $anchor.Item('List')
            $para = $anchor.Item('Para')
            $pos = $anchor.Item('Pos')
            $null = $hwp.SetPosBySet($anchor)
            [int]$sectionCount = 0
            [int]$sectionNumber = 0
            [int]$printedPage = 0
            [int]$columnNumber = 0
            [int]$lineNumber = 0
            [int]$charPosition = 0
            [int16]$overtype = 0
            [string]$controlName = ''
            $null = $hwp.KeyIndicator(
                [ref]$sectionCount,
                [ref]$sectionNumber,
                [ref]$printedPage,
                [ref]$columnNumber,
                [ref]$lineNumber,
                [ref]$charPosition,
                [ref]$overtype,
                [ref]$controlName
            )
            $propertyValues = @{}
            try {
                $props = $ctrl.Properties
                foreach ($name in @('Width','Height','HorzOffset','VertOffset','HorzRelTo','VertRelTo','TreatAsChar','TextWrap','NumberingType')) {
                    try { $propertyValues[$name] = $props.Item($name) } catch {}
                }
            }
            catch {}
            $rows += [PSCustomObject]@{
                control_order = $order
                ctrl_id = $ctrlId
                anchor_list = $list
                anchor_para = $para
                anchor_pos = $pos
                section_count = $sectionCount
                section_number = $sectionNumber
                printed_page = $printedPage
                column_number = $columnNumber
                line_number = $lineNumber
                char_position = $charPosition
                overtype = $overtype
                control_name = $controlName
                properties = $propertyValues
            }
        }
        $ctrl = $ctrl.Next
    }
}
finally {
    try { $hwp.Clear(1) } catch {}
    try { $hwp.Quit() } catch {}
}

$payload = [PSCustomObject]@{
    source = $Source
    page_count = $pageCount
    record_count = $rows.Count
    records = $rows
}
$payload | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $Output -Encoding UTF8
Write-Output ("WROTE controls={0} output={1}" -f $rows.Count, $Output)
