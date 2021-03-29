chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    newlist = chunk_one
    for i in chunk_two:
        newlist.append(i)
    return newlist
    
print(merge_list(chunk_one, chunk_two))
