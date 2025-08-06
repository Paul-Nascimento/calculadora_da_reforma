import streamlit as st
from calculadora_v2 import *
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Calculadora Tributária", layout="wide")

st.title("🧮 Calculadora Tributária Comparativa")

regime = st.selectbox("Escolha o regime tributário:", 
                      ["Simples Nacional", "Lucro Presumido", "Lucro Real"],index=2)

total_nota = st.number_input("Valor total da nota fiscal (R$)", min_value=0.01, step=0.01,value=1000.00)

tipo = st.selectbox("Tipo da operação:", ["venda", "servico"])

if tipo == 'venda':
    uf_saida = st.selectbox("UF do fornecedor (saída):", 
                            ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", 
                             "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", 
                             "RO", "RR", "RS", "SC", "SE", "SP", "TO"],index=13)

    uf_entrada = st.selectbox("UF do cliente (entrada):", 
                              ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", 
                               "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", 
                               "RO", "RR", "RS", "SC", "SE", "SP", "TO"],index=13)

anos = list(range(2026, 2034))

if regime == "Simples Nacional":
    anexo = st.selectbox("Selecione o Anexo:", ["I", "II", "III", "IV", "V"])
    rbt12 = st.number_input("Informe o RBT12 (receita bruta 12 meses):", min_value=0.0, step=100.0,value=10000.00)
    credito = st.checkbox("Gerar crédito de PIS/COFINS?", value=True)

    if st.button("Calcular Simples Nacional (2026 a 2033)"):
        resultados = []
        for ano in anos:
            try:
                resultado = calcular_simples_comparativo(anexo, rbt12, total_nota, ano, credito_pis_cofins=credito)
                resultado["Ano"] = ano
                resultados.append(resultado)
            except:
                continue

        if resultados:
            df = pd.DataFrame(resultados)
            df = df[["Ano", "preco_liquido", "aliquota_efetiva", "valor_pago_simples",
                     "credito_cbs_simples", "credito_ibs_simples", "custo_efetivo_simples"]]
            df.columns = ["Ano", "Preço Líquido", "Alíquota Efetiva", "Valor Pago",
                          "Crédito CBS", "Crédito IBS", "Custo Efetivo"]

            st.subheader("📊 Tabela Comparativa: Simples Nacional (2026–2033)")
            st.dataframe(df.style.format({
                "Preço Líquido": "{:.2f}",
                "Alíquota Efetiva": "{:.2%}",
                "Valor Pago": "R$ {:.2f}",
                "Crédito CBS": "R$ {:.2f}",
                "Crédito IBS": "R$ {:.2f}",
                "Custo Efetivo": "R$ {:.2f}"
            }))

            col1, col2 = st.columns(2)

            with col1:
                fig1, ax1 = plt.subplots()
                ax1.plot(df["Ano"], df["Crédito CBS"], marker='o', label="Crédito CBS")
                ax1.plot(df["Ano"], df["Crédito IBS"], marker='s', label="Crédito IBS")
                valores = pd.concat([df["Crédito CBS"], df["Crédito IBS"]])
                min_val = valores.min()
                max_val = valores.max()
                margem = (max_val - min_val) * 0.1 if max_val != min_val else 1
                ax1.set_ylim(min_val - margem, max_val + margem)
                ax1.set_title("Créditos de IBS e CBS")
                ax1.set_xlabel("Ano")
                ax1.set_ylabel("Crédito (R$)")
                ax1.grid(True)
                ax1.legend()
                st.pyplot(fig1)

            with col2:
                fig2, ax2 = plt.subplots()
                ax2.plot(df["Ano"], df["Custo Efetivo"], marker='o', label="Custo Efetivo", linewidth=2)
                ax2.plot(df["Ano"], df["Preço Líquido"], marker='s', label="Preço Líquido", linestyle='--', linewidth=2)
                valores = pd.concat([df["Custo Efetivo"], df["Preço Líquido"]])
                min_val = valores.min()
                max_val = valores.max()
                margem = (max_val - min_val) * 0.1 if max_val != min_val else 1
                ax2.set_ylim(min_val - margem, max_val + margem)
                ax2.set_title("Custo Efetivo vs Preço Líquido")
                ax2.set_xlabel("Ano")
                ax2.set_ylabel("Valor (R$)")
                ax2.grid(True)
                ax2.legend()
                st.pyplot(fig2)

        else:
            st.warning("Não foi possível calcular os dados. Verifique os inputs.")

elif regime == "Lucro Presumido" or regime == "Lucro Real":
    max_value = 0.25 if tipo == 'venda' else 0.05
    aliquota = st.number_input("Alíquota ICMS/ISS", min_value=0.0, max_value=1.0, value=max_value)
    credito = st.checkbox("Gerar crédito de PIS/COFINS?", value=True)

    if st.button(f"Calcular para 2026 a 2033 ({regime})"):
        resultados = []
        for ano in anos:
            if regime == "Lucro Presumido":
                preco_liquido = get_preco_liquido_lucro_presumido(total_nota, aliquota, 0.0365, tipo)
                difal = get_difal_pa(preco_liquido, ano, uf_saida, uf_entrada) if tipo == "venda" else 0
                custo = calculadora_lucro_presumido(preco_liquido, ano, aliquota, difal, credito_pis_cofins=credito)
            else:
                preco_liquido = get_preco_liquido_lucro_real(total_nota, aliquota, 0.0925)
                difal = get_difal_pa(preco_liquido, ano, uf_saida, uf_entrada) if tipo == "venda" else 0
                custo = calculadora_lucro_real(preco_liquido, ano, aliquota, difal=difal, credito_pis_cofins=credito)
            resultados.append({
                "Ano": ano,
                "Preço Líquido": preco_liquido,
                "DIFAL": difal,
                "Custo Efetivo": custo
            })

        df = pd.DataFrame(resultados)
        st.subheader(f"Tabela Comparativa ({regime})")
        st.dataframe(df.style.format({"Preço Líquido": "R$ {:.2f}", "DIFAL": "R$ {:.2f}", "Custo Efetivo": "R$ {:.2f}"}))

        fig, ax = plt.subplots()
        ax.plot(df["Ano"], df["Custo Efetivo"], marker='o', label="Custo Efetivo", linewidth=2)
        ax.plot(df["Ano"], df["Preço Líquido"], marker='s', label="Preço Líquido", linestyle='--', linewidth=2)
        valores = pd.concat([df["Custo Efetivo"], df["Preço Líquido"]])
        min_val = valores.min()
        max_val = valores.max()
        margem = (max_val - min_val) * 0.1 if max_val != min_val else 1
        ax.set_ylim(min_val - margem, max_val + margem)
        ax.set_title(f"Custo Efetivo vs Preço Líquido ({regime})")
        ax.set_xlabel("Ano")
        ax.set_ylabel("Valor (R$)")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)