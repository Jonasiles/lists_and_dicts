programmer = {
    "name":"alice",
    "position":"Fullstack dveloper",
    "skills": ['python', 'git','sql','html','css','Javascript']

}

#el metodo pop en los diccionarios requiere las llaves a eliminar
#position = programmer.pop("position")
#print(programmer)
#print(position)
del programmer["position"]
print(programmer)


#eliminar diccionario
del programmer
#print(programmer) esto es un error al eliminar el programmer del programa

programmer = {
    "name":"alice",
    "position":"Fullstack dveloper",
    "skills": ['python', 'git','sql','html','css','Javascript']

}

#Vaciar el contenido del diccionario, pero manteniendo la variabl
programmer.clear()

print(programmer) # {} es lo que se imprime