ids = sorted(input().split())   #IDENTIFICADORES
linker = {}     #LINKA CHAVE AO VALOR
linkado = {}    #CHAVE É LINKADA PELO VALOR
pageRank = {}   #PAGERANK SERÁ ATUALIZADA A CADA PASSO
for i in ids:
    linker[i] = []
    linkado[i] = []
    pageRank[i] = 1/len(ids)    #PASSO 0
linha = input()
while(not linha.isdigit()):
    linha = linha.split(" -> ")
    if(linha[0] != linha[1]):
        if(linha[1] not in linker[linha[0]]):
            linker[linha[0]].append(linha[1])
            linkado[linha[1]].append(linha[0])
    linha = input()
numPassos = int(linha)

def calPR(id_pag): 
    soma = 0
    for id_pag_link in linkado[id_pag]:
        soma += pageRank[id_pag_link]/len(linker[id_pag_link])
    return 0.125/len(ids) + 0.875*soma

for i in range(len(ids)):
    print(ids[i], "->", linker[ids[i]])
    print(linkado[ids[i]], "->", ids[i])

print("PageRank (passo 0)")
for idn in ids:
    print(idn+":", format(pageRank[idn], '0.3f'))
for passo in range(1, numPassos+1):
    print("PageRank", "(passo", str(passo)+")")
    aux = {}
    for idn in ids:
        aux[idn] = calPR(idn)
        print(idn+":", format(aux[idn], '.3f'))
    pageRank.update(aux)