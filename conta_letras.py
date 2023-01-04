#conta_letras

poema = input('escrva alguma coisa: ')

numeral = 0

for letra in poema:
    if letra.isalpha():
        numeral = numeral + 1

mensagem = 'o numero de letras foi ' 

print(mensagem, numeral)

