# 코드 리뷰 스크립트
# 사용법: .\review.ps1 <파일경로> [-interactive] [-save] [-focus <영역들>]

param(
    [Parameter(Position = 0, Mandatory = $true)]
    [string]$FilePath,

    [switch]$Interactive,
    [switch]$Save,
    [string[]]$Focus
)

# Python 스크립트 경로
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "code_reviewer.py"

# 커맨드 구성
$cmd = @("python", $pythonScript, $FilePath)

if ($Focus -and $Focus.Count -gt 0) {
    $cmd += "--focus"
    $cmd += $Focus
}

if ($Interactive) {
    $cmd += "--interactive"
}

if ($Save) {
    $cmd += "--save"
}

# 실행
& $cmd[0] $cmd[1..($cmd.Count - 1)]
