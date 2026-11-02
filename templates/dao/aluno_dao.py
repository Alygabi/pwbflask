from dao.db_config import get_connection

class AlunoDAO:

    sqlSelectAll = "SELECT id, nome, idade, cidade FROM aluno"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelectAll)
        lista = cursor.fetchall()
        conn.close()
        return lista