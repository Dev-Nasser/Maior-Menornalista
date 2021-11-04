resposta = ("S")
n = 0
soma = 0
quantidade = 0
lista = [0]

while resposta == "S":
    NumeroSoma= int(input("Digite um número para a soma"))
    resposta = str(input("Deseja continuar? Digite a letra s se sim")).upper()
    n = n + NumeroSoma
    quantidade = quantidade + 1
    lista.append(NumeroSoma)


print ("O resultado da sua operação foi de {}".format(n))
print ("Divisão de {} por {}".format(n , quantidade))
print ("O resultado da divisão entre os termos é de {}".format(n/quantidade))
print ("O maior numero da lista é {}".format(max(lista)))
print ("O menor numero da lista é {}".format(min(lista)))
