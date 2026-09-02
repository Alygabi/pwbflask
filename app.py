from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')

@app.route('/alunos')
def lista_alunos():
    msg = 'a senha é semsenha!'
    return render_template('alunos/lista.html', texto=msg)

@app.route('/professores')
def lista_professores():
    msg = 'professor senha é semsenha!'
    return render_template('professores/lista.html', texto=msg)




if __name__ == '__main__':
    app.run(debug=True)

