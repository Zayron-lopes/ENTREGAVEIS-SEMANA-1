valor_compra = float(input("Digite o valor da compra: R$ ")) #receber informação digitada
valor_pago = float(input("Digite o valor pago: R$ ")) #receber informação digitada

#obs: float, então será com casa decimal

troco = valor_pago - valor_compra #A - B = X

print(f"Troco: R$ {troco:.2f}") #mostrara o valor do troco com duas casas decimais