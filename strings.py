myStr = "Carlos"

print(myStr)
print('my name is '+ myStr)
#el f antes del texto indica que se añadira una variable
print(f'my name is {myStr}')
#el valor que ira dentro de los corchetes es el de la variable
print('my name is {}'.format(myStr))

#imprime todo lo que se puede hacer con myStr
#print(dir(myStr))  

# #todo con mayusculas
# print(myStr.upper())
# #todo con minusculas
# print(myStr.lower())
# #cambia minusculaspor mayusculas
# print(myStr.swapcase())
# #Solo la primera mayuscuka
# print(myStr.capitalize())

# #reemplazar hola por chao
# myStr = (myStr.replace('Hello','bye').upper())
# #contar las i
# print(myStr.count('i'))
# #contar espacios
# print(myStr.count(' '))

# #ver si empieza la palabra BYE
# print(myStr.startswith('BYE'))
# #ver si termina con la palabra World
# print(myStr.endswith('World'))
# print(myStr)
# #separa el texto, por defecto lo hace por un espacio
# print(myStr.split())
# #para que separe por comaSs
# print(myStr.split(','))
# #POSICIÓN DE LA LETRA O 
# print(myStr.find('O'))
# #muestra el largo de la variable
# print(len(myStr))
# #mostrar el indice en el que se encuentra la letra E
# print(myStr.index('E'))
# #saber si la variable es numerica
# print(myStr.isnumeric())
# #saber si la variable no es numerica
# print(myStr.isalpha())
# #imprimir el valor en la posición 4
# print(myStr[4])
# print(myStr[-1])