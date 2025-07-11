

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

def calculadora_reforma_produto(preco_total,ano,uf):

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



    base_de_calculo_icms = (p_sem_impostos / aliquota_preco_efetivo) + ibs_valor + cbs_valor

    print(base_de_calculo_icms,aliquota_preco_efetivo)
    icms_valor = base_de_calculo_icms * icms_aliquota


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


s = calculadora_reforma_servico(1000,2031)
print(s)