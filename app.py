import os

from flask import Flask, render_template, request, redirect, flash

from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO


app = Flask(__name__)
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

@app.route('/aluno')
def listar_aluno():
    lista = aluno_dao.listar_alunos()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html', aluno=(None, '', '', ''))

@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    aluno = aluno_dao.buscar_por_id(id)
    if aluno is None:
        flash("Aluno não encontrado.", "danger")
        return redirect('/aluno')
    return render_template('aluno/form.html', aluno=aluno)

@app.route('/aluno/salvar/', methods=['POST'])
def salvar_aluno():
    id = request.form.get('id') or None
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    result = aluno_dao.salvar(id, nome, idade, cidade)

    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')

@app.route('/professor')
def listar_professor():
    lista = professor_dao.listar_professores()
    return render_template('professor/lista.html', lista=lista)

@app.route('/professor/form')
def form_professor():
    return render_template('professor/form.html', professor=(None, '', ''))

@app.route('/professor/editar/<int:id>')
def editar_professor(id):
    professor = professor_dao.buscar_por_id(id)
    if professor is None:
        flash("Professor não encontrado.", "danger")
        return redirect('/professor')
    return render_template('professor/form.html', professor=professor)

@app.route('/professor/salvar/', methods=['POST'])
def salvar_professor():
    id = request.form.get('id') or None
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    result = professor_dao.salvar(id, nome, disciplina)

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')

@app.route('/curso')
def listar_curso():
    lista = curso_dao.listar_cursos()
    return render_template('curso/lista.html', lista=lista)

@app.route('/curso/form')
def form_curso():
    return render_template('curso/form.html', curso=(None, '', ''))

@app.route('/curso/editar/<int:id>')
def editar_curso(id):
    curso = curso_dao.buscar_por_id(id)
    if curso is None:
        flash("Curso não encontrado.", "danger")
        return redirect('/curso')
    return render_template('curso/form.html', curso=curso)

@app.route('/curso/salvar/', methods=['POST'])
def salvar_curso():
    id = request.form.get('id') or None
    nome_curso = request.form['nome_curso']
    duracao = request.form['duracao']
    result = curso_dao.salvar(id, nome_curso, duracao)

    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')

@app.route('/turma')
def listar_turma():
    lista = turma_dao.listar_turmas()
    return render_template('turma/lista.html', lista=lista)

@app.route('/turma/form')
def form_turma():
    return render_template(
        'turma/form.html',
        turma=(None, '', None, None),
        cursos=curso_dao.listar_cursos(),
        professores=professor_dao.listar_professores()
    )

@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    turma = turma_dao.buscar_por_id(id)
    if turma is None:
        flash("Turma não encontrada.", "danger")
        return redirect('/turma')
    return render_template(
        'turma/form.html',
        turma=turma,
        cursos=curso_dao.listar_cursos(),
        professores=professor_dao.listar_professores()
    )

@app.route('/turma/salvar/', methods=['POST'])
def salvar_turma():
    id = request.form.get('id') or None
    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']
    result = turma_dao.salvar(id, semestre, curso_id, professor_id)

    if result["status"] == "ok":
        flash("Turma salva com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/turma')

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