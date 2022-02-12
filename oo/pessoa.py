class Pessoa:
    def __init__(self, *filhos, nome = 'Sidnei', idade = 53):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    felipe = Pessoa(nome = 'Felipe')
    sidnei = Pessoa(felipe, nome='sidnei')
    print(Pessoa.cumprimentar(sidnei))
    print(id(sidnei))
    print(sidnei.cumprimentar())
    print(sidnei.nome)
    print(sidnei.idade)
    for filho in sidnei.filhos:
        print(filho.nome)


