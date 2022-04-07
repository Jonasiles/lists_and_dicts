todo_list = ['estudiar python', 'sacar la basuca' ,'alimentar a boby','recibir el bono', 'barrer la entrada']

def check_if_exist(check, list):
    #Revisar si cierto elemento esta en la lista
    if check in list:
        return True

if check_if_exist('recibir el bono', todo_list):
    print('tienes cosas por hacer')
else:
    print('sin bono sigo en cama')