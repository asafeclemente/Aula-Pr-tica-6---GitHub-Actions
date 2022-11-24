from random import randrange
from somar import somar_dois_numeros
from subtrair import subtrair_dois_numeros

def test_soma():

    x = somar_dois_numeros(1,-1)
    y = somar_dois_numeros(1,0)
    resultado = somar_dois_numeros(x,y)

    assert resultado == 1

def test_subtracao_de_numero_negativo():

    resultado = subtrair_dois_numeros(0,-1)

    assert resultado == 1

def test_soma_e_subtracao_opostas():

    primeiro_numero = somar_dois_numeros(1,1)
    resultado = subtrair_dois_numeros(primeiro_numero,primeiro_numero)

    assert resultado == 0

def soma_multiplas_vezes():

    numero = randrange(10)
    resultado = somar_dois_numeros(numero,numero)

    assert resultado == numero*2

def subtracao_multiplas_vezes():

    numero = randrange(10)
    resultado = subtrair_dois_numeros(numero,numero)

    assert resultado == 0