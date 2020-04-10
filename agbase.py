import random as rd
from random import uniform
from typing import Tuple, List


# Itens que podem ser add na mochila
# [benefício, peso]
ITENS = (
    [5,7], [8,8], [3,4], [2,10],
    [7,4], [9,6], [4,4], [5,7],
)
CAPACIDADE = 22 #capacidade da mochila

sortBeneficio = lambda x: x[1]
sortPeso = lambda x: x[2]
sortAvaliacao = lambda x: x[3]
sortValorDeUtilidade = lambda x: x[1]/x[2]


def gerarBinarioString(length:int=8) -> str:
    """Recebe um valor inteiro que vai determinar
    o tamanho do binário string que sera retornado."""
    return "".join([ rd.choice("01") for i in range(length) ])


def mutacao(value:str) -> str:
    """Retorna a estring recebida com um de seus
    valores alterados de forma aleatória."""
    index = rd.randint(0, len(value)-1)
    value = list(value)
    value[index] = "0" if value[index] == "1" else "1"

    return "".join(value)


def crossover1(value1:str, value2:str) -> List:
    """Recebe dois binários string de 8 bits e retorna uma tupla com
    duas novamos strings sendo a primeira composta pelos 4 primeiros
    bits do value2 e 4 ultimos bits do value1 e a segunda composta
    pelos 4 primeiros bits do value1 e 4 ultimos bits do value2."""
    new_value1 = value2[:4] + value1[4:]
    new_value2 = value1[:4] + value2[4:]

    return [new_value1, new_value2]


def crossover2(value1:str, value2:str) -> List:
    """Recebe dois binários string de 8 bits e retorna uma tupla com duas novamos
    strings sendo a primeira composta pelos 2 primeiros bits do value2 + os 4 bits do
    meio do value1 + os 2 ultimos bits do value2 e a segunda composta pelos 2 primeiros
    bits do value1 + os 4 bits do meio do value2 + os 2 ultimos bits do value1."""
    new_value1 = value2[:2] + value1[2:6] + value2[6:]
    new_value2 = value1[:2] + value2[2:6] + value1[6:]

    return [new_value1, new_value2]


def calculaBeneficioEPeso(binario:str) -> List:
    """Retorna um indivíduo com a seguinte estrutura
    [binario:str, benefício:int, peso:int]."""
    beneficio = 0
    peso = 0

    for index, bit in enumerate(binario):
        if bit == '0': continue
        b, p = ITENS[index]
        beneficio += b
        peso += p

    return [binario, beneficio, peso]


# Aptidão, Avaliação, fitness ou Objetivo
def avaliacaoLinear(n:int, pos:int, sp:float) -> float:
    """n: tamanho da população;
    pos: posição do indivíduo;
    sp: um valor qualquer entre 1 e 2."""
    return abs( round(2 - sp + ( 2 * (sp - 1) * (pos - 1) ) / (n - 1), 4) )


def rankingSelecaoLinear(populacao:List, quant:int, ass:bool=True, tend:int=0.0001):
    """população -> indivíduo: [binário:str, benefício:int, peso:int, avaliacao:float];
    quant: quantidade de sorteios;
    ass: define se a assimetria será positiva (True) ou negativa (False);
    tend: define a variação da assimetria, onde 0 significa que o grau de desvio será nenhum."""
    populacao.sort(key=sortAvaliacao)
    Fi = populacao[0][3] - 0.001 # min
    Fj = populacao[-1][3] + 0.001 # max
    
    results = []
    for i in range(quant):
        tendencia = (Fi + Fj) / 2
        tendencia = tendencia + tend if ass else tendencia - tend
        criterio = round( rd.triangular(low=Fi, high=Fj, mode=tendencia),4 )
        # print(f"{i} criterio: {criterio}, ass: {ass}, tend: {tend}")        
        for individuo in populacao:
            #print(populacao)
            binario, b, p, a = individuo
            if a > criterio and p <= CAPACIDADE:
                # print(f"sorteado: {individuo}\n","-"*30)
                results.append(individuo)
                break

    results.sort(key=sortPeso)
    return results


def criarNovaGeracao(populacao:List, prob:int=1) -> List:
    """Aplica a função de 'mutacao' em uma pocentagem (definida em 'prob')
    aleatória dos novos indivíduos sendo gerados pelo crossover da 'populacao'.
    Retorna uma lista com N * (N-1) indivíduos, onde N é o tamanho da 'populacao'."""
    if prob >= 1: prob = prob/100
    results = []

    for index, parent1 in enumerate(populacao):
        for parent2 in populacao[index+1:]:
            index = rd.choice([0,1])
            childs = crossover1(parent1[0], parent2[0])
            if rd.random() <= prob: childs[index] = mutacao(childs[index]);
            results += childs

    return results

def avaliacao(populacao):
    sp = round(uniform(1,2), 2)
    populacao_tam = len(populacao)
    for i in range(populacao_tam):        
        av = avaliacaoLinear(populacao_tam, i, sp)    
        populacao[i].append(av)
