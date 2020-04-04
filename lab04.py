peso = float(input()) #kg
idade = int(input())
if (idade == 16 or idade == 17):
    autorizacao = input()
boaSaude = input()
usoDrogas = input()
primeiraDoacao = input()
if (primeiraDoacao == "N"):
    ultimaDoacao = int(input()) 
    doacoesNos12Meses = int(input())
sexo = input() #M ou F
if (sexo == "F"):
    gravida = input()
    amamentando = input()
    if (amamentando == "S"):
        idadeDoBebe = int(input())


print("Peso:", peso)
print("Idade:", idade)
if (idade == 16 or idade == 17):
    print("Documento de autorizacao:", autorizacao)
print("Boa saude:", boaSaude)
print("Uso drogas injetaveis:", usoDrogas)
print("Primeira doacao:", primeiraDoacao)
if (primeiraDoacao == "N"):
    print("Meses desde ultima doacao:", ultimaDoacao)
    print("Doacoes nos ultimos 12 meses:", doacoesNos12Meses)
print("Sexo biologico:", sexo)
if(sexo == "F"):
    print("Gravidez:", gravida)
    print("Amamentando:", amamentando)
    if(amamentando == "S"):
        print("Meses bebe:", idadeDoBebe)


pode = 1
if(peso < 51):
    pode = 0
    print("Impedimento: abaixo do peso minimo.")
if(16 > idade):
    pode = 0
    print("Impedimento: menor de 16 anos.")
if(idade > 69):
    pode = 0
    print("Impedimento: maior de 69 anos.")
if(idade > 60 and primeiraDoacao == "S"):
    pode = 0
    print("Impedimento: maior de 60 anos, primeira doacao.")
if((idade == 16 or idade == 17) and autorizacao == "N"):
    pode = 0
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
if(boaSaude == "N"):
    pode = 0
    print("Impedimento: nao esta em boa saude.")
if(usoDrogas == "S"):
    pode = 0
    print("Impedimento: uso de drogas injetaveis.")
if(sexo == "M" and primeiraDoacao == "N" and ultimaDoacao <= 2):
    pode = 0
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
if(sexo == "F" and primeiraDoacao == "N" and ultimaDoacao <=3):
    pode = 0
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
if(sexo == "M" and primeiraDoacao == "N" and doacoesNos12Meses >= 4):
    pode = 0
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
if(sexo == "F" and primeiraDoacao == "N" and doacoesNos12Meses >= 3):
    pode = 0
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
if(sexo == "F" and gravida == "S"):
    pode = 0
    print("Impedimento: gravidez.")
if(sexo == "F" and amamentando == "S" and idadeDoBebe < 12):
    pode = 0
    print("Impedimento: amamentacao.")
if(pode):
    print("Procure um hemocentro para triagem completa.")
