programmer = {
    "name":"alice",
    "position":"Fullstack dveloper",
    "skills": ['python', 'git','sql','html','css','Javascript']

}

programmer["position"] = "sr Software Developer"

print(programmer)

programmer.update({"name": "alice smith"})

print(programmer)

programmer.update({"hobbies":["cats", "playstation","contemplate the ,moon"]})

print(programmer["hobbies"])