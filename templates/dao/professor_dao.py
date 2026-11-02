from dao.db_config import get_connection

class ProfessorDAO:

    sqlSelectAll = "SELECT id, nome, disciplina FROM professor"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelectAll)
        lista = cursor.fetchall()
        conn.close()
        return lista