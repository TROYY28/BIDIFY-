@echo off
title BIDLIFY - Setup and Preview
cd /d "%~dp0"

echo.
echo === BIDLIFY Setup ===
echo.

where node >nul 2>&1
if errorlevel 1 (
  echo Node.js is NOT installed.
  echo.
  echo 1. Open https://nodejs.org in your browser
  echo 2. Download the LTS version and run the installer
  echo 3. Close this window, open a NEW terminal, and run this file again
  echo.
  start https://nodejs.org
  pause
  exit /b 1
)

echo Node: 
node -v
echo npm:
npm -v
echo.

echo Installing packages (first time may take 2-5 minutes)...
call npm install
if errorlevel 1 (
  echo npm install failed.
  pause
  exit /b 1
)

echo.
echo Creating database...
call npx prisma db push
if errorlevel 1 (
  echo prisma db push failed.
  pause
  exit /b 1
)

echo.
echo Starting preview at http://localhost:3000
echo Keep this window open. Press Ctrl+C to stop.
echo.
start http://localhost:3000
call npm run dev

pause
