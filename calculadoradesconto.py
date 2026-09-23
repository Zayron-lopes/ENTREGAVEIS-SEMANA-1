preco = float(input("Digite o preço do produto: R$ ")) #receber informação digitada
desconto = float(input("Digite o percentual de desconto: ")) #obs: float, então será com casa decimal
#obs: float, então será com casa decimal

valor_desconto = preco * desconto / 100 #calcular o valor do desconto
preco_final = preco - valor_desconto #calcular o preço final

print(f"Preço final: R$ {preco_final:.2f}") #mostrara o valor do preço final com duas casas decimais