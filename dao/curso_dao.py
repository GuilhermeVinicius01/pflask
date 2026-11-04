from dao.db_config import get_connection


class CursoDAO:

    def listar_cursos(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome_curso, duracao FROM curso ORDER BY id")
            return cursor.fetchall()
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome_curso, duracao FROM curso WHERE id = %s", (id,))
            return cursor.fetchone()
        finally:
            conn.close()

    def salvar(self, id, nome_curso, duracao):
        """Se id for None faz INSERT, senão faz UPDATE."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if id:
                cursor.execute(
                    "UPDATE curso SET nome_curso = %s, duracao = %s WHERE id = %s",
                    (nome_curso, duracao, id)
                )
            else:
                cursor.execute(
                    "INSERT INTO curso (nome_curso, duracao) VALUES (%s, %s)",
                    (nome_curso, duracao)
                )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Erro ao salvar curso: {str(e)}"}
        finally:
            conn.close()

    def remover(self, id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM curso WHERE id = %s", (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": "Não foi possível remover o curso. Ele pode estar vinculado a uma turma."}
        finally:
            conn.close()