#Crie uma lista dos quadrados dos primeiros n números naturais
def quadrados(n):
    return [i**2 for i in range(1, n+1)]

print(quadrados(10))

#Crie uma função que recebe uma lista de números e retorna a soma dos quadrados dos números pares
def soma_quadrados_pares(lista):
    return sum([i**2 for i in lista if i % 2 == 0])

print(soma_quadrados_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Crie uma função que recebe uma lista de números e retorna a soma dos quadrados dos números ímpares
def soma_quadrados_impares(lista):
    return sum([i**2 for i in lista if i % 2 != 0])

print(soma_quadrados_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#Crie uma função que recebe uma lista de números e retorna a soma dos quadrados dos números primos
def soma_quadrados_primos(lista):
    return sum([i**2 for i in lista if eh_primo(i)])

print(soma_quadrados_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))