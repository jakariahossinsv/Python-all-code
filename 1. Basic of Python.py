name = "fahim"       #Basic of python
age = 21
price = 25.99
age2 = age

print(name)
print (name,age,price)
print("my name is :", name)
print("my age is:", age2)

print(type (name))
print(type (price))
print(type( age))

a=2                          # print sum
b=5
sum=a+b
print(sum)

a=2000
b=500
diff=a-b
print(diff)

#arithmetic                    #operatorssssssssssss
a=5
b=2
sum=a+b
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  #remainder

#relational
a=5
b=2
print(a==b) #false
print(a!=b) #true
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)

#assignment 
num1=10 
num2= num1+10 # or num +=10  same kaj kore
num3= num1-10 # or num -=10  same kaj kore
num4= num1*10 # or num *=10  same kaj kore
num5= num1/10 # or num /=10  same kaj kore
num6= num1%10 # or num %=10  same kaj kore
num7= num1**5 # or num **=10  same kaj kore power
print("num2 :", num2)

#logical
a=50
b=30
print(not False)
print(not (a>b))  #not

val1 =True
val2=True
print("and operator:", val1 and val2)
val1 =True
val2=False
print("or operator:", val1 or val2)
a=50
b=30
print("or operator:", (a==b) or (a>b))


#type conversion                            #conversion
a= 2  # int
b=4.25 #float
sum =a+b
print(sum) #auto convert int to float

#type casting
a= "2" # string
b=4.25 #float
c=int(a)  #by using this it srting comvert into integer
sum =b+c
print(sum) #auto convert int to float

a= 4.25
a=int(a)
print(type(a))

#input in python                           # input in python
#input ("enter your name:") formula
"""
name = input ("enter your name:")
print("wellcome ",name)

name = input ("enter your age:")
print("you enterd",name)

val= input ("enter some value:")
print("you enterd",val)    # "2","4.33"

int ("5")
val= int(input ("enter some value:"))      #type casting in input
print(type(val),val)   

int ("5")
val= float(input ("enter some value:"))     #type casting in input
print(type(val),val) 
"""
name =input ("enter your name : ")             #type casting in input
age=  int (input ("enter your age: "))      
marks= float(input ("enter your marks: "))

print ("Wellcome ", name)
print("your age is ", age)
print("and your marks is",marks)

