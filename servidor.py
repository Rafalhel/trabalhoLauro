import calendar
import os
from datetime import datetime, date

from flask import Flask, render_template, request
from classes import Tempo

diretorio = os.getcwd().split('\\')[-1]
app = Flask(__name__, static_folder=f"../{diretorio}", template_folder=f"../{diretorio}")

@app.route('/', methods=["POST", "GET"])
def index():

    cidade = request.form.get('tempo')
    if cidade == None:
        cidade = 'São Paulo'
    temperatura = Tempo(cidade)

    temperaturaSemanal = temperatura.tempoSemana()
    temperaturaAtual = temperatura.tempoAtualCelcius()

    try:
        for i in temperaturaSemanal[0]:
            data = datetime.strptime(i, '%Y-%m-%d').date()
            temperaturaSemanal[0][i].append(calendar.day_name[data.weekday()])
    except:
        ...

    dataAtual = str(datetime.now()).split(' ')[0]
    if dataAtual in temperaturaSemanal[0]:
        del temperaturaSemanal[0][dataAtual]
        del temperaturaSemanal[1][dataAtual]

    diaSemanaAtual = calendar.day_name[date.today().weekday()]
    mesAtual = datetime.today().strftime("%b")
    anoAtual = datetime.today().strftime("%Y")
    diaAtual = date.today().day
    cidade = temperatura.cidade

    return render_template('index.html', cidade = cidade, temperaturaAtual=temperaturaAtual[0], idAtual = temperaturaAtual[1],
                           temperaturaSemanal = temperaturaSemanal[0],id = temperaturaSemanal[1], diaSemana = diaSemanaAtual, diaAtual = diaAtual,
                           mesAtual = mesAtual, projeto = diretorio, anoAtual=anoAtual)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', debug=False, port=5000)