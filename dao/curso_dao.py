
from dao.db_config import get_connection


class CursoDAO:

    def listar_cursos(self):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, nome_curso, duracao FROM curso"
            )

            lista = cursor.fetchall()

            return lista

        finally:
            conn.close()

    def salvar(self, id, nome_curso, duracao):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO curso (nome_curso, duracao)
                VALUES (%s, %s)
                """,
                (nome_curso, duracao)
            )

            conn.commit()

            return {"status": "ok"}

        except Exception as e:
            conn.rollback()

            return {
                "status": "erro",
                "mensagem": f"Erro ao salvar curso: {str(e)}"
            }

        finally:
            conn.close()