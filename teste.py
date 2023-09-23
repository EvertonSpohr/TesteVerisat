from datetime import datetime

#classe que representa o registro contábil, com a informação da data do registro, conceito e valor do mesmo.
class RegistroContabil:
    def __init__(self, data, conceito, valor):
        self.data = data
        self.conceito = conceito
        self.valor = valor

#função para imprimir o balanço e demonstração, recebe uma lista de objetos RegistroContabil
def calcular_balanco_e_demonstracao(registros_contabeis):
    ativos_circulantes = 0
    ativos_fixos = 0
    passivos_circulantes = 0
    passivos_longo_prazo = 0
    receita_total = 0
    despesas_total = 0

    for registro in registros_contabeis:
        if registro.conceito == 'Ativo Circulante':
            ativos_circulantes += registro.valor
        elif registro.conceito == 'Ativo Fixo':
            ativos_fixos += registro.valor
        elif registro.conceito == 'Passivo Circulante':
            passivos_circulantes += registro.valor
        elif registro.conceito == 'Passivo Longo Prazo':
            passivos_longo_prazo += registro.valor
        elif registro.conceito == 'Receita':
            receita_total += registro.valor
        elif registro.conceito == 'Despesa':
            despesas_total += registro.valor

    lucro_liquido = receita_total - despesas_total

    datas = [registro.data for registro in registros_contabeis]
    datas_formatadas = [datetime.strptime(data, '%d/%m/%Y') for data in datas]

    data_inicial = min(datas_formatadas)
    data_final = max(datas_formatadas)

    print(f"Balanço Patrimonial do Período de  {data_inicial.strftime('%d/%m/%Y')}  até  {data_final.strftime('%d/%m/%Y')}")
    print("Ativos Circulantes: $", "{:.2f}".format(ativos_circulantes))
    print("Ativos Fixos: $", "{:.2f}".format(ativos_fixos))
    print("Passivos Circulantes: $", "{:.2f}".format(passivos_circulantes))
    print("Passivos de Longo Prazo: $", "{:.2f}".format(passivos_longo_prazo))

    print(f"\nDemonstração de Resultados do Período de  {data_inicial.strftime('%d/%m/%Y')}  até  {data_final.strftime('%d/%m/%Y')}")
    print("Receita Total: $", "{:.2f}".format(receita_total))
    print("Despesas Totais: $", "{:.2f}".format(despesas_total))
    print("Lucro Líquido: $", "{:.2f}".format(lucro_liquido))

    if passivos_circulantes != 0:
        liquidez_corrente = ativos_circulantes / passivos_circulantes
        print("\nÍndice de Liquidez Corrente:", "{:.3f}".format(liquidez_corrente))

    if receita_total != 0:
        margem_lucro = (lucro_liquido / receita_total) * 100
        print("Margem de Lucro Líquido (%):", "{:.2f}".format(margem_lucro))





# Exemplo de uso
registros_contabeis = [
    RegistroContabil('01/01/2023', 'Ativo Circulante', 10000.00),
    RegistroContabil('10/03/2023', 'Ativo Circulante', 1352.74),
    RegistroContabil('15/04/2023', 'Ativo Circulante', 15000.00),
    RegistroContabil('01/01/2023', 'Ativo Fixo', 200000.00),
    RegistroContabil('01/01/2023', 'Passivo Circulante', 30000.00),
    RegistroContabil('01/01/2023', 'Passivo Longo Prazo', 100000.00),
    RegistroContabil('01/01/2023', 'Receita', 80000.00),
    RegistroContabil('01/01/2023', 'Receita', 1358.54),
    RegistroContabil('01/01/2023', 'Receita', 8965.20),
    RegistroContabil('01/01/2023', 'Despesa', 40000.00),
    RegistroContabil('01/01/2023', 'Despesa', 300.00),
    RegistroContabil('01/01/2023', 'Despesa', 1589.50),

]

calcular_balanco_e_demonstracao(registros_contabeis)
