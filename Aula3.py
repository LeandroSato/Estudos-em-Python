#numero1 = 10
#numero2 = 5

#print(numero1 + numero2) soma
#print(numero1 - numero2) subtração
#print(numero1 * numero2) multiplicação
#print(numero1 / numero2) divisão
#print(numero1 // numero2) divisão inteira
#print(numero1 % numero2) resto da divisão
#print(numero1 ** numero2) potência

Produto = float(input("Digite o valor do produto: ")) # valor em real
Desconto = int(input("Digite o valor do desconto: ")) #valor em %

Valor_Final = Produto - (Produto * Desconto / 100)
print(f"O valor final do produto é R${Valor_Final}")

