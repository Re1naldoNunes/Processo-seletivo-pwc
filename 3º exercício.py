frase = input ("Digite uma frase:" )
frase = frase.replace (" ", "").lower()
palindromos = []
for i in range(len(frase)):
    for j in range (i + 1, len(frase) + 1):
        substring = frase[i:j]
        if len(substring) >= 3 and substring == substring [::-1]:
            palindromos.append(substring)

if len(palindromos) > 0:
    for palindromo in palindromos:
        print (palindromo)
else:
    print ("Nenhuma substring palindrôma foi encontrada")