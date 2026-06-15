#Calcula quantos dias um produto duraria 
# se a pessoa usar X porções por dia

Nome = input("Digite seu nome: ")
Porcoes_Total = int(input("Quantidade de porções: "))
Porcoes_Usadas = int(input("Porções usadas por dia: "))

Dias = Porcoes_Total / Porcoes_Usadas
print(f"Vão durar {int (Dias)} dias se {Nome} usar {Porcoes_Usadas} porções por dia" )
#print(f"Vão ser necessários {Dias:.0f} dias se {Nome} usar {Porcoes_Usadas} porções por dia" )
