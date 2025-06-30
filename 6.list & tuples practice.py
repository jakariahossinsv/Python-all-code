
#wap to ask user to enter name of there 3 favorite movies annd store them in a list
movies=[]
mov1=input("enter 1st movie: ") 
mov2=input("enter 2nd movie: ")
mov3=input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

         #or
movies=[]
movies.append(input("enter 1st movie: ") )
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))
print(movies)

#wap to cheak if list contains a palindrom( like"maam"/"racecar" type word) of element
list1=[1,2,1]
list2=[1,2,3]

copy_list1= list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrom")
else:
    print("not palindrom")


#or
list1=["m","a","a","m","l"]


copy_list1= list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrom")
else:
    print("not palindrom")

#wap to count the number of student with "A"gread inn the following tuple
#["C","D","A","A","B","B","A"]
gread=("C","D","A","A","B","B","A")
print (gread.count("A"))


#store the avobe value in the list and short them form "A" to "D"
gread=["C","D","A","A","B","B","A"]
gread.sort()
print (gread)
