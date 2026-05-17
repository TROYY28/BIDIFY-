@echo off
title BIDIFY - Setup and Preview
cd /d "%~dp0"
echo === BIDIFY Setup ===
echo.
where node >nul 2>&1
if errorlevel 1 (
  echo Node.js is NOT installed. Open https://nodejs.org and download LTS version.
  start https://nodejs.org
  pause
  exit /b 1
)
echo Node: & node -v & echo npm: & npm -v & echo.
echo Installing packages...
call npm install && call npx prisma db push && start http://localhost:3000 && call npm run dev
pause
