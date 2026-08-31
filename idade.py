def coletando_dados():
    idade = int(input("Insira a sua idade: "))
    return idade

def resultado_idade(idade):
    if idade <= 12:
        print("Voce é crianca: ")
    elif idade >= 13 and idade <= 18:
        print("Voce e adolescente ")
    else:
        print("Voce e adulto")

idade_recebida = coletando_dados()
resultado_idade(idade_recebida)