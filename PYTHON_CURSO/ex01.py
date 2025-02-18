#input retorna o valor de uma string por isso você precisa convertê-lo para um número usando int() ou float() antes de realizar operações matemáticas.
nota01 = float(input("Sua primeira nota: "))
nota02 = float(input("Sua segunda nota: "))
nota03 = float(input("Sua terceira nota: "))

#utilizar o parentese pois o Python segue a ordem de precedência de operadores
media = (nota01 + nota02 + nota03) / 3

print(f"Notas: {nota01}, {nota02}, {nota03} | Média: {media:.2f}")