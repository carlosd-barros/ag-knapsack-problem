from typing import Tuple, List
from random import randint, random, choice, uniform
from string import ascii_letters, ascii_lowercase, ascii_uppercase

from parse import binarioParaReal


def numeroAleatorio(integer:int=2, decimal:int=2, r:bool=False) -> float:
    """Recebe dois valores inteiros e retorna um valor real
    onde o parametro 'inteiro' determina a quantidade de casas
    a esquerda do ponto, 'decimal' determina a quantidade de
    casas a direita do ponto e 'r' determina se o arredondamento
    será ou não aplicado."""
    num = random() * (10 ** integer)

    return round(num, decimal) if r else num


def stringAleatoria(length:int=10) -> str:
    """Recebe um valor inteiro e retorna
    string com o tamanho do valor passado."""
    return "".join( choice(ascii_letters) for x in range(length) )


def gerarBinarioString(length:int=8) -> str:
    """Recebe um valor inteiro que vai determinar
    o tamanho do binário string que sera retornado."""
    return "".join([ choice(['0','1']) for i in range(length) ])


def gerarListaDeStrings(listLength=100, stringLength=10):
    """Recebe dois valores interios e retorna uma lista de strings
    onde 'listLength' vai determinar a quantidade de elementos da lista
    e 'stringLength' o tamanho da string de cada elemento."""
    return [ stringAleatoria(stringLength) for i in range(listLength) ]


def stringParaLista(string:str, maxNum:int=100):
    return [ string, uniform(0, maxNum) ]


def matrizDeStrings(lista: List):
    return [ stringParaLista(string) for string in lista ]


def moduloAoQuadrado(value):
    return abs(2 - value ** 2)


def selecionaMelhores(populacao:List, quant:int=10) -> Tuple:
    populacao.sort(key=lambda x: x[1], reverse=True)

    return populacao[:quant]


def mutacao(value:str) -> str:
    index = randint(0, len(value)-1)
    value = list(value)
    value[index] = '0' if value[index] == '1' else '1'

    return "".join(value)

def crossover1(value1:str, value2:str) -> Tuple[str,str]:
    """Recebe dois binários string de 8 bits e retorna uma tupla com
    duas novamos strings sendo a primeira composta pelos 4 primeiros
    bits do value2 e 4 ultimos bits do value1 e a segunda composta
    pelos 4 primeiros bits do value1 e 4 ultimos bits do value2."""
    new_value1 = value2[:4] + value1[4:]
    new_value2 = value1[:4] + value2[4:]

    return new_value1, new_value2


def crossover2(value1:str, value2:str) -> Tuple[str,str]:
    """Recebe dois binários string de 8 bits e retorna uma tupla com duas novamos
    strings sendo a primeira composta pelos 2 primeiros bits do value2 + os 4 bits do
    meio do value1 + os 2 ultimos bits do value2 e a segunda composta pelos 2 primeiros
    bits do value1 + os 4 bits do meio do value2 + os 2 ultimos bits do value1."""
    new_value1 = value2[:2] + value1[2:6] + value2[6:]
    new_value2 = value1[:2] + value2[2:6] + value1[6:]

    return new_value1, new_value2


def avaliacao(binary:str):
    pass


def roletaSelecao(populacao:List, quant:int):
    sum_fitness = sum([ x[1] for x in populacao ])
    num = choice([0,1])

    return None


def selecionaElementosAleatoriosEModifica(populacao:List, quant:int=10):
    results = []
    length = len(populacao) - 1
    index = randint(0, length)

    for i in range(max):
        individuo = mutacao(populacao.pop(index)[0])
        results.append(individuo)
        length -= 1
        index = randint(0, length)

    return results


def criarPopulacaoAPartirDeIndividuosExistentes(individuos:List) -> List:
    result = []

    for index, value in enumerate(individuos):
        for val in individuos[index+1:]:
            result += crossover2(value[0], val[0])

    return result






