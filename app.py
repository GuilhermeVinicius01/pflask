from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)