moeda = input()
data = input()
compra = []
venda = []
cotacao = input()
somaC = 0.0
somaV = 0.0

while (cotacao != "0.0000 0.0000"):
	separado = cotacao.split()
	compra.append(float(separado[0]))
	venda.append(float(separado[1]))

	somaC += float(separado[0])
	somaV += float(separado[1])
	if(len(compra) == 5):
		media5c = somaC / 5
		media5v = somaV / 5
	cotacao = input()

print("Moeda:", moeda)
print("Data:", data)
print("Valor minimo para compra:", format(min(compra), ".4f"))
print("Valor maximo para venda:", format(max(venda), ".4f"))
if(len(compra) >= 5):
        print("Medias das cinco cotacoes mais recentes:", format(media5c, ".4f"), format(media5v, ".4f"))
print("Medias do historico:", format(somaC / len(compra), ".4f"), format(somaV / len(venda), ".4f"))