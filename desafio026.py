frase = str(input('Digite uma frase: ')).strip().lower()
letra = str(input('Escolha uma letra para analisar a frase: ')).lower().strip()

print(f'A letra {letra} apareceu {frase.count(letra)} vezes.')
print(f'A primeira aparição da letra {letra} foi na {frase.find(letra)+1}º posição.')
print(f'A ultima vez que a letra {letra} apareceu foi na {frase.find(letra)+1}º posição.')