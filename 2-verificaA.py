def verificaA(string):
    
    count = string.lower().count('a')

    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto = input("Informe uma string: ")
verificaA(texto)