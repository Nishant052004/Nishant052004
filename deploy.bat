@echo off
echo ========================================================
echo   Deploying Nishant052004 GitHub Profile Repository
echo ========================================================
echo.

git init
git branch -M main
git add .
git commit -m "feat: enhance profile with dynamic mechanisms, terminal, repo matrix & CI workflows"
git remote remove origin 2>nul
git remote add origin https://github.com/Nishant052004/Nishant052004.git

echo.
echo Pushing to https://github.com/Nishant052004/Nishant052004.git ...
echo (Make sure you have created the public repo Nishant052004/Nishant052004 on GitHub first!)
echo.

git push -u origin main

echo.
echo ========================================================
echo   Done! Check your profile at https://github.com/Nishant052004
echo ========================================================
pause
