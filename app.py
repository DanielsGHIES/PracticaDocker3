from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "1234"),
        database=os.environ.get("DB_NAME", "login_db"),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email=%s AND password=%s"
            cursor.execute(sql, (email, password))
            user = cursor.fetchone()
        connection.close()

        if user:
            return "", 200  # Código 200 indica login correcto
        else:
            return "Correo o contraseña incorrectos", 401


    except Exception as e:
        return f"Error de conexión a la base de datos: {str(e)}", 500

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
