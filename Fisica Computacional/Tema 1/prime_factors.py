# Se pide: calcular los factores primos de un número natural arbitrariamente grande (n)

def prime_factors(n: int) -> list[int]:
    factors = []
    for i in range(2, n+1):
        while not n%i: # Si el número i es divisor de n (es factor primo)
            factors.append(i)
            n//=i # Le quito el factor primo hallado
    return factors

print(prime_factors(9))