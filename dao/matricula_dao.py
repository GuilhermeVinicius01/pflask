from dao.db_config import get_connection


class MatriculaDAO:

    def listar_matriculas(self):
        """Retorna (id, semestre, aluno, curso, professor, disciplina)."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT matricula.id,
                       turma.semestre,
                       aluno.nome,
                       curso.nome_curso,
                       professor.nome,
                       professor.disciplina
                FROM matricula
                JOIN aluno ON aluno.id = matricula.aluno_id
                JOIN turma ON turma.id = matricula.turma_id
                JOIN curso ON curso.id = matricula.curso_id
                JOIN professor ON professor.id = turma.professor_id
                ORDER BY matricula.id DESC
            """)
            return cursor.fetchall()
        finally:
            conn.close()

    def buscar_por_id(self, id):
        """Retorna (id, aluno_id, turma_id)."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, aluno_id, turma_id FROM matricula WHERE id = %s",
                (id,)
            )
            return cursor.fetchone()
        finally:
            conn.close()

    def salvar(self, id, aluno_id, turma_id):
        """Se id for None faz INSERT, senão faz UPDATE.
        O curso da matrícula é o mesmo curso da turma escolhida."""
        conn = get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("SELECT curso_id FROM turma WHERE id = %s", (turma_id,))
            linha = cursor.fetchone()
            if linha is None:
                return {"status": "erro", "mensagem": "Turma não encontrada."}
            curso_id = linha[0]

            if id:
                cursor.execute(
                    "UPDATE matricula SET aluno_id = %s, curso_id = %s, turma_id = %s WHERE id = %s",
                    (aluno_id, curso_id, turma_id, id)
                )
            else:
                cursor.execute(
                    "INSERT INTO matricula (aluno_id, curso_id, turma_id) VALUES (%s, %s, %s)",
                    (aluno_id, curso_id, turma_id)
                )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Erro ao salvar matrícula: {str(e)}"}
        finally:
            conn.close()

    def remover(self, id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM matricula WHERE id = %s", (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Não foi possível remover a matrícula: {str(e)}"}
        finally:
            conn.close()