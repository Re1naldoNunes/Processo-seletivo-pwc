from collections import Counter



palavra = input("Digite uma palavra: ")
contador = Counter(palavra)
contagem_impar = 0
for contagem in contador.values():
    if contagem % 2 != 0:
        contagem_impar += 1
    if contagem_impar > 1:
        anagrama_palindromo = False
        break
    
else:
    anagrama_palindromo = True
    
if anagrama_palindromo:
    print("True")
    
else:
    print("False")
