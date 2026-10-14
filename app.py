import os

from flask import Flask, render_template, request, redirect, flash

from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO


app = Flask(__name__)

# Chave usada pelo Flask para assinar a sessão (necessária para flash()).
# Em produção, defina a variável de ambiente SECRET_KEY na Vercel.
app.secret_key = os.environ.get("SECRET_KEY", "chave-secreta-de-desenvolvimento")


aluno_dao = AlunoDAO()
professor_dao = ProfessorDAO()
curso_dao = CursoDAO()
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


# ---------------- ALUNO ----------------
@app.route('/aluno')
def listar_aluno():
    lista = aluno_dao.listar_alunos()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/aluno/form')
def form_aluno():
    # tupla vazia: (id, nome, idade, cidade)
    return render_template('aluno/form.html', aluno=(None, '', '', ''))

@app.route('/aluno/salvar/', methods=['POST'])
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    result = aluno_dao.salvar(id, nome, idade, cidade)

    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')


# ---------------- PROFESSOR ----------------
@app.route('/professor')
def listar_professor():
    lista = professor_dao.listar_professores()
    return render_template('professor/lista.html', lista=lista)

@app.route('/professor/form')
def form_professor():
    # (id, nome, disciplina)
    return render_template('professor/form.html', professor=(None, '', ''))

@app.route('/professor/salvar/', methods=['POST'])
def salvar_professor(id=None):
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    result = professor_dao.salvar(id, nome, disciplina)

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')


# ---------------- CURSO ----------------
@app.route('/curso')
def listar_curso():
    lista = curso_dao.listar_cursos()
    return render_template('curso/lista.html', lista=lista)

@app.route('/curso/form')
def form_curso():
    # (id, nome_curso, duracao)
    return render_template('curso/form.html', curso=(None, '', ''))

@app.route('/curso/salvar/', methods=['POST'])
def salvar_curso(id=None):
    nome_curso = request.form['nome_curso']
    duracao = request.form['duracao']
    result = curso_dao.salvar(id, nome_curso, duracao)

    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')


# ---------------- TURMA ----------------
@app.route('/turma')
def listar_turma():
    lista = turma_dao.listar_turmas()
    return render_template('turma/lista.html', lista=lista)


# ---------------- SAUDAÇÃO / DESAFIO ----------------
@app.route('/saudacao')
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