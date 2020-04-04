vocabulário = {}
linha = input()
while(linha[0:3] != "---"):
    palavrasDaLinha = linha.lower().replace("-", " ").split()
    for palavra in palavrasDaLinha:
        palavra = palavra.replace(",","")
        palavra = palavra.replace(".","")
        palavra = palavra.replace(":","")
        palavra = palavra.replace("?","")
        palavra = palavra.replace("!","")
        palavra = palavra.replace("(","")
        palavra = palavra.replace(")","")    
        if(vocabulário.get(palavra) == None):
            vocabulário[palavra] = 1
        else:
            vocabulário[palavra] += 1
    linha = input()
prefixos = []
linha = input()
while(linha[0:3] != "---"):
    prefixos.append(linha.lower())
    linha = input()


print("Vocabulario:")
vocCopy = list(vocabulário.keys())
vocOrdemAlfabetica = []
while len(vocCopy) != 0:
    palavra = min(vocCopy)
    vocCopy.remove(palavra)
    vocOrdemAlfabetica.append(palavra)
    print(palavra + " (" + str(vocabulário.get(palavra)) + ")")

def AutoComplete(prefix):
    sugestoes = []
    for key in vocOrdemAlfabetica:
        if prefix in key[0:len(prefix)] and prefix != key:
            sugestoes.append(key)
    if len(sugestoes) != 0:
        return " " + str(sugestoes).replace(",", "").replace("[","").replace("]","").replace("'","")
    else:
        return ""
print("Sugestoes:")
for pref in prefixos:
    print(pref + ":" + AutoComplete(pref))
