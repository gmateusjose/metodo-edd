# # Dados do exemplo fornecido
# dados = {
#     'prodA': {'processamento': 2, 'entrega': 21, 'adiantamento': 7, 'atraso': 6},
#     'prodB': {'processamento': 3, 'entrega': 9, 'adiantamento': 6, 'atraso': 1},
#     'prodC': {'processamento': 5, 'entrega': 6, 'adiantamento': 1, 'atraso': 8},
#     'prodD': {'processamento': 6, 'entrega': 8, 'adiantamento': 4, 'atraso': 9},
#     'prodE': {'processamento': 8, 'entrega': 4, 'adiantamento': 3, 'atraso': 3},
# }

# Dados do problema
dados = {
    'prod1': {'processamento': 10, 'entrega': 20, 'adiantamento': 0.20, 'atraso': 0.4},
    'prod2': {'processamento': 3, 'entrega': 98, 'adiantamento': 0.30, 'atraso': 0.6},
    'prod3': {'processamento': 13, 'entrega': 100, 'adiantamento': 1.00, 'atraso': 2},
    'prod4': {'processamento': 15, 'entrega': 34, 'adiantamento': 0.20, 'atraso': 0.4},
    'prod5': {'processamento': 9, 'entrega': 50, 'adiantamento': 1.00, 'atraso': 2},
    'prod6': {'processamento': 22, 'entrega': 44, 'adiantamento': 0.70, 'atraso': 1.4},
    'prod7': {'processamento': 17, 'entrega': 32, 'adiantamento': 0.40, 'atraso': 0.8},
    'prod8': {'processamento': 30, 'entrega': 60, 'adiantamento': 0.20, 'atraso': 0.4},
    'prod9': {'processamento': 12, 'entrega': 80, 'adiantamento': 0.30, 'atraso': 0.6},
    'prod10': {'processamento': 16, 'entrega': 150, 'adiantamento': 2.00, 'atraso': 4},
}


# Ordernar por data de entrega crescente
ordem_entregas = [(prod, valores['entrega']) for prod, valores in dados.items()]
ordem_entregas.sort(key=lambda x: x[1])
ordem_entregas = [prod[0] for prod in ordem_entregas]


# Utilizar tempo de processamento para calcular inicio e fim
dados_edd = []
for indice, prod in enumerate(ordem_entregas):
    tempo_processamento = dados[prod]['processamento']

    inicio = 0
    if indice != 0:
        inicio = dados_edd[indice-1]['fim']

    fim = inicio + tempo_processamento
    dados_edd.append({'inicio': inicio, 'fim': fim})


# Definir atraso ou adiantamento
for indice, prod in enumerate(ordem_entregas):
    fim = dados_edd[indice]['fim']
    data_entrega = dados[prod]['entrega']
    dados_edd[indice].update({'atraso_ou_adiantamento': fim - data_entrega})


# Definir "ocorre adiantamento da ordem" e  "ocorre atraso da ordem"
for indice, _ in enumerate(ordem_entregas):
    atraso_ou_adiantamento = dados_edd[indice]['atraso_ou_adiantamento']

    ocorre_adiantamento = 0
    if atraso_ou_adiantamento < 0:
        ocorre_adiantamento = 1

    ocorre_atraso = 0
    if atraso_ou_adiantamento > 0:
        ocorre_atraso = 1

    dados_edd[indice].update({'ocorre_adiantamento': ocorre_adiantamento, 'ocorre_atraso': ocorre_atraso})


# Definir custo do adiantamento e custo do atraso
for indice, prod in enumerate(ordem_entregas):
    atraso_ou_adiantamento = dados_edd[indice]['atraso_ou_adiantamento']

    ocorre_adiantamento = dados_edd[indice]['ocorre_adiantamento']
    penalidade_adiantamento = dados[prod]['adiantamento']
    custo_adiantamento = abs(atraso_ou_adiantamento * penalidade_adiantamento * ocorre_adiantamento)

    ocorre_atraso = dados_edd[indice]['ocorre_atraso']
    penalidade_atraso = dados[prod]['atraso']
    custo_atraso = abs(atraso_ou_adiantamento * penalidade_atraso * ocorre_atraso)

    dados_edd[indice].update({'custo_adiantamento': custo_adiantamento, 'custo_atraso': custo_atraso})


# Calcular dados
adiantamento_total, atraso_total = 0, 0
custo_adiantamento_total, custo_atraso_total = 0, 0
for item in dados_edd:
    custo_adiantamento_total += item['custo_adiantamento']
    custo_atraso_total += item['custo_atraso']

    atraso_ou_adiantamento = item['atraso_ou_adiantamento']
    if atraso_ou_adiantamento < 0:
        adiantamento_total += abs(atraso_ou_adiantamento)
    elif atraso_ou_adiantamento > 0:
        atraso_total += atraso_ou_adiantamento

print(f'Adiantamento total: {adiantamento_total}')
print(f'Atraso total: {atraso_total}')
print(f'Custo por adiantamento total: {custo_adiantamento_total}')
print(f'Custo por atraso total: {custo_atraso_total}')
