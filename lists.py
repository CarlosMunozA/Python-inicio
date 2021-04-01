lala = [1,23,12,[True,2, 'lala']]

colors=['red','green','white']

numberList = list((1,2,3,4))
#print (type(numberList))

#range crea listas con los número del 1 al 9 en este caso
#r= list(range(1,10))
#print(r)
# print(dir(colors))
# #len=largo de la lista  
# print(len(colors))
# print(len(lala))

#pregunta si existe green en colors
# print('green' in colors) 
# print(colors)

# colors[1]='black'
# print(colors)
#colors.append('violet')
#print(colors)

#Le agrega los elementos dentro de la lista
#colors.extend(['brown','yellow','pink'])
#print(colors)

#insertar el valor en la posición 1
#colors.insert(1,'violet')

#insertar el valor en la última posición
colors.insert(len(colors),'violet')

#elimina el ultimo elemento
#colors.pop()

#elimina los colores que se llamen green
#colors.remove('green')

#elimina el elemento ubicado en la pocisión 2
#colors.remove(colors[1])
#borra los elementos del arreglo
#colors.clear()

#ordenar por orden del alfabeto
#colors.sort() 
#ordena en forma de la z a la a
#colors.sort(reverse=True)
#pregunta la posición del elemento red
#print(colors.index('red'))
print(colors.count('violet'))