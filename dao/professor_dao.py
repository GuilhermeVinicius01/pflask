from dao.db_config import get_connection


class ProfessorDAO:

    def listar_professores(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, nome, disciplina FROM professor"
        )

        lista = cursor.fetchall()

        conn.close()

        return lista