from flask import Flask, render_template
import sqlite3



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre') 
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')

@app.route('/alunos')
def listar_alunos():
    DB_PATH = "banco_escolar.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, idade, cidade FROM alunos")
    lista_alunos = cursor.fetchall()
    conn.close()


    return render_template('alunos/lista.html', lista_alunos=lista_alunos)

@app.route('/professores')
def lista_professores():
    lista_professores = [
        (1, 'Dr. João Silva', 'Matemática'),
        (2, 'Dra. Maria Oliveira', 'Física'),
        (3, 'Prof. Carlos Souza', 'Química'),
        (4, 'Dra. Ana Costa', 'Biologia'),
        (5, 'Prof. Pedro Lima', 'História')
    ]
    return render_template('professores/lista.html', lista_professores=lista_professores)




if __name__ == '__main__':
    app.run(debug=True)

