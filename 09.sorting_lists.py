from audioop import reverse


fruits = ['Mango', 'Piña','Durazno','Platano','Arandanos']

#El metodo sort() es destructivo. ya que modifica la lista original

fruits.sort()

print(fruits)

#por defecto ordna ascendente. Con la 'key' revers podemos ordenar en forma descndente

fruits.sort(reverse = True)

print(fruits)

grades = [10,9,10,9,8,8,5]

grades.sort(reverse = True)

print(grades)

cat_bag =['hola', 12, True]

#no es posible comparar entreros con strings
#cat_bag.sort()

print(cat_bag)

veggies = ['papas','quinoa','choclo','papas']

#con el paramtro "key" podmos indicar una funcion para que realice el ordenamiento
veggies.sort(key = str.lower)

print(veggies)

def strLength(elem):
    return len(elem)

#la lista sera ordenada por el largo de los elementos
fruits.sort(key=strLength, reverse = True)

print(fruits)