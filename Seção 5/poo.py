# Orientação a objetos: Paradigma de Programação
# Classes e Objetos

class Veiculo:
    def movimentar(self):
        print('Sou um veículo e me movimentei!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Getter
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}')

    def getNumRegistro(self):
        return self.__num_registro

    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro

class Carro(Veiculo):
    # Método __init__ será herdado de 'Veículo'
    def movimentar(self):
        print('Sou um carro e estou andando pelas ruas!!!')

class Motocicleta(Veiculo):
    def movimentar(self):
        print('Sou uma motoca!!!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)
    
    def getCategoria(self):
        return self.__cat

    def movimentar(self):
        print('Sou um avião. Estou voando.')

if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('49903-5')
    # print(f'Registro do veículo: {meu_veiculo.getNumRegistro()}\n')

    meu_carro = Carro('Volkswagen', 'Gol')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    seu_carro = Carro('Audi', 'A5 Sportback')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()

    minha_moto = Motocicleta('Honda', 'CB 500')
    minha_moto.movimentar()
    minha_moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.getCategoria()}')