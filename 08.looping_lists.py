from operator import index


todo_list = ['estudiar python', 'sacar la basuca' ,'alimentar a boby','recibir el bono', 'barrer la entrada']

for todo in todo_list:
    print(todo)

    index=0
    while index < len(todo_list):
        print(todo_list[index])
        index +=1

#El indice termina en 5 por la ultima iteracion
print(index)

#utilizando list comprehemsions
[print(todo) for todo in todo_list]
