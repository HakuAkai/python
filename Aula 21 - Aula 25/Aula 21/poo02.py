class CarroFusca:
    carros = []

    def __init__(self, ligado, porta_aberta, velocidade_atual):
        self.ligado = ligado
        self.porta_aberta = porta_aberta
        self.velocidade_atual = velocidade_atual

        CarroFusca.carros.append(self)

    def acelerar( self ):
            if self.ligado == True and self.porta_aberta == False:
                return self.velocidade_atual + 10
            elif self.ligado == True and self.porta_aberta == True:
                return " Porta aberta "
            elif self.ligado == False and self.porta_aberta == False:
                return " Desligado "
            else:
                return " Erro "  

    def frear( self ):
        return self.velocidade_atual - self.velocidade_atual
    
carro01 = CarroFusca(True, True, 200)
carro02 = CarroFusca(False, False, 250)
herbie = CarroFusca(True, False, 150)

i = 0

for carro in CarroFusca.carros:
    i += 1
    print(f"\n {i}º carro: \n> Velocidade: Acelerada: {carro.acelerar():<15} | Freada: {carro.frear():<15} | Padrão: {carro.velocidade_atual}")
    