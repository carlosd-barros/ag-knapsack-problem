from random import uniform

from agbase import (
    sortBeneficio, sortPeso, sortAvaliacao, sortValorDeUtilidade,
    gerarBinarioString, calculaBeneficioEPeso, CAPACIDADE as CAP,
    rankingSelecaoLinear, criarNovaGeracao, avaliacaoLinear, criarNovaGeracao,
)


POPULACAO_LENGTH = 20
BS = gerarBinarioString
populacao = [ calculaBeneficioEPeso( BS(length=8) ) for i in range(POPULACAO_LENGTH) ]
del BS

geracao = 0
qt_geracoes = 1000
melhor_geracao = ['0', 0, 0, 0]
sp = round(uniform(1,2), 2)

for i in range(qt_geracoes):
    n = len(populacao)
    populacao = [ individuo+[avaliacaoLinear(n=n,pos=pos,sp=sp)] for pos, individuo in enumerate(populacao) ]

    melhores = rankingSelecaoLinear(populacao=populacao, quant=10)

    dif = melhor = None
    for current_best in melhores:
        binario, b, p, a = current_best
        if not melhor: melhor=current_best; dif=CAP-p;continue

        vu = b/p if b and p else 0
        current_dif = CAP - p

        if b > melhor[1] and p <= CAP:
            melhor = current_best
            dif = current_dif

    if melhor[2] > melhor_geracao[2] and melhor[1] > melhor_geracao[1]:
        melhor_geracao = melhor
        geracao = i

    novos_individuos = criarNovaGeracao(melhores)

    indiviuos_aptidao_baixa = rankingSelecaoLinear(populacao=populacao, quant=10, ass=False, tend=0.8)
    populacao = novos_individuos + [ x[0] for x in indiviuos_aptidao_baixa ]
    populacao = [ calculaBeneficioEPeso(x) for x in populacao ]

    print( f"Melhor da geração ({i}): - binário: {melhor[0]}, benefício: {melhor[1]}, peso: {melhor[2]}, avaliação: {round(melhor[3], 2)}." )

print( "-"*50, f"\nMelhor indivíduo - Geração: {geracao}, binário: {melhor_geracao[0]}, benefício: {melhor_geracao[1]}, peso: {melhor_geracao[2]}, avaliação: {round(melhor[3], 2)}.")
