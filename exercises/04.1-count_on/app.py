
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []
typelist = []
typeobject = {}
for i in my_list:
    if (type(i) == type(typelist) or type(i) == type(typeobject)):
        hello.append(i)
print(hello)
