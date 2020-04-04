diagrama = []
linha = ""
while(True):
    linha = input()
    if(linha.isdigit()):
        linha = int(linha)
        break
    linha = linha.split()
    diagrama.append(linha)
procuradas = []
for i in range(linha):
    procuradas.append(input())
diagramaBase = [["." for x in range(len(diagrama[0]))] for y in range(len(diagrama))]
resultado = {}

def LerHorDir(word): #CORRETO
    tam = len(word)
    flag = False
    for i in range(len(diagrama)): #linhas
        for j in range(len(diagrama[i]) - tam + 1): #colunas
            if(diagrama[i][j] == word[0]): #se é igual a primeira letra
                j += 1
                flag = True
                for posLetra in range(1, tam): #percorre o restante da palavra
                    if(diagrama[i][j] != word[posLetra]):
                        flag = False
                        break
                    else:
                        j += 1  
                if(flag): #se é a palavra
                    global linha
                    linha -= 1
                    diagramaBase[i][j-tam:j] = diagrama[i][j-tam:j] #escreve no diagrama resposta
                    break
def LerCimaBaixo(word): #CORRETO
    tam = len(word)
    flag = False
    for j in range(len(diagrama[0])): #colunas
        for i in range(len(diagrama) - tam + 1): #linhas
            if(diagrama[i][j] == word[0]): #se é igual a primeira letra
                flag = True
                i+=1
                for posLetra in range(1, tam): #percorre o restante da palavra
                    if(diagrama[i][j] != word[posLetra]):
                        flag = False
                        break
                    else:
                        i += 1  
                if(flag): #se é a palavra
                    global linha
                    linha -= 1
                    for x in range(i-tam, i): #escreve no diagrama
                        diagramaBase[x][j] = diagrama[x][j]
                    break

def LerHorEsq(word): #CORRETO
    tam = len(word)
    flag = False
    for i in range(len(diagrama)): #linhas
        for j in range(len(diagrama[i]) - tam + 1): #colunas
            if(diagrama[i][j] == word[tam - 1]): #se é igual a última letra
                j-=1
                flag = True
                for posLetra in range(tam - 2, 0, -1): #percorre o restante da palavra RESTRITO PARA PALAVRAS MAIORES QUE 2 LETRAS
                    if(diagrama[i][j] != word[posLetra]):
                        flag = False
                        break
                    else:
                        j-=1
                if(flag): #se é a palavra
                    global linha
                    linha-=1
                    diagramaBase[i][j-tam+1:j+1] = diagrama[i][j-tam+1:j+1] #escreve no diagrama resposta
                    break


def LerBaixoCima(word):
    tam = len(word)
    flag = False
    for j in range(len(diagrama[0])): #colunas
        for i in range(len(diagrama) - tam + 1): #linhas
            if(diagrama[i][j] == word[tam - 1]): #se é igual a primeira letra
                flag = True
                i+=1
                for posLetra in range(1, tam): #percorre o restante da palavra
                    if(diagrama[i][j] != word[posLetra]):
                        flag = False
                        break
                    else:
                        i += 1  
                if(flag): #se é a palavra
                    global linha
                    linha -= 1
                    for x in range(i-tam, i): #escreve no diagrama
                        diagramaBase[x][j] = diagrama[x][j]
                    break

while(linha > 0):
    o = linha
    #LerHorDir(procuradas[len(procuradas) - 1])
    #LerHorEsq(procuradas[len(procuradas) - 1])
    #LerCimaBaixo(procuradas[len(procuradas) - 1])
    #LerBaixoCima(procuradas[len(procuradas) - 1])
    #del(procuradas[len(procuradas) - 1])
    f = linha
    vezes = o - f
    resultado[procuradas[len(procuradas) - 1]] = vezes #escreve no dicionário

print(diagramaBase)