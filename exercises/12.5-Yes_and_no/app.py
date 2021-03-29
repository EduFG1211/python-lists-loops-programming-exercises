theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def replacebool (num):
    if num == 1:
        word = 'wiki'
    else:
        word = 'woko'
    return word

new_list=list(map(replacebool,theBools))
print(new_list)


