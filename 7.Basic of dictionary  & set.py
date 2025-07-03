#basic of dictonary
info= {
    "key":"value",
    "name":"fahim",
    "subject":["python","java","c","c++"], #list allowed
    "topic": ("dictonary","set"), #tuples allowed
    "age":35, #int allowed
    "is_adult":True,  #boolian allowed
    "markes":3.9,  #floting allowed
    12 : 39,  #key also can be number
    3.2 : 3.9, # key also floting,tuple,string 
    }
print (info)
print (type(info))
print(info["name"]) # individually key serch
print(info["topic"])  # individually key serch
print(info["subject"])  # individually key serch
print(info["age"])      # individually key serch

info["name"]="jakaria"  #changing key value
info["surname"]= "mondal" # new key value or rename
print(info)

#null dict
null_dict={}   #we can creat null dictonary
null_dict=["Daffodil","university"]
print(null_dict)




#nested dicttonary
student={                          # dictionary in a dictonary
    "name": "fahim",
    "subject" : {                   # dictionary in a dictonary
        "phy":95,
        "chem":98,
        "bio":100
    }
    
}
print(student)
print(student["subject"]) 
print(student["subject"] ["chem"]) #to print individual mark



#dictionary mathod
#1
student={                             #dict.keys() mathode      
    "name": "fahim",
    "subject" : {                   
        "phy":95,
        "chem":98,
        "bio":100
    }
    
}
print(student.keys())
print(len(student))
print(list(student.keys())) #convert with list
print(len(list(student.keys())))


#2
student={                             #dict.values() mathode      
    "name": "fahim",
    "subject" : {                   
        "phy":95,
        "chem":98,
        "bio":100
    }
    
}
print(student.values())
print(list(student.values())) #convert with list



#3
student={                             #dict.items() mathode      
    "name": "fahim",
    "subject" : {                   
        "phy":95,
        "chem":98,
        "bio":100
    }
    
}
print(student.items())
print(list(student.items())) #typecast with list
pairs=list(student.items())
print(pairs[0])
print(pairs[1])


#4
student={                             #dict.get("key") or d["key"] mathode      
    "name": "fahim",
    "subject" : {                   
        "phy":95,
        "chem":98,
        "bio":100
    }
    
}
print(student["name"])         #type 1
print(student.get("name"))     #type 2
#print(student["name2"])       # error asbe
#print(student.get("name2"))   # mathode diye try korle none asbe

#[NB. akbar error asle tar por r konooo kisu run korbe na]



#5
student={                             #dict.update({}"key:value"}) mathode      
    "name": "fahim",
    "subject" : {                   
        "phy":95,
        "chem":98,
        "bio":100
    }
    
}
print(student.update({"city":"dhaka"}))
print(student)
       #or
new_dict={"city":"dhaka","age":21}
student.update(new_dict)
print(student)
       #or
new_dict={"name":"jakaria","age":21}  #purano name update hoie jabe is called " overide"
student.update(new_dict)
print(student)  





#set in python
collection= {1,2,3,4}
print(collection)
print(type (collection))
#or
collection= {1,2,2,2,2} #set ignore the duplicate value
print(collection)
print(type (collection))
#or
collection= {1,2,3,4,"hello","world"} #set is unorderd
print(collection)
print(type (collection))
#or
collection= set() #its empty set not this " collection={} " its dictionary
print(collection)
print(type (collection))

#set mathod
#1
collection= set() #set.add(el) mathod
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hello") #string
collection.add((1,2,3)) #tupple
#collection.add([1,2,3]) #list nos pass in set its mutable or changable
print(collection)

#2
collection= set() #set.remove(el) mathod
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(2)
#collection.remove(7) #its not exiest in set its error
print(collection)


#3
collection= set() #set.clear(el) mathod
collection.add(1)
collection.add(2)
collection.add("hello") 
collection.add((1,2,3))
collection.clear()
print(len(collection))

#4
collection={"hello","world","daffodil","diu","dhaka"}   #set.pop(el) mathod
print(collection.pop())
print(collection.pop())

#5
set1={1,2,3}      #set.union(set2) mathod
set2={2,3,4}
print(set1)
print(set2)
print(set1.union(set2))

#6
set1={1,2,3}     #set.inntersection(set2) mathod
set2={2,3,4}
print(set1)
print(set2)
print(set1.intersection(set2))
