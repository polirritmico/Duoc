from flask import Flask

app = Flask(__name__)


@app.route("/a")
def a():
    return "Respuesta desde servicio A\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
