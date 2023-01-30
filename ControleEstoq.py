entrada = input("Digite o nome do produto que está entrando: ")
quantEnd = int(input("Digite a quantidade de produto: "))
saida = input("Digite o nome do produto que está saindo: ")
quantSai = int(input("Digite a quantidade de produto: "))
estoque = quantEnd-quantSai


#saida de dados 
print("-" * 30)
print("os dados coletados foram:")
print("ENTRADA: ",entrada)
print("QUANTIDADE: ",quantEnd)
print("SAIDA: ",saida)
print("QUANTIDADE: ",quantSai)
print("ESTOQUE: ",estoque)
print("-" * 30)