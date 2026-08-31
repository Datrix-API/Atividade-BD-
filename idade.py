#Coleta a idade do usuario
def coletando_dados():
    idade = int(input("Insira a sua idade: "))
    return idade

#Funcao de tratamento de dados
def resultado_idade(idade):
    #Se a idade for MENOR ou IGUAL a 12 = CRIANCA
    if idade <= 12:
        print("Voce é crianca: ")

    #Se a idade for MAIOR/IGUAL a 13 OU MENOR/IGUAL 18 = ADOLESCENTE    
    elif idade >= 13 or idade <= 18:
        print("Voce e adolescente ")

    #Se nao for nenhuma das opcoes acima, entao o usario é ADULTO
    else:
        print("Voce e adulto")

idade_recebida = coletando_dados()
resultado_idade(idade_recebida)