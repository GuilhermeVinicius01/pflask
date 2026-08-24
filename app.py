from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/sobre')
def sobre_o_sistema():
    return render_template ('sobre.html')

@app.route('/ajuda')
def ajuda():
    return render_template ('ajuda.html')


if __name__ == '__main__':
    app.run(debug=True)