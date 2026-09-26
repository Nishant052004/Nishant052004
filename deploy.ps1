Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Deploying Nishant052004 GitHub Profile Repository" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

git init
git branch -M main
git add .
git commit -m "feat: enhance profile with dynamic mechanisms, terminal, repo matrix & CI workflows"
try { git remote remove origin 2>$null } catch {}
git remote add origin https://github.com/Nishant052004/Nishant052004.git

Write-Host "`nPushing to https://github.com/Nishant052004/Nishant052004.git ...`n" -ForegroundColor Yellow
Write-Host "(Make sure you have created the public repo Nishant052004/Nishant052004 on GitHub first!)`n" -ForegroundColor Gray

git push -u origin main

Write-Host "`n========================================================" -ForegroundColor Green
Write-Host "  Done! Check your profile at https://github.com/Nishant052004" -ForegroundColor Green
Write-Host "========================================================`n" -ForegroundColor Green
