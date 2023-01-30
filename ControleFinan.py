despesas = int(input("Digite o valor total de despesas: "))
fechamento = int(input("Digite o valor total de fechamento do mês: "))
lucros =  fechamento - despesas 

#saida de dados 
print("-" * 30)
print("os dados coletados foram:")
print("DESPESAS: ",despesas)
print("FECHAMENTO: ",fechamento)
print("LUCROS DO MÊS: ",lucros)
print("-" * 30)