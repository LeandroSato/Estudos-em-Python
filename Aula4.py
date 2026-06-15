#num1= 10
#num2 = 12

#print(num1 == num2)
#print(num1 != num2)
#print(num1 > num2)
#print(num1 < num2)
#print(num1 < num2)
#print(num1 >= num2)
#print(num1 <= num2)

#__________________________________________________________________________________

#Igual ou maior que 18 anos de idade é adulto

#Nome = input("Qual é o seu nome? ")
#Idade = int(input("Qual é sua idade? "))

#verificador = Idade >= 18
#print(verificador)

#___________________________________________________________________________________

#Esta pessoa pode dirigir? Maior de idade e tem que ter carteira de dirigir

#Idade = int(input("Qual é sua idade? "))
#CNH = True

#verificador = Idade >= 18 and CNH

#print(verificador)

#___________________________________________________________________________________

#Verificação de usario e senha

usuario = input("Digite o seu usuario: ")
senha = input("Digite sua senha: ")

login_valido = usuario == "Admin" and senha == "123admin"

print(f"Login Permitido: {login_valido}")