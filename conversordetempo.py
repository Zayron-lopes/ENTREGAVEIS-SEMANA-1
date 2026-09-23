segundos = int(input("Digite o tempo em segundos: ")) #receber informação digitada
#obs: int é inteiro, então será sem casa decimal

horas = segundos // 3600 #obs: // é divisão inteira
resto = segundos % 3600 #% é resto da divisão

minutos = resto // 60 #obs: // é divisão inteira
segundos_restantes = resto % 60 #% é resto da divisão

print(f"{horas}:{minutos}:{segundos_restantes}") #mostrara o valor do tempo em horas, minutos e segundos