from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta para la sesión


# Lista de usuarios registrados (solo para propósitos de demostración)
usuarios_registrados = {
    "usuario1": "password1",
    "usuario2": "password2"
}

# Función para verificar las credenciales del usuario
def verificar_credenciales(usuario, contrasena):
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contrasena:
        return True
    return False

# Función para procesar la consulta del usuario y generar una respuesta
def procesar_consulta(consulta):
    # Procesar la consulta utilizando spaCy
    doc = nlp(consulta)
    
    # Buscar en la base de conocimientos la respuesta más relevante
    respuesta = base_conocimientos.get(consulta, "Lo siento, no tengo información sobre eso.")
    
    return respuesta

# Función principal del chat
def chat2():
    print("¡Bienvenido al chat de consultas legales!")
    print("Puedes hacerme cualquier pregunta sobre leyes y regulaciones.")
    
    # Bucle principal del chat
    while True:
        # Leer la consulta del usuario
        consulta_usuario = input("Tú: ")
        
        # Procesar la consulta y generar una respuesta
        respuesta = procesar_consulta(consulta_usuario)
        
        # Mostrar la respuesta al usuario
        print("Bot: " + respuesta)
        
        # Preguntar al usuario si desea hacer otra consulta
        continuar = input("¿Quieres hacer otra consulta? (sí/no): ")
        if continuar.lower() != "sí":
            break

# Decorador para proteger las rutas que requieren autenticación
def proteger_ruta(func):
    def wrapper(*args, **kwargs):
        if "usuario" in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return wrapper

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]
        if verificar_credenciales(usuario, contrasena):
            session["usuario"] = usuario
            return redirect(url_for("chat"))  # Redirige al chat después del inicio de sesión
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

# Ruta para manejar las consultas de los usuarios
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        # Obtener la consulta del usuario desde el formulario web
        consulta_usuario = request.form["consulta"]
        
        # Procesar la consulta y generar una respuesta
        respuesta = procesar_consulta(consulta_usuario)
        
        # Devolver la respuesta al cliente
        return render_template("index.html", respuesta=respuesta)
    
    # Si se accede a la página por primera vez, mostrar la interfaz de chat
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
