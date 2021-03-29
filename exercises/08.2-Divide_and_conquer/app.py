list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(lists):
    even = []
    odd = []
    for i in lists:
        if(i % 2 != 0):
            odd.append(i)
        else:
            even.append(i)
    newlist = [odd,even]
    return newlist

print(merge_two_list(list_of_numbers))

