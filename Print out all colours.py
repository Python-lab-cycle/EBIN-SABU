#print out all colours from colour list1 not contained in colour list2
colour_list_1=set(["white","black", "red"])
colour_list_2=set(["red","green"])
print(colour_list_1.difference(colour_list_2))
