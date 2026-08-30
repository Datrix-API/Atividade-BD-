#programa para calcular o valor lógico de 
#p or (q or r)
p = input("Digite o valor lógico de p (True ou False): ").strip().lower()=="true"
q = input("Digite o valor lógico de q (True ou False): ").strip().lower()=="true"
r = input("Digite o valor lógico de r (True ou False): ").strip().lower()=="true"
if p or (q and r):
    print("O valor lógico da expressão p or (q and r) é: Verdadeiro")
else:
    print("O valor lógico da expressão p or (q and r) é: Falso")