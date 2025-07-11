from flask import Flask, render_template, request
from utils.calculadoras import calculadora_reforma_produto, calculadora_reforma_servico

app = Flask(__name__)

# (Cole aqui todas as funções fornecidas na sua mensagem, incluindo calculadora_reforma_produto)
# A função calculadora_reforma_servico ainda será implementada

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    if request.method == "POST":
        valor = float(request.form["valor"])
        tipo = request.form["tipo"]
        uf = request.form.get("uf", "").upper()

        for ano in range(2026, 2034):
            if tipo == "produto":
                resultado = calculadora_reforma_produto(valor, ano, uf)
            elif tipo == "servico":
                resultado = calculadora_reforma_servico(valor, ano)
            else:
                resultado = {}

            resultado["ano"] = ano
            resultados.append(resultado)

    return render_template("index.html", resultados=resultados)

