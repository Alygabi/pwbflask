from flask import Flask, render_template
from dao.aluno_dao import AlunoDAO
import sqlite3



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre') 
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)


@app.route('/professor')
def lista_professores():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, disciplina FROM professor")
    lista= cursor.fetchall()
    conn.close()
   
    return render_template('professor/lista.html', lista=lista)



@app.route('/turma')
def lista_turma():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("select turma.id, semestre, nome_curso, professor.nome from turma join curso on curso.id=turma.curso_id join professor on professor.id=turma.professor_id")
    lista= cursor.fetchall()
    conn.close()
    return render_template('turma/lista.html', lista=lista)


if __name__ == '__main__':
    app.run(debug=True)

