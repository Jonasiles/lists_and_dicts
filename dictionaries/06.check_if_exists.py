programmer = {
    "name":"alice",
    "position":"Fullstack dveloper",
    "skills": ['python', 'git','sql','html','css','Javascript']

}

if "position" in programmer:
    print('Existe la posicion')

if "alice" in programmer:
    print("Alice esta presente")

if "alice" in programmer.values():
    print("alice sta en los valores")
    