@echo off
echo Activating virtual environment...
call .\venv\Scripts\activate.bat

echo Running Python script...
python .\main.py

echo Deactivating virtual environment...
call deactivate.bat

echo Done.
pause
