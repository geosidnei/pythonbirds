class Pessoa:
    def __init__(self, nome = 'Sidnei', idade = 53):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Raimunda')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'sidnei'
    print(p.nome)
    print(p.idade)