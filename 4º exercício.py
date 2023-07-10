import re

texto = input ("Digite sua frase :")
frases = re.split(r'(?<=[.!?])\s+', texto)
frases_pegas = [frase.capitalize() for frase in frases]
texto_pego = ' '.join(frases_pegas)
print(texto_pego)