#funciones ya establecidas
# print()
# dir()
# type()

#crear función def hace referencia a creacion de una funcion

# def hello(name='Person'):
#     print('Hello ' + name.upper())

# hello('Carlos')
# hello('Juan')
# hello('Pedro')
# hello(  )

# def add(numberOne,numberTwo):
#     return numberOne+numberTwo

# print (add(4,5))
# print (add(numberOne=int (input('Num 1')),numberTwo= int(input('Num 2'))))

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10, 30))