#!/bin/bash

# текущая директория
projectPath=$(pwd)

# венв
if [ ! -d "$projectPath/venv" ]; then
    python3 -m venv "$projectPath/venv"
fi

# активируем венв
source "$projectPath/venv/bin/activate"

# зависимости
pip install -r "$projectPath/requirements.txt"

# сервер
cd "$projectPath/server" || exit
export FLASK_APP=app.py
flask run &

# бот
cd "$projectPath/bot" || exit


python main.py
