marks=4.45
marks=4.56
marks=4.67
marks=4.99
#or
marks=["fahim",56,"dhaka"]  #or[3.45,4.00,3.67,3.46] , print(marks),print(type(marks))
print(marks[1])
print(marks[0])

student=["fahim",56,"dhaka"]    #in list it totally allowed
print(student[0])
student[0]="jakaria"
print(student)


marks=[98,43,85,47,77]           #slicingg
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-3:-1])#negative indx

list=[2,1,3]                     #list mathode
list.append(4)
list.sort()
print(list)

list=["apple","banana","orrange"]
print(list.sort(reverse=True))
print(list)

list=['a','f','d','b']
list.sort(reverse=True)
print(list)

list=['a','f','d','b']
list.reverse()
print(list)

list=[2,1,3] 
list.insert(1,10)
print(list)


list=[2,1,6,3] 
list.remove(2)
print(list)

list=[2,1,6,3] 
list.pop(2)
print(list)

#tuple                          #tuple
tup=(1,3,4,5,6,7)
print(type(tup))
print(tup[0])
print(tup[1:4])# tuple clising

tup=(3,5,6,7)
print(tup.index(5))

tup=(3,4,2,2,2,3,4,5,2,)
tup.count(2)
print(tup.count(2))
