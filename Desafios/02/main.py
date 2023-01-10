# Projeto baseado no seguinte link: https://acervolima.com/jogo-de-adivinhacao-de-numeros-em-python-3/
# Adivinhador de Números

import random
from math import log
import sys
import os

continuar = 0
partidasGanhas = 0
partidasPerdidas = 0

while continuar == 0:
  print("Diga um intervalo de número. (Exemplo: 1 a 100): ")
  inicio = int(input("Primeiro número do intervalo: "))
  final = int(input("Último número do intervalo: "))
  
  if len(range(inicio,final)) < 6:
    print("\nHoje não, espertinho. Tem que ter um intervalo maior!")
    sys.exit()
  numero = random.randint(inicio, final)
  
  tentativas = round(log(final - inicio + 1, 2))
  tentativa = 1
  
  while tentativa <= tentativas:
    
    estimativa = int(input("Adivinhe: "))
    
    if estimativa > numero:
      print("Tente novamente! Você adivinhou muito alto!")
      print(f"Tentativa {tentativa} de {tentativas:.0f}")
    elif estimativa < numero:
      print("Tente novamente! Você adivinhou muito baixo!")
      print(f"Tentativa {tentativa} de {tentativas:.0f}")
    else:
      print("Parabéns! Você acertou!")
      print(f"Você resolveu em {tentativa} de {tentativas:.0f} tentativa(s)")
      partidasGanhas = partidasGanhas + 1
      break
    if tentativa == tentativas:
      print("\nVocê atingiu o limite máximo de tentativas, boa sorte da próxima :)")
      partidasPerdidas = partidasPerdidas + 1
      break
    else:
      pass
    tentativa = tentativa + 1

  if input("\n\tContinuar? [S] [N]: ") == "S":
    os.system("clear")
  else:
    os.system("clear")
    print(f"Você jogou {partidasGanhas + partidasPerdidas} partidas.")
    print(f"{partidasGanhas} vitória(s).\n{partidasPerdidas} derrota(s).")
    continuar = 1
  
