from os import system
from sys import exit
from nameVerify import verify

anoAtual = 2023

nome = str(input("Digite seu nome: "))
verify(nome)
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = int(input("Digite sua altura(cm): ")) / 100

anoNasc = (idade - anoAtual) * -1
imc = peso / pow(altura,2)

if input("\nJá fez aniversário esse ano? [Sim] [Não] ") == "Sim":
  pass
else:
  anoNasc = anoNasc - 1

system("clear")
print(f"Olá, {nome}.")
print(f"Idade: {idade} anos.")
print(f"Peso: {peso:.2f}kgs.")
print(f"Altura: {altura:.2f}m.")
print(f"Ano do Nascimento: {anoNasc}")
print(f"IMC: {imc:.2f}")
