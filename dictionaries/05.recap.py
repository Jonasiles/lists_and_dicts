programmer = {
    "name":"alice",
    "position":"Fullstack dveloper",
    "skills": ['python', 'git','sql','html','css','Javascript']

}

#Estas variables qudan referencias que se actualizan
keys =programmer.keys()
values = programmer.values()
items = programmer.item()

print(keys)
print(values)
print(items)

#Acá estamos agregando un nuevo item
programmer["dream"]= "Be a Python pro"

#Las llaves se actualizan considerando la nueva llave y valor agregados
print(items)
