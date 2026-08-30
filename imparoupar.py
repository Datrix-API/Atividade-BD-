def coletando_numero():
    n1 = int(input("Insira um numero: "))
    print (f"O numero escolhido foi {n1}" )
    return n1 


def impar_par(numero):
    if numero % 2 == 0:
        print("O numero escolhido é par")
    else:
        print("O numero escolhido é impar")
    
valor_recebido = coletando_numero()
impar_par(valor_recebido)