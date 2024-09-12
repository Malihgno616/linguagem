# CLASSES E MÉTODOS EM PYTHON

"""
    Atributos: são os dados que representam o estado do objeto, como nome e idade.
    
    Métodos: definem o comportamento do objeto, indicando as ações que ele pode executar, como cumprimentar ou fazer login.
    
    Encapsulamento: combina atributos e métodos em uma entidade, permitindo controlar o acesso a atributos por meio de métodos.
   
    Herança: possibilita que uma classe herde atributos e métodos de outra, promovendo o reúso de código e a organização hierárquica, como na relação entre as classes pessoa, funcionário e cliente.
   
    Polimorfismo: refere-se à capacidade de várias classes responderem de forma diferente a uma mesma mensagem, graças à herança e às respostas específicas de cada classe às mensagens.
"""

class Pessoa:
    
    def __init__(self,  nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
    def cumprimentar(self):
        
        return f"Olá, meu nome é {self.nome}."
    
    def aniversario(self):
        self.idade += 1
        
     
pessoa1 = Pessoa("João", 30,"Masculino")        
        
print(pessoa1.cumprimentar())

print(f"Idade: {pessoa1.idade}")

pessoa1.aniversario()

print(f"Nova idade: {pessoa1.idade}")

#Herança em Python

"""
    Benefícios da herança
    Reutilização de código: a herança permite que você reutilize o código existente, aproveitando a estrutura e a funcionalidade de classes-pai em suas subclasses.
    Extensibilidade: você pode estender ou adicionar comportamentos específicos às classes-filhas sem modificar as classes-pai, mantendo a coesão e a organização do código.
    Hierarquia de classes: é possível criar uma hierarquia de classes na qual classes-filhas podem herdar características comuns de classes-pai e, por sua vez, serem herdadas por outras classes.
"""

class Animal:
    
    def __init__(self, nome):
        self.nome = nome
        
    def fazer_barulho(self):
        pass
    
class Cachorro(Animal):
   
    def fazer_barulho(self):
        return "Latir"

class Gato(Animal):
    
    def fazer_barulho(self):
        return "Miar"    
    
rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

print(f"\n{rex.nome} faz: {rex.fazer_barulho()}")
print(f"{whiskers.nome} faz:{whiskers.fazer_barulho()}")

## Exercicio de Classe

class Veiculo:

    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
    def acelerar(self, incremento):
        
        self.velocidade += incremento
    
    def frear(self, decremento):
        
        self.velocidade -= decremento
        
    
    def status(self):
        
        return f"Marca:{self.marca}, Modelo:{self.modelo}, Ano:{self.ano}, Velocidade:{self.velocidade}km/h" 
    
class Carro(Veiculo):
    
    def __init__(self, marca, modelo, ano, potencia):
        
        super().__init__(marca, modelo, ano)
    
        self.potencia = potencia
    
    def acelerar(self, incremento):
        
        self.velocidade += incremento + self.potencia
    
class Bicicleta(Veiculo):
    
    def __init__(self, marca, modelo, ano, tipo):
        
        super().__init__(marca, modelo, ano)
        
        self.tipo = tipo
        
    def status(self):
        
        return f"Marca: {self.marca}, Modelo:{self.modelo}, Ano:{self.ano}, Tipo:{self.tipo}, Velocidade:{self.velocidade} km/h"   
        
carro1 = Carro("Toyota","Corolla",2022, 150)

bicicleta1 = Bicicleta("Trek", "Mountain Bike", 2021, "MTB")

carro1.acelerar(50)

bicicleta1.acelerar(20)

print("Status do Carro:")

print(carro1.status())


print("\nStatus da Bicicleta:")

print(bicicleta1.status())







        