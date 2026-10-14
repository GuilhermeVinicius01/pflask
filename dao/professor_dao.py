from dao.db_config import get_connection


class ProfessorDAO:

    def listar_professores(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, disciplina FROM professor")
        lista = cursor.fetchall()

        conn.close()

        return lista

    def salvar(self, id, nome, disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO professor (nome, disciplina) VALUES (%s, %s)',
                (nome, disciplina)
            )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()