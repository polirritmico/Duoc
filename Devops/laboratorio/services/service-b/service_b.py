import requests
from flask import Flask

app = Flask(__name__)


@app.route("/b")
def b():
    try:
        resp = requests.get("http://service-a:5000/a", timeout=2)
        texto_a = resp.text
        return "Respuesta desde servicio B\n" + texto_a
    except Exception as e:
        texto_a = f"Error llamando a servicio A: {e}\n"
        return "Respuesta desde servicio B\n" + texto_a


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
