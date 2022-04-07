#Los diccionarios son estructuras similares a las listas o arreglos, pero s accede a sus elemntos mediante "llaves" o "keys" y no por su indice

#Ejemplo
#Definimos un diccionario utilizando llaves o "curly bracs"
programmer = {
    "name":"alice",
    "position":"Fullstack dveloper",
    "skills": ['python', 'git','sql','html','css','Javascript']

}

#accedemos a los elementos por la llav
print(programmer['name'])
#no podmos acceder por el indice
#print)programmer[0])
print(programmer['position'])
print(programmer['skills'])

#tambin podemos acceder a sus elementos con el metodo get()
print(programmer.get("position"))

#son de tipo <class 'dict'>
print(type(programmer))

#podemos acceder a todas sus llaves on el metodo keys()
keys=programmer.keys()
print(keys)
