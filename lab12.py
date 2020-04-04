potAltura = int(input())
nSubDiv = int(input())
char = input()

h = 1
for i in range(potAltura):
    h *= 2
b = 2 * h - 1

numTriP = [1]
aux0 = 2
for i in range(nSubDiv-1):
    numTriP.append(numTriP[i] + aux0)
    aux0 *= 2

def tela_branca():
    return [ [" " for j in range(b)] for i in range(h)]

def desenho_base(telaBranca):
    largura = 1
    posStart = h - 1
    for linha in range(h):
        for i in range(largura):
            posNaLinha = posStart + i
            telaBranca[linha][posNaLinha] = char
        largura += 2
        posStart -= 1
    return telaBranca

def printa(tela):
    for i in range(len(tela)):
        for j in range(len(tela[i])):
            print(tela[i][j], end='')
        print()

def triangulo_branco(x, y, altura, telaDesenho):
    largura = 1
    posStart = x
    for linha in range(altura):
        for posNaLinha in range(largura):
            telaDesenho[y-linha][posStart+posNaLinha] = ' '
        largura += 2
        posStart -= 1

def emoldura(telaBase):
    horizontal = list('+'+ '-'*(b+2) +'+')
    telaBase.insert(0, list('|'+ ' '*(b+2) +'|'))
    telaBase.insert(0, horizontal)
    telaBase.append(list('|'+ ' '*(b+2) +'|'))
    telaBase.append(horizontal)
    for x in range(2, len(telaBase) - 2):
        telaBase[x].append(' ')
        telaBase[x].append('|')
        telaBase[x].insert(0,' ')
        telaBase[x].insert(0,'|')
    for linha in range(len(telaBase)):
        for coluna in range(len(telaBase[0])):
            print(telaBase[linha][coluna], end='')
        print()

base = b
altura = h
aux3 = h
def recursao(p, telaDesenho):
    if p == 0:
        global base
        global altura
        global aux3
        return telaDesenho
    tela = recursao(p-1, telaDesenho)
    meio = base//2
    aux3 //= 2
    for linha in range(len(tela)-1, -1, -altura): # h
        aux = 0
        base = meio
        for tri in range(numTriP[p-1]):
            triangulo_branco(meio+aux, linha, aux3, telaDesenho)
            #printa(telaDesenho)
            aux += base + 1 #AQUI TA ERRADO
        numTriP[p-1] -= 1
    altura = altura//2
    return telaDesenho

emoldura(recursao(nSubDiv, desenho_base(tela_branca())))
