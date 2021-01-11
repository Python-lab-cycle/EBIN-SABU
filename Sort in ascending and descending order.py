d={1:2,3:4,4:3,2:1,0:0}
print('orginal dictionary:',d)
sorted_d=sorted(d.items())
print('dictionary in acending order by value:',sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print('dictonary in decending order by value :',sorted_d)
