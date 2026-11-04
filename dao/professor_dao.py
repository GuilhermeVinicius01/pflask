from dao.db_config import get_connection


class ProfessorDAO:

    def listar_professores(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, disciplina FROM professor ORDER BY id")
            return cursor.fetchall()
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, disciplina FROM professor WHERE id = %s", (id,))
            return cursor.fetchone()
        finally:
            conn.close()

    def salvar(self, id, nome, disciplina):
        """Se id for None faz INSERT, senão faz UPDATE."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if id:
                cursor.execute(
                    'UPDATE professor SET nome = %s, disciplina = %s WHERE id = %s',
                    (nome, disciplina, id)
                )
            else:
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

    def remover(self, id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM professor WHERE id = %s", (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": "Não foi possível remover o professor. Ele pode estar vinculado a uma turma."}
        finally:
            conn.close()