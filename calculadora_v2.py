from typing import Dict

# Dicionário de faixas por Anexo com alíquota nominal (%) e parcela a deduzir (R$)
tabela_simples = {
    'I': {
        1: {'aliquota': 0.04,   'deducao': 0.00,         "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,      "cpp":0.415,"iss":0.0,"icms":0.34, 'ipi':0.0},
        2: {'aliquota': 0.073,  'deducao': 5_940.00,     "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,      "cpp":0.415,"iss":0.0,"icms":0.34, 'ipi':0.0},
        3: {'aliquota': 0.095,  'deducao': 13_860.00,    "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,      "cpp":0.42,"iss":0.0,"icms":0.345, 'ipi':0.0},
        4: {'aliquota': 0.1070, 'deducao': 22_500.00,    "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,      "cpp":0.42,"iss":0.0,"icms":0.345, 'ipi':0.0},
        5: {'aliquota': 0.1430, 'deducao': 87_300.00,    "irpj":0.055,   "csll":0.035,   "cofins":0.1274,    "pis":0.0276,      "cpp":0.42,"iss":0.0,"icms":0.345, 'ipi':0.0},
        6: {'aliquota': 0.1900, 'deducao': 378_000.00,   "irpj":0.1350,  "csll":0.10,    "cofins":0.2827,    "pis":0.0613,      "cpp":0.421,"iss":0.0,"icms":0.0, 'ipi':0.0},
    },
    'II': {
        1: {'aliquota': 4.50,   'deducao': 0.00,            "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,             "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        2: {'aliquota': 7.80,   'deducao': 5_940.00,        "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,             "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        3: {'aliquota': 10.00,  'deducao': 13_860.00,       "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,             "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        4: {'aliquota': 11.20,  'deducao': 22_500.00,       "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,             "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        5: {'aliquota': 14.70,  'deducao': 85_500.00,       "irpj":0.055,"csll":0.035,"cofins":0.1151,"pis":0.0249,             "cpp":0.375,"iss":0.0,"icms":0.32, 'ipi':0.075},
        6: {'aliquota': 30.00,  'deducao': 720_000.00,      "irpj":0.085,"csll":0.075,"cofins":0.2096,"pis":0.0454,             "cpp":0.235,"iss":0.0,"icms":0.00,  'ipi':0.35},
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


def get_percentual_efetivo(ano):
    data = {
        "2026":1,
        "2027":1,
        "2028":1,
        "2029":0.9,
        "2030":0.8,
        "2031":0.7,
        "2032":0.6,
        "2033":0
    }

    return data[str(ano)]

def get_aliquota_cbs(ano: int) -> float:
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

def get_aliquota_ibs(ano: int) -> float:
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

def get_aliquota_pis_cofins(ano):
    if ano == 2026:
        return 0.0925
    else:
        return 0.0

def obter_aliquota_icms_pa(uf_vendedor: str,uf_tomador: str = "PA", ) -> float:
    # Definições básicas
    aliquota_interna = 0.19  # padrão para operações internas
    aliquota_12 = 0.12
    aliquota_7 = 0.07

    # Estados por região
    regioes = {
        "N": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
        "NE": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
        "CO": ["DF", "GO", "MT", "MS"],
        "SE": ["ES", "MG", "RJ", "SP"],
        "S": ["PR", "RS", "SC"]
    }

    def get_regiao(uf):
        for regiao, estados in regioes.items():
            if uf in estados:
                return regiao
        return None

    regiao_tomador = get_regiao(uf_tomador.upper())
    regiao_vendedor = get_regiao(uf_vendedor.upper())

    # Caso não encontre a região
    if not regiao_tomador or not regiao_vendedor:
        raise ValueError("UF inválida ou não encontrada.")

    # Operação interna
    if uf_tomador == uf_vendedor:
        return aliquota_interna

    # Operação interestadual
    # Regra básica: Sul/Sudeste -> Norte/Nordeste/CO = 7%
    if regiao_vendedor in ["S", "SE"] and regiao_tomador in ["N", "NE", "CO"]:
        return aliquota_7
    # Regra inversa: Norte/Nordeste/CO -> Sul/Sudeste = 12%
    elif regiao_tomador in ["S", "SE"] and regiao_vendedor in ["N", "NE", "CO"]:
        return aliquota_12
    else:
        # Operações entre regiões similares (N x N, SE x SE, etc.) = 12%
        return aliquota_12

def get_difal_pa(preco_liquido,ano,uf_saida,uf_entrada,ibs_cbs_na_base=False):
    #Dado um determinado preco liquido, o objetivo é retornar o custo efetivo ou ganho efetivo em uma determinada operação
    #Preço liquido é o valor deduzidos os impostos pagos
    
    #Recupera a aliquota com base no estado do fornecedor
    aliquota = obter_aliquota_icms_pa(uf_vendedor=uf_saida,uf_tomador=uf_entrada)

    aliquota_pis_cofins = 0.0925 if ano <= 2026 else 0
    percentual_efetivo = get_percentual_efetivo(ano)
    aliquota_efetiva = aliquota * percentual_efetivo

    #Se tiver IBS e CBS na base, ela integra o bc_tributo no numerador    
    bc_tributo = (preco_liquido) / (1 - aliquota_efetiva - aliquota_pis_cofins)
    tributo_efetivo = bc_tributo * aliquota_efetiva

    print(f'Tributo efetivo: {tributo_efetivo} - BC TRIBUTO {bc_tributo}')
    
    difal_efetivo = ((bc_tributo - tributo_efetivo) / (1 - (0.19 * percentual_efetivo))) * (0.19 * percentual_efetivo) - tributo_efetivo
    
    return difal_efetivo

def get_preco_liquido_lucro_real(valor_total,aliquota_tributo,aliquota_pis_cofins):
    tributo_efetivo = valor_total * aliquota_tributo
    pis_cofins_efetivo = valor_total * aliquota_pis_cofins

    preco_liquido = valor_total - tributo_efetivo - pis_cofins_efetivo

    return preco_liquido

def calculadora_lucro_real(preco_liquido,ano,aliquota,difal=0,credito_pis_cofins=False,ibs_cbs_na_base=False):
    #Dado um determinado preco liquido, o objetivo é retornar o custo efetivo ou ganho efetivo em uma determinada operação
    #Preço liquido é o valor deduzidos os impostos pagos
    
    aliquota_pis_cofins = 0.0925 if ano <= 2026 else 0
    
    percentual_efetivo = get_percentual_efetivo(ano)
    aliquota_efetiva = aliquota * percentual_efetivo
    
    #Se tiver IBS e CBS na base, ela integra o bc_tributo no numerador    
    bc_tributo = (preco_liquido) / (1 - aliquota_efetiva - aliquota_pis_cofins)
    
    tributo_efetivo = bc_tributo * aliquota_efetiva

    #difal_efetivo = ((bc_tributo - tributo_efetivo) / (1 - 0.19)) * 0.19 - tributo_efetivo if difal else 0
    pis_cofins_efetivo = bc_tributo * aliquota_pis_cofins
    print(f'BC TRIBUTO LR {bc_tributo} - TRIBUTO {tributo_efetivo} - DIFAL {difal} - CREDITO PIS COFINS {credito_pis_cofins} - pis cofins {pis_cofins_efetivo}')
    
    if not credito_pis_cofins:
        custo = preco_liquido + tributo_efetivo + difal + pis_cofins_efetivo
    else:
        custo = preco_liquido + tributo_efetivo + difal
    
    return custo

def get_preco_liquido_lucro_presumido(valor_total,aliquota_tributo,aliquota_pis_cofins,tipo):
    tributo_efetivo = valor_total * aliquota_tributo
    pis_cofins_efetivo = (valor_total - tributo_efetivo) * aliquota_pis_cofins
    aliquota_irpj = 0.15
    aliquota_csll = 0.09

    if tipo == 'servico':
        base_presumida = 0.32

    elif tipo == 'venda':
        base_presumida = 0.08
    else:
        base_presumida = 0.12
    
    irpj = valor_total * base_presumida * aliquota_irpj
    csll = valor_total * base_presumida * aliquota_csll

    preco_liquido = valor_total - tributo_efetivo - pis_cofins_efetivo - irpj - csll

    return preco_liquido

def calculadora_lucro_presumido(preco_liquido,ano,aliquota,difal,credito_pis_cofins=False,ibs_cbs_na_base=False):
    #Dado um determinado preco liquido, o objetivo é retornar o custo efetivo ou ganho efetivo em uma determinada operação
    #Preço liquido é o valor deduzidos os impostos pagos
    
    aliquota_pis_cofins = 0.0365 if ano <= 2026 else 0
    aliquota_pis_cofins_credito = 0.0925 if ano <= 2026 else 0
    
    percentual_efetivo = get_percentual_efetivo(ano)
    aliquota_efetiva = aliquota * percentual_efetivo
    
    aliquota_irpj = 0.08 * 0.15
    aliquota_csll = 0.08 * 0.09
    #Se tiver IBS e CBS na base, ela integra o bc_tributo no numerador    
    bc_tributo = (preco_liquido) / (1 - aliquota_efetiva - aliquota_pis_cofins - aliquota_csll - aliquota_irpj)

    tributo_efetivo = bc_tributo * aliquota_efetiva
    pis_cofins_efetivo = bc_tributo * aliquota_pis_cofins
    irpj_efetivo = aliquota_irpj * bc_tributo
    csll_efetivo = aliquota_csll * bc_tributo
    valor_credito_pis_cofins = aliquota_pis_cofins_credito * bc_tributo

    print(f'IRPJ {irpj_efetivo} -  CSLL {csll_efetivo}')

    if credito_pis_cofins:
        custo = preco_liquido + tributo_efetivo + difal + irpj_efetivo + csll_efetivo + pis_cofins_efetivo - valor_credito_pis_cofins
    else:
        custo = preco_liquido + tributo_efetivo + difal + irpj_efetivo + csll_efetivo + pis_cofins_efetivo
    return custo


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

def calcular_simples_comparativo(anexo: str, rbt12: float, faturamento: float, ano: int,credito_pis_cofins:bool) -> Dict[str, float]:
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
    if credito_pis_cofins and ano <= 2026:
        valor_credito_pis_cofins = faturamento * 0.0925
    else:
        valor_credito_pis_cofins = 0

    custo_simples = faturamento - credito_cbs_simples - credito_ibs_simples - valor_credito_pis_cofins

    return {
        'aliquota_efetiva': data['aliquota_efetiva'],
        'valor_pago_simples': valor_total,
        'preco_liquido': preco_liquido,
        'credito_ibs_simples': credito_ibs_simples,
        'credito_cbs_simples': credito_cbs_simples,
        'percentual_ibs_simples': ibs_percent,
        'percentual_cbs_simples': cbs_percent,
        'preco_liquido':preco_liquido,
        'custo_efetivo_simples': custo_simples
    }

"""
if __name__ == "__main__":
    regime_tributario = 'lucro_presumido'
    if regime_tributario == 'lucro_real':
        aliquota = 0.05
        total_da_nota = 1000
        aliquota_pis_cofins = 0.0925
        tipo = 'serviço'
        ano = 2033
        uf_saida = 'PA'
        uf_entrada = 'PA'
        credito_pis_cofins = True

        preco_liquido = get_preco_liquido_lucro_real(total_da_nota,aliquota,aliquota_pis_cofins)
        print(f'O preço líquido é {preco_liquido}')
        
        
        if tipo == 'venda':
            difal = get_difal_pa(preco_liquido,ano,uf_saida,uf_entrada)
        else:
            difal = 0

        print(difal)
        data = calculadora_lucro_real(preco_liquido,ano,aliquota,credito_pis_cofins=False,difal=difal,credito_pis_cofins=credito_pis_cofins)
        print(data)

    elif regime_tributario == 'lucro_presumido':
        uf_saida = 'PA'
        uf_entrada = 'PA'

        aliquota = 0.19
        total_da_nota = 1000
        aliquota_pis_cofins = 0.0365
        tipo = 'venda'
        ano = 2033
        preco_liquido = get_preco_liquido_lucro_presumido(total_da_nota,aliquota,aliquota_pis_cofins,tipo=tipo)

        if tipo == 'venda':
            difal = get_difal_pa(preco_liquido,ano,uf_saida,uf_entrada)
        else:
            difal = 0
        c = calculadora_lucro_presumido(preco_liquido,ano,aliquota,difal)
        


    elif regime_tributario == 'simples_nacional':
        ...

    else:
        ...
        """