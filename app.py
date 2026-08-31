from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template ('dashboard/index.html')

@app.route('/sobre')
def sobre_o_sistema():
    return render_template ('dashboard/sobre.html')

@app.route('/contato')
def contato_dev():
    return render_template ('dashboard/contato.html')

@app.route('/aluno')
def lista_aluno():
    return render_template ('aluno/lista.html')

@app.route('/professor')
def lista_professor():
    return render_template ('proofessor/lista.html')


if __name__ == '__main__':
    app.run(debug=True)