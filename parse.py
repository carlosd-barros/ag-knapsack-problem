from random import random


def inteiroParaBinario(num:int) -> str:
    """Recebe um inteiro e retorna uma string equivalente
    sua representação binária. Ex: input: 10 -> output: 1010"""
    binary = ""
    count = 0

    while num > 0 and count < 8:
        mod = str( int(num % 2) )
        binary += mod
        num /= 2
        count += 1

    return str( int(binary[::-1]) )


def binarioParaParteFracionaria(binary:str) -> str:
    """Recebe um binário string e retorna uma string
    equivalente a parte fracionária de um número real."""
    result = 0

    for index, value in enumerate(binary):
        result += int(value) * 2 ** ((index + 1) * -1)

    return str(result).split('.')[1]


def binarioParaReal(binary:str) -> float:
    """Recebe um binário string e retorna um número real sendo
    que os dois primairos bits vão representar a parte inteira
    e os demais a parte fracionária."""
    integer = str( int(binary[:2], base=2) )
    frac = binarioParaParteFracionaria(binary[2:])

    return float(integer + "." + frac)

def floatParaBinario(num:float):
    pass

def realParaBinario(num:float) -> str:
    """Recebe um valor float e retorna uma string
    equivalente a sua representação em binário."""
    integer, frac = str(num).split('.')

    integer = inteiroParaBinario(int(integer))
    # TODO: isso aqui tá errado, mas deixa assim por enquanto
    frac = inteiroParaBinario(int(frac))

    return integer + frac
