from dao.db_config import get_connection


class TurmaDAO:

    def listar_turmas(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT turma.id, turma.semestre, curso.nome_curso, professor.nome
                FROM turma
                JOIN curso ON curso.id = turma.curso_id
                JOIN professor ON professor.id = turma.professor_id
                ORDER BY turma.id
            """)
            return cursor.fetchall()
        finally:
            conn.close()

    def buscar_por_id(self, id):
        """Retorna (id, semestre, curso_id, professor_id)."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, semestre, curso_id, professor_id FROM turma WHERE id = %s",
                (id,)
            )
            return cursor.fetchone()
        finally:
            conn.close()

    def salvar(self, id, semestre, curso_id, professor_id):
        """Se id for None faz INSERT, senão faz UPDATE."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if id:
                cursor.execute(
                    "UPDATE turma SET semestre = %s, curso_id = %s, professor_id = %s WHERE id = %s",
                    (semestre, curso_id, professor_id, id)
                )
            else:
                cursor.execute(
                    "INSERT INTO turma (semestre, curso_id, professor_id) VALUES (%s, %s, %s)",
                    (semestre, curso_id, professor_id)
                )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Erro ao salvar turma: {str(e)}"}
        finally:
            conn.close()

    def remover(self, id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM turma WHERE id = %s", (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Não foi possível remover a turma: {str(e)}"}
        finally:
            conn.close()