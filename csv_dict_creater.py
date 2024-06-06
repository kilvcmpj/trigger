$nextToken = $null
$workflows = @()

do {
    if ($null -eq $nextToken) {
        $response = aws glue list-workflows | ConvertFrom-Json
    } else {
        $response = aws glue list-workflows --next-token $nextToken | ConvertFrom-Json
    }

    $workflows += $response.Workflows
    $nextToken = $response.NextToken

} while ($null -ne $nextToken)

# Output all workflows
$workflows | ForEach-Object { Write-Output $_ }
