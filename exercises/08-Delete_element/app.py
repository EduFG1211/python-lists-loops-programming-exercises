people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    newpeople = []
    for i in people:
        if(i != person_name):
            newpeople.append(i)
    return newpeople
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))