class Pessoa:
    def __init__(self, *filhos, nome = 'Sidnei', idade = 53):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    felipe = Pessoa(nome = 'Felipe')
    sidnei = Pessoa(felipe, nome='Sidnei')
    print(Pessoa.cumprimentar(sidnei))
    print(id(sidnei))
    print(sidnei.cumprimentar())
    print(sidnei.nome)
    print(sidnei.idade)
    for filho in sidnei.filhos:
        print(filho.nome)
    sidnei.sobrenome = 'Lopes Ribeiro' # atributo criado dinamicamente #
    print(sidnei.nome, sidnei.sobrenome)
    print()
    del sidnei.filhos # apaga um atributo
    print(sidnei.__dict__) # apresenta todos atributos de instância de um objeto #
    print(felipe.__dict__)
    # também é possível remover atributos dinamicamente #
    # mas adicionar e apagar atributos dinamicamente não é uma boa prática #
    # Porém, em certos casos especiais é admissível fazê-lo como, por exemplo, mudar um formato de data a ser apresentado em um site #


