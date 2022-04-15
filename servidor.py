import calendar
import os
from datetime import datetime, date

from flask import Flask, render_template, request, url_for, redirect
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

    # else:
    #     cidade = None
    #     temperaturaSemanal = None
    #     temperaturaAtual = None
    # print(temperaturaAtual)
    # print(temperaturaSemanal)
    # print(cidade)

    try:
        for i in temperaturaSemanal[0]:
            data = datetime.strptime(i, '%Y-%m-%d').date()
            temperaturaSemanal[0][i].append(calendar.day_name[data.weekday()])
    except:
        ...

    diaSemanaAtual = calendar.day_name[date.today().weekday()]
    mesAtual = datetime.today().strftime("%b")
    diaAtual = date.today().day

    return render_template('index.html', cidade = cidade, temperaturaAtual=temperaturaAtual[0], idAtual = temperaturaAtual[1],
                           temperaturaSemanal = temperaturaSemanal[0],id = temperaturaSemanal[1], diaSemana = diaSemanaAtual, diaAtual = diaAtual,
                           mesAtual = mesAtual, projeto = diretorio)

@app.route('/2', methods=["POST", "GET"])
def index2():

    cidade = request.form.get('tempo')
    if cidade != None:
        temperatura = Tempo(cidade)

        temperaturaAtual = temperatura.tempoAtualCelcius()
        try:
            temperaturaAtual = int(temperaturaAtual)
        except:
            temperaturaAtual = None
    else:
        cidade = None
        temperaturaAtual= None

    return render_template('index2.html', temperatura=temperaturaAtual, cidade = cidade)



if __name__ == '__main__':
    from waitress import serve
    # serve(app, host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', debug=True, port=5000)