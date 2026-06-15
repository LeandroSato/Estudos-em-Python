#definir função

def saudacao(nome, idade):
  print(f"Olá {nome}! Você tem {idade} anos de idade")


saudacao("Leandro", "19")
saudacao("Isabella", "20")

#def somar 

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

def somar(x, y):
    return x + y

total = somar(x, y)
print(f"O resultado da soma é de: {total}")

#def calcular_desconto(preco, porcentagem):

def calcular_desconto(preco, porcentagem):
  return preco - (preco * porcentagem / 100)

valor_final = calcular_desconto(1010, 25)
print(f" O valor com desconto é de: R${valor_final:.2f}")