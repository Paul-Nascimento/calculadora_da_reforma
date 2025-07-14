
from flask import Flask, render_template, request
from typing import Dict

# Dicionário de faixas por Anexo com alíquota nominal (%) e parcela a deduzir (R$)
tabela_simples = {
    'I': {
        1: {'aliquota': 0.04,   'deducao': 0.00,         "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,     "cpp":0.415,"iss":0.0,"icms":0.34, 'ipi':0.0},
        2: {'aliquota': 0.073,  'deducao': 5_940.00,     "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,     "cpp":0.415,"iss":0.0,"icms":0.34, 'ipi':0.0},
        3: {'aliquota': 0.095,  'deducao': 13_860.00,    "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,    "cpp":0.42,"iss":0.0,"icms":0.345, 'ipi':0.0},
        4: {'aliquota': 0.1070, 'deducao': 22_500.00,    "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,    "cpp":0.42,"iss":0.0,"icms":0.345, 'ipi':0.0},
        5: {'aliquota': 0.1430, 'deducao': 87_300.00,    "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,    "cpp":0.42,"iss":0.0,"icms":0.345, 'ipi':0.0},
        6: {'aliquota': 0.1900, 'deducao': 378_000.00,   "irpj":0.1350,  "csll":0.10,    "cofins":0.2827,    "pis":0.0613,     "cpp":0.421,"iss":0.0,"icms":0.0, 'ipi':0.0},
    },
    'II': {
        1: {'aliquota': 4.50,   'deducao': 0.00,            "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,     "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        2: {'aliquota': 7.80,   'deducao': 5_940.00,        "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,     "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        3: {'aliquota': 10.00,  'deducao': 13_860.00,       "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,     "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        4: {'aliquota': 11.20,  'deducao': 22_500.00,       "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,     "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        5: {'aliquota': 14.70,  'deducao': 85_500.00,       "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,     "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        6: {'aliquota': 30.00,  'deducao': 720_000.00,      "irpj":0.085,"csll":0.075,"cofins":0.2096,"pis":0.0454,     "cpp":0.235,"iss":0.0,"icms":0.00,  'ipi':0.35},
    },
    'III': {
        1: {'aliquota': 0.06,   'deducao': 0.00,            "irpj":0.04,    "csll":0.035,   "cofins":0.1282,"pis":0.0278,     "cpp":0.4340, "iss":0.335,    "icms":0.32, 'ipi':0.000},
        2: {'aliquota': 0.112,  'deducao': 5_940.00,        "irpj":0.04,    "csll":0.035,   "cofins":0.1405,"pis":0.0305,     "cpp":0.4340, "iss":0.32,     "icms":0.32, 'ipi':0.000},
        3: {'aliquota': 0.135,  'deducao': 13_860.00,       "irpj":0.04,    "csll":0.035,   "cofins":0.1364,"pis":0.0296,     "cpp":0.4340, "iss":0.3250,   "icms":0.32, 'ipi':0.000},
        4: {'aliquota': 0.16,   'deducao': 22_500.00,       "irpj":0.04,    "csll":0.035,   "cofins":0.1364,"pis":0.0296,     "cpp":0.4340, "iss":0.3250,   "icms":0.32, 'ipi':0.000},
        5: {'aliquota': 0.21,   'deducao': 87_300.00,       "irpj":0.04,    "csll":0.035,   "cofins":0.1282,"pis":0.0278,     "cpp":0.4340, "iss":0.3350,   "icms":0.32, 'ipi':0.000},
        6: {'aliquota': 0.33,   'deducao': 720_000.00,      "irpj":0.35,    "csll":0.15,    "cofins":0.1603,"pis":0.0347,     "cpp":0.3050, "iss":0.0,      "icms":0.00, 'ipi':0.00},
    },
    'IV': {
        1: {'aliquota': 0.045,   'deducao': 0.00,           "irpj":0.18,        "csll":0.1520,   "cofins":0.1767,   "pis":0.0383,     "cpp":0.0, "iss":0.4450,   "icms":0.0, 'ipi':0.000},
        2: {'aliquota': 0.090,  'deducao': 8_1.00,          "irpj":0.198,       "csll":0.1520,   "cofins":0.2055,   "pis":0.0445,     "cpp":0.0, "iss":0.4000,   "icms":0.0, 'ipi':0.000},
        3: {'aliquota': 0.102,  'deducao': 12_420.00,       "irpj":0.2080,      "csll":0.1920,   "cofins":0.1973,   "pis":0.0427,     "cpp":0.0, "iss":0.4000,   "icms":0.0, 'ipi':0.000},
        4: {'aliquota': 0.140,   'deducao': 39_780.00,      "irpj":0.1780,      "csll":0.1920,   "cofins":0.1890,   "pis":0.0410,     "cpp":0.0, "iss":0.4000,   "icms":0.0, 'ipi':0.000},
        5: {'aliquota': 0.220,   'deducao': 183_780.00,     "irpj":0.1880,      "csll":0.1920,   "cofins":0.1808,   "pis":0.0392,     "cpp":0.0, "iss":0.4000,   "icms":0.0, 'ipi':0.000},
        6: {'aliquota': 0.330,   'deducao': 828_000.00,     "irpj":0.5350,      "csll":0.2150,   "cofins":0.2055,   "pis":0.0445,     "cpp":0.0, "iss":0.0,      "icms":0.0, 'ipi':0.00},
    },
    'V': {
        1: {'aliquota': 0.1550,   'deducao': 0.00,           "irpj":0.25,      "csll":0.1500,   "cofins":0.1410,   "pis":0.0305,     "cpp":0.2885, "iss":0.1400,   "icms":0.0, 'ipi':0.000},
        2: {'aliquota': 0.1800,   'deducao': 4500.00,        "irpj":0.23,      "csll":0.1500,   "cofins":0.1410,   "pis":0.0305,     "cpp":0.2785, "iss":0.1700,   "icms":0.0, 'ipi':0.000},
        3: {'aliquota': 0.1950,   'deducao': 9_900.00,       "irpj":0.24,      "csll":0.1500,   "cofins":0.1492,   "pis":0.0323,     "cpp":0.2385, "iss":0.1900,   "icms":0.0, 'ipi':0.000},
        4: {'aliquota': 0.2050,   'deducao': 17_100.00,      "irpj":0.21,      "csll":0.1500,   "cofins":0.1574,   "pis":0.0341,     "cpp":0.2385, "iss":0.2100,   "icms":0.0, 'ipi':0.000},
        5: {'aliquota': 0.2300,   'deducao': 62_100.00,      "irpj":0.23,      "csll":0.1250,   "cofins":0.1410,   "pis":0.0305,     "cpp":0.2385, "iss":0.2350,   "icms":0.0, 'ipi':0.000},
        6: {'aliquota': 0.3050,   'deducao': 540_000.00,     "irpj":0.35,      "csll":0.1550,   "cofins":0.1644,   "pis":0.0356,     "cpp":0.2950, "iss":0.0,      "icms":0.0, 'ipi':0.00},
    },
}

ibs_cbs_simples_nacional = {
    #Basicamente, dado 
    2026: {
        "ibs": 0.0053,   # 1% de IBS (fase de teste)
        "cbs": 0.009   # 0,9% de CBS (fase de teste)
    },
    2027: {
        "ibs": 0.0053,   # alíquota de IBS em transição
        "cbs": 1.0   # CBS substitui integralmente PIS/Pasep + Cofins no Simples
    },
    2028: {
        "ibs": 0.0053,
        "cbs": 1
    },
    2029: {
        "ibs": 0.1096,
        "cbs": 1.0
    },
    2030: {
        "ibs": 0.2467,
        "cbs": 1
    },
    2031: {
        "ibs": 0.4229,
        "cbs": 1
    },
    2032: {
        "ibs": 0.6579,
        "cbs": 1
    },
    2033: {
        "ibs": 1,  # IBS substitui integralmente ICMS + ISS no Simples
        "cbs": 1
    }
}


def preco_sem_impostos(valor_da_nota,icms,credito_de_pis_e_cofins):
    return valor_da_nota - (valor_da_nota * icms) - (valor_da_nota * credito_de_pis_e_cofins)

def aliquota_icms(uf: str, ano: int) -> float:
    aliquotas_por_ano = {
        2026: {"PA": 0.19, "S_SE": 0.07, "N_NE_CO": 0.12},
        2027: {"PA": 0.19, "S_SE": 0.07, "N_NE_CO": 0.12},
        2028: {"PA": 0.19, "S_SE": 0.07, "N_NE_CO": 0.12},
        2029: {"PA": 0.1710, "S_SE": 0.0630, "N_NE_CO": 0.1080},
        2030: {"PA": 0.1520, "S_SE": 0.0560, "N_NE_CO": 0.0960},
        2031: {"PA": 0.1330, "S_SE": 0.0490, "N_NE_CO": 0.0840},
        2032: {"PA": 0.1140, "S_SE": 0.0420, "N_NE_CO": 0.0720},
        2033: {"PA": 0.00, "S_SE": 0.00, "N_NE_CO": 0.00},
    }

    regioes = {
        "PA": "PA",
        "AC": "N_NE_CO", "AP": "N_NE_CO", "AM": "N_NE_CO", "RR": "N_NE_CO", "RO": "N_NE_CO", "TO": "N_NE_CO",
        "MA": "N_NE_CO", "PI": "N_NE_CO", "CE": "N_NE_CO", "RN": "N_NE_CO", "PB": "N_NE_CO", "PE": "N_NE_CO",
        "AL": "N_NE_CO", "SE": "S_SE",    "BA": "N_NE_CO", "DF": "N_NE_CO", "GO": "N_NE_CO", "MT": "N_NE_CO",
        "MS": "N_NE_CO", "MG": "S_SE",    "ES": "S_SE",    "RJ": "S_SE",    "SP": "S_SE",    "PR": "S_SE",
        "SC": "S_SE",    "RS": "S_SE",
    }

    if ano not in aliquotas_por_ano:
        raise ValueError("Ano fora do intervalo permitido (2026 a 2033)")

    uf = uf.upper()
    if uf not in regioes:
        raise ValueError("UF inválida ou não reconhecida")

    grupo = regioes[uf]
    return aliquotas_por_ano[ano][grupo]

def aliquota_iss(ano: int) -> float:
    aliquotas = {
        2026: 0.05,
        2027: 0.05,
        2028: 0.05,
        2029: 0.045,
        2030: 0.04,
        2031: 0.035,
        2032: 0.03,
        2033: 0.00,
    }
    if ano not in aliquotas:
        raise ValueError("Ano fora do intervalo permitido (2026 a 2033)")
    return aliquotas[ano]

def aliquota_cbs(ano: int) -> float:
    aliquotas = {
        2026: 0.0000,
        2027: 0.0925,
        2028: 0.0925,
        2029: 0.0925,
        2030: 0.0925,
        2031: 0.0925,
        2032: 0.0925,
        2033: 0.0925,
    }
    if ano not in aliquotas:
        raise ValueError("Ano fora do intervalo permitido (2026 a 2033)")
    return aliquotas[ano]

def aliquota_ibs(ano: int) -> float:
    aliquotas = {
        2026: 0.0000,
        2027: 0.0010,
        2028: 0.0010,
        2029: 0.0188,
        2030: 0.0375,
        2031: 0.0563,
        2032: 0.0750,
        2033: 0.1875,
    }
    if ano not in aliquotas:
        raise ValueError("Ano fora do intervalo permitido (2026 a 2033)")
    return aliquotas[ano]

def aliquota_pis_cofins(ano):
    if ano == 2026:
        return 0.0925
    else:
        return 0.0

def calculadora_reforma_produto(preco_total,ano,uf,ibs_cbs_na_base=True):

    icms_aliquota = aliquota_icms(uf,ano)
    aliquota_estadual_pa = aliquota_icms('PA',ano)
    aliquota_icms_2026 = aliquota_icms(uf,2026)
    aliquota_pis_cofins_2026 = aliquota_pis_cofins(2026)

    iss_aliquota = aliquota_iss(ano)
    ibs_aliquota = aliquota_ibs(ano)
    cbs_aliquota = aliquota_cbs(ano)
    pis_cofins_aliquota = aliquota_pis_cofins(ano)

    p_sem_impostos = preco_sem_impostos(preco_total,aliquota_icms_2026,aliquota_pis_cofins_2026)  
    print(icms_aliquota,pis_cofins_aliquota)

    aliquota_preco_efetivo = 1 - aliquota_estadual_pa - pis_cofins_aliquota #Verificar qual aliquota de ICMS vai aqui

    ibs_valor = p_sem_impostos * ibs_aliquota
    cbs_valor = p_sem_impostos * cbs_aliquota
    pis_cofins_valor = preco_total * pis_cofins_aliquota

    print(p_sem_impostos,pis_cofins_valor,ibs_valor,cbs_valor)


    if ibs_cbs_na_base:
        base_de_calculo_icms = (p_sem_impostos / aliquota_preco_efetivo) + ibs_valor + cbs_valor
    else:
        base_de_calculo_icms = (p_sem_impostos / aliquota_preco_efetivo)
        
    print(base_de_calculo_icms)

    icms_valor = base_de_calculo_icms * icms_aliquota

    print(icms_valor)

    difal = (((base_de_calculo_icms - icms_valor)/(1 - aliquota_estadual_pa)) * aliquota_estadual_pa) - icms_valor  

    print(base_de_calculo_icms)
    print(f"IBS: {ibs_valor} | CBS: {cbs_valor} | ICMS: {icms_valor} | Preço sem impostos {p_sem_impostos} | PIS COFINS {pis_cofins_valor} | DIFAL {difal}")

    custo_nesa = p_sem_impostos + difal + icms_valor
    return {
        
        "IBS":ibs_valor,
        "CBS":cbs_valor,
        "ICMS":icms_valor,
        "Preço sem impostos":p_sem_impostos,
        "PIS_COFINS":pis_cofins_valor,
        "DIFAL":difal,
        "CUSTO NESA":custo_nesa
    }   

def calculadora_reforma_servico(preco_total,ano):
    #icms_aliquota = aliquota_icms(uf,ano)
    #aliquota_estadual_pa = aliquota_icms('PA',ano)
    #aliquota_icms_2026 = aliquota_icms(uf,2026)
    aliquota_pis_cofins_2026 = aliquota_pis_cofins(2026)
    iss_aliquota_2026 = 0.05

    iss_aliquota = aliquota_iss(ano)
    ibs_aliquota = aliquota_ibs(ano)
    cbs_aliquota = aliquota_cbs(ano)
    pis_cofins_aliquota = aliquota_pis_cofins(ano)

    p_sem_impostos = preco_total - (preco_total * iss_aliquota_2026) - (preco_total * aliquota_pis_cofins_2026)
    print(p_sem_impostos)
    aliquota_preco_efetivo = 1 - iss_aliquota - pis_cofins_aliquota 

    ibs_valor = p_sem_impostos * ibs_aliquota
    cbs_valor = p_sem_impostos * cbs_aliquota
    pis_cofins_valor = preco_total * pis_cofins_aliquota

    base_de_calculo_iss = (p_sem_impostos / aliquota_preco_efetivo) #+ ibs_valor + cbs_valor
    iss_valor = base_de_calculo_iss * iss_aliquota


    print(f"IBS: {ibs_valor} | CBS: {cbs_valor} | ISS: {iss_valor} | Preço sem impostos {p_sem_impostos} | PIS COFINS {pis_cofins_valor} ")

    custo_nesa = p_sem_impostos + iss_valor 
    return {
        "IBS":ibs_valor,
        "CBS":cbs_valor,
        "ISS":iss_valor,
        "Preço sem impostos":p_sem_impostos,
        "PIS_COFINS":pis_cofins_valor,
        "CUSTO NESA":custo_nesa
    }   

def faixa_simples_nacional(rbt12):
    """
    Retorna a faixa do Simples Nacional com base no RBT12 (receita bruta dos últimos 12 meses).
    """
    if rbt12 <= 180_000.00:
        return 1
    elif rbt12 <= 360_000.00:
        return 2
    elif rbt12 <= 720_000.00:
        return 3
    elif rbt12 <= 1_800_000.00:
        return 4
    elif rbt12 <= 3_600_000.00:
        return 5
    elif rbt12 <= 4_800_000.00:
        return 6
    else:
        return None  # Acima do teto do Simples Nacional

def apurar_simples_nacional(anexo: str,
                            rbt12: float,
                            faturamento: float) -> Dict[str, float]:
    """
    Calcula a apuração do Simples Nacional para um dado anexo e faixa.

    Args:
        anexo (str): Anexo do Simples Nacional (I, II, III, IV ou V).
        rbt12 (float): Receita Bruta Total dos últimos 12 meses.
        faturamento (float): Faturamento do mês de apuração.

    Returns:
        Dict[str, float]: Dicionário contendo todas as alíquotas efetivas
                          e os valores de cada tributo a recolher.

    Raises:
        ValueError: Se o anexo ou a faixa forem inválidos.
    """
    faixa = faixa_simples_nacional(rbt12)
    dados = tabela_simples.get(anexo, {}).get(faixa)

    if not dados:
        raise ValueError("Anexo ou faixa inválida.")

    aliquota = dados['aliquota']
    parcela_a_deduzir = dados['deducao']
    aliquota_efetiva = ((rbt12 * aliquota) - parcela_a_deduzir) / rbt12
    valor_a_pagar = faturamento * aliquota_efetiva

    # Calcula cada tributo
    iss   = valor_a_pagar * dados['iss']
    ipi   = valor_a_pagar * dados['ipi']
    pis   = valor_a_pagar * dados['pis']
    cofins = valor_a_pagar * dados['cofins']
    csll  = valor_a_pagar * dados['csll']
    cpp   = valor_a_pagar * dados['cpp']
    icms  = valor_a_pagar * dados['icms']
    irpj  = valor_a_pagar * dados['irpj']

    return {
        'aliquota_nominal'  : aliquota,
        'aliquota_efetiva'  : aliquota_efetiva,
        'valor_total'       : valor_a_pagar,
        'iss'               : iss,
        'ipi'               : ipi,
        'pis'               : pis,
        'cofins'            : cofins,
        'csll'              : csll,
        'cpp'               : cpp,
        'icms'              : icms,
        'irpj'              : irpj,
    }

def calcular_simples_comparativo(anexo: str, rbt12: float, faturamento: float, ano: int) -> Dict[str, float]:
    data = apurar_simples_nacional(anexo, rbt12, faturamento)

    valor_total = data['valor_total']
    preco_liquido = faturamento - valor_total

    pis = data['pis']
    cofins = data['cofins']
    icms = data['icms']
    iss = data['iss']

    # Percentuais de IBS/CBS vigentes para o ano informado
    ibs_percent = ibs_cbs_simples_nacional[ano]['ibs']
    cbs_percent = ibs_cbs_simples_nacional[ano]['cbs']

    # Créditos no regime do Simples Nacional
    credito_ibs_simples = (icms + iss) * ibs_percent
    credito_cbs_simples = (pis + cofins) * cbs_percent

    # Custo real no Simples Nacional (sem possibilidade de crédito cheio)
    custo_simples = faturamento - credito_cbs_simples - credito_ibs_simples

    return {
        'aliquota_efetiva': data['aliquota_efetiva'],
        'valor_pago_simples': valor_total,
        'preco_liquido': preco_liquido,

        'credito_ibs_simples': credito_ibs_simples,
        'credito_cbs_simples': credito_cbs_simples,
        'percentual_ibs_simples': ibs_percent,
        'percentual_cbs_simples': cbs_percent,

        'custo_efetivo_simples': custo_simples
    }


#s = calculadora_reforma_produto(1000,2026,'SP')
#print(s)

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
