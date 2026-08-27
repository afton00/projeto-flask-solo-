from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Projeto Flask da Dupla</h1>
    <p>Nosso primeiro projeto com Flask, Git e GitHub!</p>
    <p>Projeto desenvolvido por nossa dupla.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)