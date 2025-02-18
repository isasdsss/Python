
#arrendondar valores
num = 2.7893839
print(num)
print(round(num, 1))  #arrendonda uma casa
print(round(num))

#retorna a quuantidade de elementos de qualquer lista/len

lista = [1,2,3,4,5,6,7,8,9]
dicionario = {'Nome:':'Isack'}
tupla = (1,2,3,4,5,6)


print(len(tupla))
print(len(dicionario))
print(len(lista))



#Fatiamento de string
string = "Oolá mundooo!"

cpf = 'Cpf: 123456789'
print(type(string))
print(len(string))
print(string[2])  #acessa a posiçao da sua string
print(string[0:4]) 
print(cpf[-9:])


#Manipular strings - 12 funções para manipular uma string 

nome = 'manipulando uma string'
print(nome)


#substituir algo
print(nome.replace('string', 'sequencia de caracteres'))
print(nome.replace('uma string', ''))



print(nome.startswith('string'))  #starswith/verifica o começo
print(nome.endswith('string'))   #endswith/verifica o fim

print(nome.count("m"))#count/quantas vezes o valor aparece

print(nome.capitalize()) #primeira letra maiuscula

print(nome.isdigit()) #verifica se tem um valor numerico


nome2 = 'teste num 2'
print(nome2.isalnum())

 
nome3 = 'rua la paz, jardim america, 889'

print(nome.upper()) #transforma em maiuscula
print(nome.lower()) #transofrma em minuscula
print(nome.find("uma")) #localiza a posicao do cstring
print(nome.strip()) #remove os caracteres do começo e do fim
print(nome3.split('')) #quebra a string

