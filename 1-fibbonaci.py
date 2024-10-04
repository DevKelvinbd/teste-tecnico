def testeFibonacci(numero):
    a = 0
    b = 1
    
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))
if testeFibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")