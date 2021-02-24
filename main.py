# Outra forma de comentario, com texto maior.
'''
Autor: Hugo
Data: 16/02/2021
Version: 1.0
'''

# Meu primeiro codigo para print
print('Meu primeiro codigo para print')
print("teste")
print('Olá, tudo bem')

# Meu Segundo codigo para print
print('Terca-feira')

print()

#### Estudo de Variable
print('Estudo de Variable')
x = 2
print(x)
print(x + x)

y = 'Ola'
print(y)

w = 2.4
print(w)
print(w + w)

print()

#### Manipulcao do tipo da variable
print('Manipulcao do tipo da variable')

a = str(2) #Passando o tipo da variable, nesse caso string
b = int(4) #Passando o tipo da variable, nesse caso Interge
c = float(5) #Passando o tipo da variable, nesse caso Float 

print(a + a)
print(b + b)
print(c + c)

print()

#### Praticando com String e Interge
print('Praticando com String e Interge')

# O Andre tem 24 anos de idade e mora em Sao Paulo.

nome = 'Andre'
idade = str(24)
mora = 'Sao Paulo'

#Em um print nao e possivel concatenar uma variavel interge e string. Nesse caso, convertemos a idade em string para ficar tudo todas as variavel do tipo string.
print('O ' + nome + ' tem ' + str(idade) + ' anos de idades e mora em ' + mora + '.')

#Segue outra maneira de manipular a variavel no corpo do print de interge para string.
nome2 = 'Andre'
idade2 = 24
mora2 = 'Sao Paulo'

print('O ' + nome2 + ' tem ' + str(idade2) + ' anos de idades e mora em ' + mora2 + '.')

