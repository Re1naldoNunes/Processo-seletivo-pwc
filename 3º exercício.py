
frase = input("Digite uma frase: ")
frase = frase.replace(" ", "").lower()
palindromos = []
for i in range(len(frase)):
    for j in range(i + 1, len(frase) + 1):
        substring = frase[i:j]
        if len(substring) >= 3 and substring == substring[::-1]:
            palindromos.append(substring)

if len(palindromos) > 0:
    saida = "Palíndromos encontrados:\n" + "\n".join(palindromos)
else:
    saida = "Nenhuma substring palindrôma foi encontrada"

print(saida)