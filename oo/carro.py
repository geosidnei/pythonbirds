#aula 10 do curso Pybirds
# 13/02/2020
# Composição


"""
Você deve criar uma classe carro que possui dois outros atributos compostos por duas classes:

1) Motor
2) Direção

O Motor controla a velocidade e tem os seguintes atributos:
    1) Atributo de dado velocidade;
    2) Método acelerar, que incrementa a velocidade de uma unidade
    3) Método frear para decrementar a velocidade em duas unidades

Direção: controla a direção e tem os atributos:
    1) Direção com valores possíveis: Norte, Sul, Leste e Oeste;
    2) Método girar_a_direita
    3) Método girar_a_esquerda

            N
          O   L
            S
    Exemplo da determinação do teste básico desta classe carro:
    # Testando motor
    ## DocTest abaixo

    >>> motor = Motor()
    >>> motor.velocidade
    0

    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direção #
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte' # valor inicial da direção
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    # Montando o aplicativo
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade
    0
    >>> carro.calcular_direcao()
    >>>'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Oeste'


"""
    # composição é a interação entre objetos diferentes,
    # que até podem ser de classes diferentes! #
    # O carro é um agregador, definidor da interface maior #

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Direção:
    rotação_a_direita_dicion = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotação_a_esquerda_dicion = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotação_a_direita_dicion[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotação_a_esquerda_dicion[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade) # esta função não deixa existir número menor que zero (ótimo para velocidade!)




 '''
   >> > if action == 'E':
        >> > my_car.acelerar()
        >> > elif action == 'F':
        >> > my_car.frear()
        >> > elif action == 'O':
        >> > print('The car ahas driven {quilometros} quilômetros.format(my_car.odometro)')
 
 '''