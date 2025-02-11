from portfolio import app
from flask import Flask, render_template, send_file

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_pdf():
    caminho_pdf = 'curriculo.pdf'
    return send_file(caminho_pdf, as_attachment=True)

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')


