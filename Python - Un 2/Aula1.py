#Estrutura de dados pt1

# Objetos do tipo sequência

# Coleções versáteis que podem armazenar vários valores.

# O primeiro elemento da sequência é sempre o índice 0, o segundo pelo índice 1 e assim por diante até o último elemento.

"""
x in s = True caso um item de s seja igual a x, senão false.

s + t = Concatenação de s e t.
         
n * s = Adiciona s a si mesmo n vezes.

s[i] = Acessa o valor guardado na posição i da sequência.

s[i:j] = Acessa os valores da posição i até j.

s[i:j:k] = Acessa os valores da posição i até j, com passo k.

len(s) = Comprimento de s.

min(s) = Menor valor de s.

max(s) = Maior valor de s.

s.count(x) = Número total de ocorrência de x em s.

"""

texto = "Explorando funcionalidades de estruturas de dados com Python"

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de 'e' no texto = {texto.count('e')}")
print(f"As 5 primeiras letras são = {texto[:5]}")
print()

# Listas

cores = ["amarelo", "azul", "preto", "cinza", "vermelho"]

for cor in cores:
    print(f"Posição = {cores.index(cor)}, cor = {cor}")

print()

#List Comprehensions, Map e Filter
#Função lower
langs = ["Python", "PHP", "JavaScript", "NodeJS", "C", "C++", "C#", "Go"]
print("Antes da listcomp =", langs)
langs = [item.lower() for item in langs]
print("\nDepois da listcomp = ", langs)

#map() e filter() são usadas para manipular listas e aplicar transformações ou filtragens a elementos iteráveis.

precos_em_dolar = [100,50,75,120]
taxa = 5.25
precos_em_reais = list(map(lambda x : x * taxa, precos_em_dolar))

print(precos_em_reais)
print()
# map() é usada para aplicar uma função lambda que multiplica o preço em dólares pela taxa de câmbio. Depois, convertemos o resultado em uma lista. O resultado será uma lista com os preços em reais

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_pares = list(filter(lambda x:x%2 == 0, numeros))

print(numeros_pares)

#Nesse caso, usamos a função filter() com uma função lambda que verifica se um número é par(resto da divisão por 2 igual a 0), em seguida, convertemos o resultado em uma lista. resultado = uma lista contendo apenas os números pares.

#Tuplas

#São estruturas de dados pertencentes ao grupo de objetos do tipo sequência em Python. A diferença entre listas e tuplas é o fato de que as listas serem mutáveis, permitindo a atribuição de valores a posições específicas, enquato as tuplas são objetos imutáveis.

# 3 maneiras de criar tuplas;
"""
    1.Usando um par de parênteses para denotar uma  tupla vazia: tupla1 = ()
    
    2.Usando um par de parênteses e elementos separados por vírgulas: tupla2 = ('a','b','c')

    3.Usando o construtor de tipo tuple()

"""

# Um exemplo

vogais = ('a','e','i','o','u')
print(f"\nTipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"\nPosição = {p}, valor = {x}")
    

# A função enumerate() é utilizado para obter tanto a posição quanto o valor de cada elemento na tupla. É importante observar que as tuplas são imutáveis, o que significa que, uma vez criadas, não é possível alterar seu conteúdo.    

# Exercício
# Convidados

convidados = ("Andre", "Bob", "Caroline", "Davi", "Elaine")

confirmados = ["Andre", "Davi"]

nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

print("\nConvidados que ainda não confirmaram:")
for pessoa in nao_confirmados:
    print(pessoa)
    
print("\nEnviando lembretes para os convidados que ainda não confirmaram.")    
    

