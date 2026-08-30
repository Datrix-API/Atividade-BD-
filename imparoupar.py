#Aqui eu criei uma funcao que coleta o numero inserido pelo usuario
def coletando_numero():
    n1 = int(input("Insira um numero: "))
    print (f"O numero escolhido foi {n1}" )
    return n1 

#Na segunda funcao, faz o tratamento de dados
#Na primeira linha do if, eu pego o numero inserido e divido por 2
#Se o resto da divisao for 0, o numero é par.
#Caso o resto da divisao for 1, entao o numero é impar
def impar_par(numero):
    if numero % 2 == 0:
        print("O numero escolhido é par")
    else:
        print("O numero escolhido é impar")

#Aqui eu to apenas chamando as funcoes    
valor_recebido = coletando_numero()
impar_par(valor_recebido)