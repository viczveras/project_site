from flask import Flask, render_template

app = Flask(__name__)

#atribui uma funcionalidade na função home
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/perfil')
def perfil():
    return 'Perfil do usuário'
if __name__ == '__main__':
    app.run(debug=True)