from dao.db_config import get_connection


class AlunoDAO:

    def listar_alunos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, idade, cidade FROM aluno")
        lista = cursor.fetchall()

        conn.close()

        return lista

    def salvar(self, id, nome, idade, cidade):
        conn = get_connection()
        cursor = conn.cursor()
        try:
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