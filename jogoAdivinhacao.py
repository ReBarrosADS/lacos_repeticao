## escreva um programa que sorteia um valor de 1 a 100. 
# O jogador pode então tentar acertar o menor ou maior que o valor sorteando. 
# O processo se repete ate que o jogador acerte o valor sortiado
# Refatore o codigo para ao final moste quantas tentativas foram antes de acerta

from random import randint

numeroSorteado = randint(1, 100)
tentativa = 0

while tentativa != numeroSorteado:
    numeroChute = int(input("Tente acertar o número entre 1 e 100: "))
    tentativa += 1

    if numeroChute == numeroSorteado:
        print(f"Parabéns, você acertou em {tentativa} tentativas!!")
        break
    elif numeroChute > numeroSorteado:
        print("Número sorteado é menor, tente novamente!")
    elif numeroChute < numeroSorteado:
        print("Número sorteado é maior, tente novamente!")