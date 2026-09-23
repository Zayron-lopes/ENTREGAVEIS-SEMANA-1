numero = int(input("Digite um número inteiro: ")) #receber informação digitada
#obs: int é inteiro, então será sem casa decimal

if numero % 2 == 0: #% é resto da divisão, == é igual a, então se o resto da divisão do número por 2 for igual a 0, o número é par
    print("O número é par.")
else: #else é caso contrário, então se o resto da divisão do número por 2 não for igual a 0, o número é ímpar
    print("O número é ímpar.") #mostrar na tela