from dao.db_config import get_connection


class TurmaDAO:

    def listar_turmas(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""SELECT turma.id,semestre,nome_curso,professor.nome FROM turma JOIN curso ON curso.id = turma.curso_id JOIN professor ON professor.id = turma.professor_id """)
        lista = cursor.fetchall()

        conn.close()

        return lista