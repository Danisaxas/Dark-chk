import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página de inicio de sesión (login)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar el login (se puede personalizar más adelante)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Aquí puedes agregar la lógica para verificar las credenciales
    if username == "admin" and password == "1234":
        return redirect(url_for('home'))  # Redirige a la página de inicio si el login es exitoso
    else:
        return "Credenciales incorrectas, intenta de nuevo."

# Página principal después de login exitoso
@app.route('/home')
def home():
    return "Bienvenido a la página principal."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Heroku asigna un puerto automáticamente
    app.run(host="0.0.0.0", port=port)