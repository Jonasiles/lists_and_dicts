todo_list = ['estudiar python', 'sacar la basuca' ,'alimentar a boby','recibir el bono', 'barrer la entrada']

#Agrega un item en el indice del primer parametro, desplazando otros item.
todo_list.insert(2,'bañarme')

# Agrega al final 
todo_list.append('Ver friends')

print(todo_list)

#Mezclar
movies = ['el dia de la indpendencia','American pie', 'Scary Movie']

books = ['Harry potter', 'the bro code', 'Como entrenar a tu dragon']

#Agrega al final todo el arreglo entrgado como parametro
movies.extend(books)

print(movies)

print(books)