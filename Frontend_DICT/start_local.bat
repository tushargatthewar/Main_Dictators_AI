@echo off
echo ==========================================
echo   DICTATOR AI MIDDLEWARE - LOCAL LAUNCH
echo ==========================================

echo [1/2] Starting Backend Server (Port 5000)...
start "Backend Server" cmd /k "python server.py"

echo [2/2] Starting Frontend App (Port 5173)...
REM Using call to ensure npm runs correctly in batch
start "Frontend App" cmd /k "npm run dev"

echo.
echo Both servers are starting!
echo Once ready, open your browser to: http://localhost:5173
echo.
pause
