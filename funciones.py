from sympy import isprime

def es_primo(n: int) -> bool:
    return isprime(n)
    
def es_primo_a_mano(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
