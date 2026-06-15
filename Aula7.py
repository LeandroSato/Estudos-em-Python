#Lista **PODEM SER ALTERADAS**

frutas = ["Abacate", "Banana", "Morango"]

#print(frutas[2]) #Baseado em index, inicia no zero
frutas.append("Uva")
frutas.append("Laranja")
frutas.remove("Banana")

print(len(frutas)) #tamanho da lista

print(frutas)

#Usando o for

Tarefas = [] 

Tarefas.append("Estudar Python com IA")
Tarefas.append("Ler um artigo sobre IA")
Tarefas.append("Responder e-mails")
Tarefas.append("Lavar o carro")

print("Minhas tarefas de hoje: ")

for Tarefa in Tarefas:
  print(f"Tarefas: {Tarefa}")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Tuplas **Não PODEM SER ALTERADAS**

Meses = ("Janeiro", "Fevereiro", "Março")

print(Meses[1])

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Dicionário **POSSUI CHAVE E VALOR**

Usuario = {
    "Nome": "Leandro",
    "Idade": 19,
    "Departamento": "TI"
}

#Adicionar/Atualizar
Usuario["Idade"] = 20 
Usuario["Cidade"] = "São Paulo"

print(Usuario)

Aluno = {
    "Nome": input("Nome do aluno: "),
    "Idade": int(input("Idade do aluno: ")),
    "Nota": int(input("Nota do aluno: "))
}

print(f"O {Aluno["Nome"]} tem {Aluno["Idade"]} anos de idade e tirou uma nota de {Aluno["Nota"]}!")