#Com for
ordemLista = input("Digite (c) para ordem crescente ou (d) para odem descrecente")
numeroMaximo = int(input("Digite o numero numero Maximo de repetições"))

if ordemLista == 'c':
    for numero in range(1, numeroMaximo + 1):
        print(numero)
elif ordemLista == 'd':
    for numero in range(numeroMaximo, 0, -1):
        print(numero)
else:
    print("Ordenação invalida")



#Com While
ordemLista = input("Digite (c) para ordem crescente ou (d) para ordem decrescente: ")
numeroMaximo = int(input("Digite o número máximo de repetições: "))

if ordemLista == 'c':
    numero = 1
    while numero <= numeroMaximo:
        print(numero)
        numero += 1
elif ordemLista == 'd':
    numero = numeroMaximo
    while numero >= 1:
        print(numero)
        numero -= 1
else:
    print("Ordenação inválida")
 
 


