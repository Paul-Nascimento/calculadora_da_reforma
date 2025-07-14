
from flask import Flask, render_template, request
from utils.calculadoras import (
    calculadora_reforma_produto,
    calculadora_reforma_servico,
    calcular_simples_comparativo,
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    if request.method == "POST":
        valor = float(request.form["valor"])
        tipo = request.form["tipo"]
        uf = request.form.get("uf", "PA").upper()
        regime = request.form.get("regime", "")
        rbt12 = float(request.form.get("rbt12", "400000"))
        anexo = request.form.get("anexo", "III" if tipo == "servico" else "I")

        for ano in range(2026, 2034):
            if regime == "normal":
                if tipo == "produto":
                    resultado = calculadora_reforma_produto(valor, ano, uf)
                else:
                    resultado = calculadora_reforma_servico(valor, ano)
                resultado["ano"] = ano
            elif regime == "simples":
                comparativo = calcular_simples_comparativo(anexo, rbt12, valor, ano)

                # calcular custo no regime normal para comparação
                if tipo == "produto":
                    regime_normal = calculadora_reforma_produto(valor, ano, uf)
                else:
                    regime_normal = calculadora_reforma_servico(valor, ano)
                custo_normal = regime_normal["CUSTO NESA"]

                resultado = {
                    "ano": ano,
                    "IBS": comparativo["credito_ibs_simples"],
                    "CBS": comparativo["credito_cbs_simples"],
                    "ICMS": 0.0 if tipo == "servico" else 0.0,
                    "ISS": 0.0 if tipo == "produto" else 0.0,
                    "PIS_COFINS": 0.0,
                    "Preço sem impostos": comparativo["preco_liquido"],
                    "CUSTO NESA": comparativo["custo_efetivo_simples"],
                    "CUSTO REGULAR": custo_normal
                }
            resultados.append(resultado)

    return render_template("index.html", resultados=resultados)
