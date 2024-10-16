from flask import render_template, request, jsonify
from . import app
from .ml import processing


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/ml', methods=['GET', 'POST'])
def ml():
    text = request.form.get('text')

    response = processing(text)

    return jsonify({'msg': f'{response}'})

@app.route('/bot', methods=['GET', 'POST'])
def bot():
    if request.method == 'GET':
        msg = request.args.get('msg')
        try:
            response = processing(msg)
            return jsonify({'msg': response})
        except Exception as e:
            return jsonify({'msg': f'Ошибка - {e}'})

