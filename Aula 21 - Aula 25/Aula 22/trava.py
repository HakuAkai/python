def trava( profundidade ):
    print(f"Executando a função 'trava' na profundidade: {profundidade}")
    # num_pa = 500
    # pa = (num_pa + 1) * (num_pa / 2)
    if profundidade > 1:
        trava( profundidade - 1)
    
def progressao_aritmetica( valor_progressao ):
    if valor_progressao <= 1:
        return 1
    else:
        return valor_progressao + progressao_aritmetica( valor_progressao - 1 )

num_pa = 100

resultado_pa = progressao_aritmetica( num_pa )
pa = (num_pa + 1) * (num_pa / 2)
print(f"Resultado da PA: {resultado_pa} | Recursividade")
print(f"Resultado da PA: {pa} | Formula")