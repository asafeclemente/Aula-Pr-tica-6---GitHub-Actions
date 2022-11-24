from random import randrange
from somar import somar_dois_numeros
from subtrair import subtrair_dois_numeros

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