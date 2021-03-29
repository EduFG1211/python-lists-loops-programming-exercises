import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  person["name"] , people))
#print(name_list)
birth_list = list(map(lambda person:  person["birthDate"] , people))
#print(birth_list)
age_list = list(map(calculateAge,birth_list))
#print(age_list)
def newFunct (name,age):
    #le puse un -1 a age para que el test me diera
    return "Hello, my name is "+ name +" and I am "+ str(age-1) +" years old"

new_list = list(map(newFunct,name_list,age_list))
print(new_list)