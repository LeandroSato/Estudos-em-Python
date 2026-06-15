# Aula 1

## Funções

| Função | Descrição |
|--------|-----------|
| `print()` | Mostrar na tela |
| `type()` | Mostrar o tipo de variável |
| `input()` | Receber dados do usuário |
| `int()` | Converter para inteiro |

---

# Aula 2

Contas matemáticas básicas, f-string e conversão de tipos

---

# Aula 3 + Desafio

## Mais contas matemáticas

| Operador | Descrição |
|----------|-----------|
| `+` | Soma |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `//` | Divisão inteira |
| `%` | Resto da divisão |
| `**` | Potenciação |

---

# Aula 4

## Operadores relacionais

Usados para comparar valores e retornar um valor booleano (True ou False)

| Operador | Descrição |
|----------|-----------|
| `==` | Igual |
| `!=` | Diferente |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual a |
| `<=` | Menor ou igual a |

## Operadores lógicos

Usados para combinar expressões booleanas

| Operador | Descrição |
|----------|-----------|
| `and` | E |
| `or` | Ou |
| `not` | Não |

---

# Aula 5

##Condições

| Estrutura | Descrição |
|-----------|-----------|
| `if` | Se |
| `elif` | Senão se |
| `else` | Senão |

#Sempre colocar em ordem (de cima para baixo do mais específico 
#para o mais geral, ou seja, do maior para o menor.)

---

# Aula 6

## Looping

| Estrutura | Descrição |
|-----------|-----------|
| `while` | Enquanto (repete enquanto a condição for verdadeira) |
| `for` | Para (repete para cada item de uma sequência) |

| Estrutura | Quando usar |
|-----------|-------------|
| `for` | Quando se sabe a quantidade de repetições |
| `while` | Quando não se sabe a quantidade de repetições |

---

# Aula 7

## Listas, Tuplas e Dicionários

### Listas

Coleção ordenada e **mutável** de elementos. Aceita itens de tipos diferentes.

```python
frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4, 5]
misto = [1, "texto", True]
```

**Acesso por índice** (começa no 0):

```python
frutas[0]   # "maçã"
frutas[-1]  # "uva" (último elemento)
```

**Métodos principais:**

| Método | Descrição |
|--------|-----------|
| `.append(x)` | Adiciona `x` ao final |
| `.insert(i, x)` | Insere `x` na posição `i` |
| `.remove(x)` | Remove a primeira ocorrência de `x` |
| `.pop(i)` | Remove e retorna o elemento da posição `i` |
| `.sort()` | Ordena a lista |
| `.reverse()` | Inverte a ordem |
| `len(lista)` | Retorna o tamanho da lista |

---

### Tuplas

Coleção ordenada e **imutável** de elementos. Não pode ser alterada após criada.

```python
coordenadas = (10, 20)
cores = ("vermelho", "verde", "azul")
```

**Acesso por índice** (igual às listas):

```python
cores[0]   # "vermelho"
cores[-1]  # "azul"
```

> Use tuplas quando os dados não devem ser modificados (ex: coordenadas, dias da semana).

---

### Dicionários

Coleção de pares **chave: valor**, não ordenada e **mutável**.

```python
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}
```

**Acesso por chave:**

```python
pessoa["nome"]    # "João"
pessoa["idade"]   # 25
```

**Métodos principais:**

| Método | Descrição |
|--------|-----------|
| `.keys()` | Retorna todas as chaves |
| `.values()` | Retorna todos os valores |
| `.items()` | Retorna pares (chave, valor) |
| `.get(chave)` | Retorna o valor sem erro se não existir |
| `.update({...})` | Atualiza ou adiciona pares |
| `del dicio[chave]` | Remove uma chave |

---

### Comparativo

| Tipo | Ordenado | Mutável | Acesso |
|------|----------|---------|--------|
| Lista | Sim | Sim | Por índice |
| Tupla | Sim | Não | Por índice |
| Dicionário | Não | Sim | Por chave |

---

# Aula 8

## Funções

Bloco de código que é escrito uma vez e pode ser utilizado várias vezes.

```python
def nome_da_funcao(parametros):
    # código
    return resultado
```

### Organização

| Prática | Descrição |
|---------|-----------|
| Separar em arquivos | Criar arquivos diferentes para organizar o código |
| Reutilizar funções | Importar e chamar funções entre arquivos |

# Segue o link do trabalho: https://github.com/LeandroSato/Python-Fun-es.git