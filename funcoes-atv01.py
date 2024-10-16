# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.



def verificar_pariedade():
    numero = int(input("Digite o número: "))
    if numero %2 == 0:
        return "É um número par"
    else:
        return "É IMPAR"
    
k = verificar_pariedade()
print(k)
    