from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')

@app.route('/alunos')
def listar_alunos():
    lista_alunos = [
        (1, 'Ana Beatriz Silva', 20, 'São Paulo'),
        (2, 'Carlos Eduardo Lima', 22, 'Rio de Janeiro'),
        (3, 'Mariana Souza', 19, 'Belo Horizonte'),
        (4, 'Lucas Pereira', 21, 'Brasília'),
        (5, 'Fernanda Oliveira', 23, 'Curitiba'),
        (6, 'Rafael Santos', 20, 'Porto Alegre'),
        (7, 'Juliana Costa', 22, 'Recife'),
        (8, 'Gabriel Almeida', 19, 'Fortaleza'),
        (9, 'Isabela Rodrigues', 21, 'Salvador'),
        (10, 'Thiago Martins', 23, 'Manaus')
    ]
    return render_template('alunos/lista.html', lista_alunos=lista_alunos)

@app.route('/professores')
def lista_professores():
    msg = 'professor senha é semsenha!'
    return render_template('professores/lista.html', texto=msg)




if __name__ == '__main__':
    app.run(debug=True)

