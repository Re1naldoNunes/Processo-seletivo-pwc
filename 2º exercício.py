frase = input("Digite aqui: ")
frase_sem_caracteres = ""
for i in frase:
    if i not in frase_sem_caracteres:
        frase_sem_caracteres += i
print(frase_sem_caracteres)
    
        