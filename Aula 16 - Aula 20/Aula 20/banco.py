lancamentos = [
    {"lancamento" : "Pagamento recebido", "valor": 2419.355},
    {"lancamento" : "Posto Shell", "valor": 55.0000},
    {"lancamento" : "Mc Donalds", "valor": 38.99999}
]

print(f"{'Lançamento:':<27} - Valor:\n")
for lancamento in lancamentos:
    print("> {0:<25} - R$ {1:.2f}".format(lancamento['lancamento'], lancamento['valor']))