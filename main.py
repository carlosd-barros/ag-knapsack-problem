from agbase import (
    criarPopulacaoAPartirDeIndividuosExistentes,
    gerarBinarioString,
)

#####################################
# ESTRUTURA DO ALGORITIMO GENÉTICO
# 1- Inicialização da população
# 2 - Avaliação de cada indivíduo
# 3 - Seleção de alguns indivíduos
# 4 - crossover e mutação
# 5 - concepção da nova geração
# repete a partir do passo 2 até estar satisfeito
# 6 - fim do algoritimo
#####################################

sortBeneficio = lambda x: x[1]
sortPeso = lambda x: x[2]

# estrutura dos cromossomos:
# [binário: str, benefício/fitness: int, peso: int]


# população inicial
# gerar uma população de forma randomica
populacao_length = 100
populacao = [ gerarBinarioString(length=8) for i in range(populacao_length) ]

# função de aptidão / fitness function
# criar uma função que vai avaliar cada indivíduo
# e recompensar os que estiverem melhor adaptados
# e punir aqueles menos adaptados
# algo semelhante a isso aqui
# populacao = [ calcula_apttidao(individuo) for individuo in populacao ]


# seleção
# função para selecionar os indivíduos mais aptos da população
# utilizando metodo da roleta para garantir a diversidade de indivíduos
melhores = []

# crossover
# fazer o cruzamento dos indivíduos selecionados
# no item anterior e gerar uma nova populaçao
nova_populacao = criarPopulacaoAPartirDeIndividuosExistentes(melhores)

# mutação
# fazer uma função que recebe uma população e calcula a probabilidade
# de um indivíduo da nossa população estar ou não apto a receber uma mutação
# criar um calculo que determina se o indivíduo recebe ou não a mutação
# taxa de mutação deve estar entre 0,001 e 0,1 dos indivíduos da população


melhor_global = [None, None, None]
melhor_local = [None, None, None]

geracoes = int(input("Quantidade de gerações?\n"))

# loop por tantas geerações repetindo tudo que foi feito
# da função de aptidão em diante para cada geração