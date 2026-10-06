# PowerShell wrapper for tutor CLI
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ArgsList
)
node "$PSScriptRoot\tutor.js" @ArgsList
