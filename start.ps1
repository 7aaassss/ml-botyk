# текущую директорию
$projectPath = $PWD.Path

# создаем виртуальное окружение
if (-Not (Test-Path "$projectPath\venv")) {
    python -m venv "$projectPath\venv"
}

# активируем венв
& "$projectPath\venv\Scripts\Activate.ps1"

# зависимости
pip install -r "$projectPath\requirements.txt"

# сервер
Set-Location "$projectPath\server"
$env:FLASK_APP = "app.py"
Start-Process -NoNewWindow -File "flask" -ArgumentList "run"


Set-Location "$projectPath"

# бот
Set-Location "$projectPath\bot"
& "$projectPath\venv\Scripts\python.exe" "main.py"
