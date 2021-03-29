contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
#print(contact.keys())
#print(contact.values())
#print(contact.items())
new1 = []
new2 = []
for i in contact.keys():
    new1.append(i)
for j in contact.values():
    new2.append(j)
for k in range (0,len(contact),1):
    print(new1[k]+' : '+new2[k])

