todo_list = ['estudiar python', 'sacar la basuca' ,'alimentar a boby','recibir el bono', 'barrer la entrada']

# Podemos eliminar un elemento en particular
todo_list.remove('recibir el bono')

print(todo_list)

#el metodo pop() remueve el ultimo y lo retorna. tambien acepta indice
Element = todo_list.pop()

print(todo_list)
print(Element)

#Tambien existe la palabra clave "del"
del todo_list[1]
print(todo_list)

# esto lo elimina del programa
del todo_list

todo_list = ['estudiar python', 'sacar la basuca' ,'alimentar a boby','recibir el bono', 'barrer la entrada']

#limpiar toda la lista pero no la elimina
todo_list.clear()

print(todo_list)