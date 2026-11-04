from dao.db_config import get_connection


class AlunoDAO:

    def listar_alunos(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, idade, cidade FROM aluno ORDER BY id")
            return cursor.fetchall()
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, idade, cidade FROM aluno WHERE id = %s", (id,))
            return cursor.fetchone()
        finally:
            conn.close()

    def salvar(self, id, nome, idade, cidade):
        """Se id for None faz INSERT, senão faz UPDATE."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if id:
                cursor.execute(
                    'UPDATE aluno SET nome = %s, idade = %s, cidade = %s WHERE id = %s',
                    (nome, idade, cidade, id)
                )
            else:
                cursor.execute(
                    'INSERT INTO aluno (nome, idade, cidade) VALUES (%s, %s, %s)',
                    (nome, idade, cidade)
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
            cursor.execute("DELETE FROM aluno WHERE id = %s", (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Não foi possível remover o aluno: {str(e)}"}
        finally:
            conn.close()