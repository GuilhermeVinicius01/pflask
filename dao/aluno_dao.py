from dao.db_config import get_connection


class AlunoDAO:

    def listar_alunos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, idade, cidade FROM aluno")
        lista = cursor.fetchall()

        conn.close()

        return lista