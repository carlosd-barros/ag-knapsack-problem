from random import uniform

from agbase import CAPACIDADE as CAP
from agbase import sortBeneficio, sortPeso, sortAvaliacao, sortValorDeUtilidade
from agbase import gerarBinarioString, calculaBeneficioEPeso, rankingSelecaoLinear


#####################################
# ESTRUTURA DO ALGORITIMO GENÉTICO
# 1 - Inicialização da população | FEITO
# 2 - Avaliação de cada indivíduo
# 3 - Seleção de alguns indivíduos | FEITO
# 4 - crossover e mutação
# 5 - concepção da nova geração | FEITO
# repete a partir do passo 2 até estar satisfeito
# 6 - fim do algoritimo
#####################################

# estrutura dos cromossomos:
# [binário:str, benefício:int, peso:int, avaliacao:float]


# 1 - Inicialização da população
POPULACAO_LENGTH = 100
BS = gerarBinarioString
populacao = [ calculaBeneficioEPeso( BS(length=8) ) for i in range( POPULACAO_LENGTH ) ]
print("1 - Inicialização da população")
print(f"populoção inicial criada >>> {populacao[-1]}, tamanho: {len(populacao)}","-"*50, sep="\n")

qt_geracoes = 1000
sp = round(uniform(1,2), 2)
melhor_geracao = [0, 0, 0, 0, 0]# [bin, ben, peso, avaliacao, geracao]

for i in range(2): # range(qt_geracoes):
    if not isinstance(populacao[0], (list, tuple,)):
        populacao = [ calculaBeneficioEPeso(x) for x in populacao ]

    # print("# 2 - Avaliação de cada indivíduo")
    # os indivíduos devem ter essa estrutura: [binário:str, benefício:int, peso:int, avaliacao:float]


    # print("#3 - Seleção de alguns indivíduos")
    # precisa da dois pronta para funcionar
    length, retries, quant, melhores = 0, 0, 10, []

    # while length != quant:
    #     melhores = rankingSelecaoLinear( populacao=populacao , quant=quant)
    #     length = len(melhores)
    #     retries+=1


    # pegando o melhor da geração
    dif = melhor = None
    for current_best in melhores:
        if not melhor: melhor=current_best;dif=CAP-current_best[2];continue

        binario, b, p, a = current_best
        vu = b/p if b and p else 0
        current_dif = CAP - p

        if b > melhor[1] and p <= CAP:
            melhor = current_best
            dif = current_dif

    # pegando o melhor de todas as gerações
    if melhor and melhor[2] > melhor_geracao[2] and melhor[1] > melhor_geracao[1]:
        melhor_geracao = melhor + [i]


    # print("#4 - crossover e mutação")


    # print("#5 - concepção da nova geração")
    length, retries, nova_populacao = 0, 0,[]


    if melhor: print( f"Melhor da geração ({i}): - binário: {melhor[0]}, benefício: {melhor[1]}, peso: {melhor[2]}, avaliação: {round(melhor[3], 2)}." )


# 6 - fim do algoritimo
# printar o indivíduo ótimo e qual a sua geração
print( "-"*50, f"\nMelhor indivíduo - Geração: {melhor_geracao[-1]}, binário: {melhor_geracao[0]}, benefício: {melhor_geracao[1]}, peso: {melhor_geracao[2]}, avaliação: {round(melhor_geracao[3], 2)}.")
