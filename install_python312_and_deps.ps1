<#
PowerShell helper to install Python 3.12 (using winget if available) and then install project pip dependencies.
Run as Administrator in PowerShell.

Usage (run from project folder):
  Open PowerShell as Administrator, cd to project folder, then:
    Set-ExecutionPolicy Bypass -Scope Process -Force; .\install_python312_and_deps.ps1
#>

function Write-Info($m){ Write-Host "[INFO] $m" -ForegroundColor Cyan }
function Write-OK($m){ Write-Host "[OK]   $m" -ForegroundColor Green }
function Write-Err($m){ Write-Host "[ERROR] $m" -ForegroundColor Red }

Write-Info "Starting installer script..."

# Helper to run command and capture output
function Run-Command($cmd){
    $out = & cmd /c $cmd 2>&1
    return @{ExitCode=$LASTEXITCODE; Output=$out}
}

# Check for python
try{
    $pyVersionOut = python --version 2>&1
    $pythonFound = $true
} catch {
    $pythonFound = $false
}

if ($pythonFound -and $pyVersionOut -match 'Python (\d+)\.(\d+)\.(\d+)'){
    $major = [int]$matches[1]; $minor = [int]$matches[2]
    Write-Info "Detected Python version: $pyVersionOut"
    if ($major -gt 3 -or ($major -eq 3 -and $minor -ge 12)){
        Write-OK "Python meets requirement (3.12+). Skipping Python install."
    } else {
        Write-Info "Python version is older than 3.12. Attempting to install Python 3.12 via winget..."
        $pythonFound = $false
    }
}

if (-not $pythonFound){
    # Try winget
    $wingetAvailable = $false
    try{
        $wingetVer = winget --version 2>$null
        if ($LASTEXITCODE -eq 0){ $wingetAvailable = $true }
    } catch { $wingetAvailable = $false }

    if ($wingetAvailable){
        Write-Info "winget detected. Installing Python 3 using winget (may install latest 3.x)."
        Write-Info "Accepting package/source agreements..."
        $args = 'install --id Python.Python.3 -e --accept-package-agreements --accept-source-agreements'
        $res = Run-Command("winget $args")
        if ($res.ExitCode -eq 0){
            Write-OK "winget install finished."
        } else {
            Write-Err "winget install failed. Output:`n$res.Output"
            Write-Info "Please install Python 3.12 manually from https://www.python.org/downloads/ and re-run this script."
            exit 1
        }
    } else {
        Write-Err "winget is not available. Please download and install Python 3.12 from https://www.python.org/downloads/ manually."
        Write-Info "After installing Python 3.12, re-run this script."
        exit 1
    }
}

# Refresh environment PATH in current session (try to pick up new python)
$env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User')

# Verify python now
try{ $pv = python --version 2>&1 } catch { $pv = $null }
if (-not $pv){
    Write-Err "Python still not found in PATH. Please restart PowerShell or your machine and re-run this script."
    exit 1
}
Write-OK "Python available: $pv"

# Upgrade pip, setuptools, wheel
Write-Info "Upgrading pip, setuptools and wheel..."
python -m pip install --upgrade pip setuptools wheel
if ($LASTEXITCODE -ne 0){ Write-Err "Failed to upgrade pip/tools."; exit 1 }
Write-OK "pip, setuptools and wheel upgraded."

# Install project dependencies
if (Test-Path .\requirements.txt){
    Write-Info "Installing pip packages from requirements.txt..."
    python -m pip install -r .\requirements.txt
    if ($LASTEXITCODE -ne 0){
        Write-Err "pip install -r requirements.txt failed. Try running the failed command manually or see errors above."
        exit 1
    }
    Write-OK "All pip packages installed successfully."
} else {
    Write-Err "requirements.txt not found in current folder. Ensure you run this script from project root."
    exit 1
}

Write-OK "Installation complete. You can now run the Streamlit app with:\n   streamlit run streamlit_app.py"

exit 0
