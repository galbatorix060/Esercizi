from flask import Flask, render_template, request

utenti = [["mariorossi@gmail.com", "dsrfed12e28h501r", "pippo", '0'],["elenagialli@gmail.com", "abcdef12th501m", "coca", '0'],["giannabianchi@gmail.com", "bgfmjh90e26h501i", "lalalala", '0']]

api = Flask("__name__")

@api.route('/registrati', methods=['GET'])
def registrazioni():
    utente = []
    utente.append(request.args.get("mail"))
    utente.append(request.args.get("codfisc"))
    utente.append(request.args.get("password"))
    utente.append('0')
    if utente in utenti:
        return render_template('regOk.html')
    else:
        return render_template('regKo.html')
    

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

api.run(host="0.0.0.0", port=8085)