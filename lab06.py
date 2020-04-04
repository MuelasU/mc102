objeto = input()
caracter = input()
lado = int(input())
if objeto not in ["Q", "H", "TI", "TR", "R", "QQ", "X"]:
    print("Identificador invalido.")
    
else:
    if(objeto == "Q"):
        if(lado >= 3):
            espaço = lado - 2
            print(lado * caracter)
            print((str(caracter) + " "*espaço + str(caracter) + "\n") * espaço + lado*caracter)
        else:
            print("Dimensao invalida.")

    elif(objeto == "H"):
        if(lado < 3):
            print("Dimensao invalida.")
        else:
            espAnt = lado - 1
            print(espAnt*" " + lado*caracter)
            espAnt -= 1
            for espEnt in range(lado, lado + 2*espAnt + 1, 2):
                print(espAnt*" " + caracter + espEnt*" " + caracter)
                espAnt -= 1
            espAnt = 1
            for espEnt in range(lado + 2*(lado - 2) - 2, lado - 1, -2):
                print(espAnt*" " + caracter + espEnt*" " + caracter)
                espAnt += 1
            print(espAnt*" " + lado*caracter)
    elif(objeto == "TR"):
        if(lado < 3):
            print("Dimensao invalida.")
        else:
            print(caracter)
            for i in range(lado - 2):
                print(caracter + i*" " + caracter)
            print(lado * caracter)
    elif(objeto == "TI"):
        if(lado < 3):
            print("Dimensao invalida.")
        else:
            espAnt = lado - 1
            print(espAnt * " " + caracter)
            espAnt -= 1
            for i in range(1,lado,2):
                print(espAnt*" " + caracter + i*" " + caracter)
                espAnt -= 1
            print(((lado*2) - 1) * caracter)
    elif(objeto == "R"):
        altura = int(input())
        if(lado >= 3 and altura >= 3):
            espaçoX = lado - 2
            espaçoY = altura - 2
            print(lado * caracter)
            print((str(caracter) + " "*espaçoX + str(caracter) + "\n") * espaçoY + lado*caracter)
        else:
            print("Dimensao invalida.")

    elif(objeto == "QQ"):
        largura = int(input()) #* (lado-1) + 1
        altura = int(input()) #* (lado-1) + 1
        if(largura <= 0 or altura <= 0):
            print("Dimensao invalida.")
        else:
            print((largura*(lado-1) + 1) * caracter)
            for i in range(altura):
                for x in range(lado - 2):
                    print(caracter, end="")
                    for j in range(largura):
                        print((lado - 2)*" " + caracter, end="")
                    print()
                print((largura*(lado-1) + 1) * caracter)
    else:                                       #X
        largura = int(input()) #* (lado-1) + 2
        altura = int(input()) #* (lado-1) + 2 
        if(largura <= 0 or altura <= 0):
            print("Dimensao invalida.")
        else:
            print((largura * (lado-1) + 1) * caracter)
            for i in range(altura):
                if (i % 2): #começa cheio
                    for x in range(lado - 2):
                        for j in range(largura):
                            if (j % 2): #vaza
                                print((lado - 2) * " ", end="")
                            else: #preenche
                                print(lado * caracter, end="")
                        print()
                else: #começa furado
                    for x in range(lado - 2):
                        for j in range(largura):
                            if (j % 2): #preenche
                                print((lado - 2) * caracter, end="")
                            else: #vaza
                                print(caracter + (lado - 2) * " " + caracter, end="")
                        print()
                print((largura * (lado-1) + 1) * caracter)