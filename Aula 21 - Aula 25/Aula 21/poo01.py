class CarroFusca:
    porta_aberta = False
    velocidade_atual = 233
    potencia_motor = 67
    ligado = True
    cor = "azul"

    def acelerar():
        if CarroFusca.ligado == True and CarroFusca.porta_aberta == False:
            return CarroFusca.velocidade_atual + 10

    def frear():
        return CarroFusca.velocidade_atual - CarroFusca.velocidade_atual

    def abrir_porta():
        return not CarroFusca.porta_aberta

    def ligar():
        return not CarroFusca.ligado

print(f"\n > Velocidade: \n Acelerada: {CarroFusca.acelerar()} | Freada: {CarroFusca.frear()} | Padrão: {CarroFusca.velocidade_atual}")
print(f"\n > A porta está aberta: \n Padrão: {CarroFusca.porta_aberta} | Abrindo: {CarroFusca.abrir_porta()}")
print(f"\n > O carro está ligado: \n Padrão: {CarroFusca.ligado} | Abrindo: {CarroFusca.ligar()} \n")

