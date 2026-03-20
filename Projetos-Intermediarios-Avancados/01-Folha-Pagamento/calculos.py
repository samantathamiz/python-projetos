# Cálculo de salário com descontos

def calcular_imposto_talisma(salario_bruto):
    return salario_bruto * 0.11  # Mantém 11%

def calcular_imposto_mistico(salario_base):
    if salario_base <= 5000:
        return 0.0
    elif salario_base <= 7000:
        return salario_base * 0.075
    else:
        return salario_base * 0.15

def calcular_salario_liquido(salario_bruto):
    """Calcula salário líquido considerando Imposto Talismã e Imposto Místico"""
    imposto_talisma = calcular_imposto_talisma(salario_bruto)
    base_mistico = salario_bruto - imposto_talisma
    imposto_mistico = calcular_imposto_mistico(base_mistico)
    liquido = salario_bruto - imposto_talisma - imposto_mistico
    return {
        "salario_bruto": salario_bruto,
        "imposto_talisma": imposto_talisma,
        "imposto_mistico": imposto_mistico,
        "salario_liquido": liquido
    }
