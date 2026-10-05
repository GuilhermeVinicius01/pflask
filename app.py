from flask import Flask, render_template, request

from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO


app = Flask(__name__)


aluno_dao = AlunoDAO()
professor_dao = ProfessorDAO()
turma_dao = TurmaDAO()


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')

@app.route('/contato')
def contato_dev():
    return render_template('dashboard/contato.html')

@app.route('/aluno')
def listar_aluno():
    lista = aluno_dao.listar_alunos()
    return render_template('aluno/lista.html',lista=lista)

@app.route('/professor')
def listar_professor():
    lista = professor_dao.listar_professores()
    return render_template('professor/lista.html',lista=lista)

@app.route('/turma')
def listar_turma():
    lista = turma_dao.listar_turmas()
    return render_template('turma/lista.html',lista=lista)

@app.route('/exercicios')
def menu_exercicios():
    return render_template('saudacao/menu.html')


@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return f'Olá, {nome}! Seja bem-vindo ao sistema.'


@app.route('/saudacao2/')
def saudacao2():
    return render_template('saudacao/saudacao.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

    return f'Usuário: {usuario} | Senha: {senha}'

    return render_template('saudacao/login.html')

@app.route('/desafio', methods=['GET', 'POST'])
def desafio():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        cpf = request.form['cpf']
        nome_mae = request.form['nome_mae']
        return render_template('saudacao/resultado.html', nome=nome, data_nascimento=data_nascimento, cpf=cpf, nome_mae=nome_mae)

    return render_template('saudacao/desafio.html')

if __name__ == '__main__':
    app.run(debug=True)