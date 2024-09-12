#Estruturas de Dados Pt2
#Objetos do tipo set

"""  
     Os objetos do tipo “set” habilitam operações de conjuntos, como união, interseção, diferença e muitas outras. Essa estrutura é especialmente útil para realizar testes de associação e eliminar valores duplicados em uma sequência.
"""

"""
    Em Python, existem duas formas principais de criar objetos do tipo “set”:

    Usando um par de chaves e elementos separados por vírgulas, por exemplo: set1 = {'a', 'b', 'c'}.

    Usando o construtor de tipo set(iterable) com um objeto iterável, como uma lista, uma tupla ou mesmo uma sequência de caracteres (string).
"""

#add(valor) e remove(valor)

# Criando um conjunto vazio

meu_conjunto = set()

meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

print("Conjunto após adicionar elementos:", meu_conjunto)

#Verificar se o 20 está em nosso conjunto

elemento = 20
if  elemento in meu_conjunto:
    print(f"O elemento {elemento} está no conjunto")
else:
    print(f"O elemento {elemento} não está no conjunto")

#removendo elemento
meu_conjunto.remove(20)

#imprimindo o conjunto atualizado
print(f"Conjunto após remover o elemento {elemento}:", meu_conjunto)
print()

#Objetos do tipo mapping
#Estrutura de Dados que estabelecem uma relação entre chaves e valores.
#Exemplo: Dicionários.

#Representado pelo tipo dict

"""
Podemos Criar dicionários em Python das seguintes maneiras:
1. Usando um par de chaves para denotar um dicionário vazio: dicionario1= {}
2. Usando pares de elementos na forma "chave: valor"
separados por vírgulas: dicionário2 = {'um':1,'dois':2,'tres':3}.
3. Usando o construtor de tipo dict
"""

#Veja aqui o exemplo

# Primeiro exemplo
dict1 = {}
dict1['nome'] = "Maria"
dict1['idade'] = 25

print(dict1)
print()

# Segundo exemplo
dict2 = {'nome':"Maria",'idade': 25}
print(dict2)
print()

# Terceiro exemplo 
dict3 = dict([('nome',"Maria"), ('idade',25)])
print(dict3)
print()

# Quarto exemplo
dict4 = dict(zip(['nome','idade'], ['Maria',25]))
print(dict4)
print()

#Teste se todas as construções resultam em objetos iguais

print(dict1 == dict2 == dict3 == dict4)
print(dict1)
print()

#Objetos do tipo array NumPy

#importar a biblioteca NumPy

#Array com NumPy
import numpy as np

my_array = np.array([1,2,3,4,5])

print("Array original:")
print(my_array)

#Realize operações matemáticas com o array

squared_array = my_array ** 2

sum_of_elements =np.sum(my_array)

print("\nArray ao quadrado:")
print(squared_array)

print("\nSoma dos elementos:")
print(sum_of_elements)

#Acesse elementos do array

element_at_index_2 = my_array[2]

print("\nElemento no índice 2:", element_at_index_2)

# Exercício

# importe as bibliotecas necessárias

import numpy as np

# dados dos participantes

participantes = [
    {
        "nome":"Alice",
        "localizacao": "EUA",
        "afiliacao":"Universidade A",
        "interesses":["Física","Astronomia"]
    },
    {
        "nome":"Bob",
        "localizacao": "Brasil",
        "afiliacao":"Instituto B",
        "interesses":["Biologia","Astronomia"]
    },
    {
        "nome":"Charlie",
        "localizacao": "Índia",
        "afiliacao":"Instituto C",
        "interesses":["Química","Engenharia"]
    }
]

    #adicione mais participantes conforme necessaário
    
    #Usando sets par identificar diferentes regiões dos participantes
    
regioes = set(participante["localizacao"] for participante in participantes)

    #Usando um dicionario para categorizar afiliações

afiliacoes = {}

for participante in participantes:
    
    afiliacao = participante["afiliacao"]
        
    if afiliacao not in afiliacoes:
        
        afiliacoes[afiliacao] = []
    
    afiliacoes[afiliacao].append(participante["nome"])    
        
   #Usando NumPy para analisar áreas de interesse
   
    areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])
    
    interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
    
    area_mais_popular = interesses_unicos[np.argmax(contagem)]
    
    print("\nRegiões dos participantes:", regioes)
    
    print("Afiliações dos participantes:")
    
    for afiliacao, nomes in  afiliacoes.items():
        print(f"{afiliacao}:{','.join(nomes)}")

    print("Area de interesse mais popular:", area_mais_popular)