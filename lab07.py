notasAC = [float(x) for x in input().split()]
def lista_Labs(z):
    y=z[1:-1]
    y = y.split(",")
    y[0] = float(y[0])
    y[1] = int(y[1])
    return y
labs = [ lista_Labs(x) for x in input().split()]
notasP = [float(x) for x in input().split()]
freq = float(input())  

#Atividades conceituais
somaAC = 0
for i in notasAC:
    somaAC += i
mediaAC = somaAC / len(notasAC)
print("Media das atividades conceituais:", format(mediaAC, '.1f') )

#Labs
somaLabs = 0
somaPesos = 0
for i in labs:
    somaLabs += i[0] * i[1]
    somaPesos += i[1]
mediaLabs = somaLabs / somaPesos
print("Media das tarefas de laboratorio:", format(mediaLabs, '.1f') )

#Provas
mediaP = (notasP[0]*2 + notasP[1] + notasP[2]*4) / 7
print("Media das avaliacoes escritas:", format(mediaP, '.1f') )

print("Frequencia: " + str(freq) + "%")

if(freq >= 75):
    if(mediaP >= 5 and mediaLabs >= 5):
        print("Aprovado(a) por nota e frequencia.")
        print("Media final:", format(max([5, 0.6*mediaP + 0.3*mediaLabs + 0.1*mediaAC]), '.1f'))
    elif(mediaP >= 2.5 and mediaLabs >= 2.5):
        notaE = float(input())
        mediaPre = min([4.9, 0.6*mediaP + 0.3*mediaLabs + 0.1*mediaAC])
        mediaFinal = (mediaPre + notaE)/2
        print("Media preliminar:", format(mediaPre, '.1f') )
        print("Nota no exame:", format(notaE, '.1f') )
        if(mediaFinal >= 5):
              print("Aprovado(a) por nota e frequencia.")
        else:
              print("Reprovado(a) por nota.")
        print("Media final:", format(mediaFinal, '.1f'))
    else:
        print("Reprovado(a) por nota.")
        print("Media final:", format(min([mediaP, mediaLabs]), '.1f'))
else:
    print("Reprovado(a) por frequencia.")
    print("Media final:", format(min([mediaP, mediaLabs]), '.1f'))