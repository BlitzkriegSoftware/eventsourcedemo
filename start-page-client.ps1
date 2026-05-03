<#
    Html Page Client
#>
$script = Join-Path -Path $PSScriptRoot -ChildPath "index.html"
Start-Process "chrome.exe" "--new-window $script"