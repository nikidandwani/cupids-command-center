# Quick Setup Script for Cupid's Command Center
# Run this on a new laptop to set everything up in 2 minutes!

Write-Host "🎯 CUPID'S COMMAND CENTER - Quick Setup" -ForegroundColor Magenta
Write-Host "========================================" -ForegroundColor Magenta

# Step 1: Check Python
Write-Host "`n📌 Step 1: Checking Python..." -ForegroundColor Cyan
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "   ✅ Python found: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "   ❌ Python not found. Please install Python first." -ForegroundColor Red
    Write-Host "   Run: winget install Python.Python.3.12" -ForegroundColor Yellow
    exit 1
}

# Step 2: Install pandas
Write-Host "`n📌 Step 2: Installing pandas..." -ForegroundColor Cyan
pip install pandas --quiet
Write-Host "   ✅ pandas installed" -ForegroundColor Green

# Step 3: Run data preparation
Write-Host "`n📌 Step 3: Preparing data..." -ForegroundColor Cyan
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location "$scriptPath\data-prep"

if (Test-Path "prepare_data.py") {
    python prepare_data.py
    Write-Host "   ✅ Data prepared successfully!" -ForegroundColor Green
} else {
    Write-Host "   ❌ prepare_data.py not found" -ForegroundColor Red
    exit 1
}

# Step 4: Verify output
Write-Host "`n📌 Step 4: Verifying output files..." -ForegroundColor Cyan
$processedPath = "$scriptPath\data-prep\processed"
$csvCount = (Get-ChildItem -Path $processedPath -Filter "*.csv" | Measure-Object).Count

if ($csvCount -gt 0) {
    Write-Host "   ✅ Found $csvCount CSV files ready for Power BI" -ForegroundColor Green
    Get-ChildItem -Path $processedPath -Filter "*.csv" | ForEach-Object {
        Write-Host "      • $($_.Name)" -ForegroundColor Gray
    }
} else {
    Write-Host "   ❌ No CSV files found" -ForegroundColor Red
}

# Done!
Write-Host "`n========================================" -ForegroundColor Magenta
Write-Host "🎉 SETUP COMPLETE!" -ForegroundColor Green
Write-Host "`nNext steps:" -ForegroundColor White
Write-Host "1. Open Power BI Desktop" -ForegroundColor White
Write-Host "2. Get Data → Text/CSV → data-prep/processed/" -ForegroundColor White
Write-Host "3. Import all CSV files" -ForegroundColor White
Write-Host "4. Follow powerbi/dashboard-setup.md" -ForegroundColor White
Write-Host "`nGood luck at the hackathon! 💝" -ForegroundColor Magenta

# Open the processed folder
explorer "$processedPath"
