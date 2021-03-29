all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(list):
    return list["sexy"] == True
def generate_li(item):
    return "<li>"+item+"</li>"

doneColor = list(filter(filter_colors, all_colors))
doneColor2 = list(map(lambda x : x["label"], doneColor))
doneColor3 = list(map(generate_li,doneColor2))
#print(doneColor3)
string = ""
for i in doneColor3:
    string += i
print(string)


