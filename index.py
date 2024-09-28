#variables that holds my name and age
name="Mireille"
age=20
print("My name is "+name)
print(name,age)
#Create a variable inside a function, with the same name as the global variable
x="awesome"
def myFunction():
    x="Fantastic"
    print("Python is "+x)
myFunction() #displays Python is Fantastic
print("Python is "+x)#display python is Awesome
#using global keyword 
x="awesome"
def myFunction2():
   global x
   x="Fantastic"
myFunction2() 
print("Python is "+x)#displays Python is Fantastic
# get type of variable
x="Mireille Irafasha"
print(type(x))
#Random number
import random

print(random.randrange(1,10))
# Assign  multiple variables
st1,st2,st3="Neema","Mugisha","Nicole"
print(st1)
print(st2)
print(st3)
#Assiigning ob=ne value to different variables
x=y=z="Merveille"
print(x)
#Unpack collection
fruits=["Apple","Banana","Mango"]
a,b,c=fruits
print("I need to buy ",a)

#In the print() function, you output multiple variables, separated by a comma:
print("I have",a,b,c)

# Print different values like string and  number and using global variable
 
x1=2
def GlobalVariable():
  x2="Computer Graphic design"
  print(x2,x1)
GlobalVariable()

# swap two variables
def Swap(x,y):
   z=0
   z=x
   x=y
   y=z
   return "The value of x",x,"and the value of y",y

print(Swap(20,4))

#About me using multiline strings
about="""I'm a third-year Computer Science student at the University of Rwanda with 
strong backend development skills in JavaScript, Node.js, and MongoDB. 
I've completed the SheCanCode bootcamp, where I gained hands-on experience in building backend systems and working with Swagger documentation. 
I'm also an entrepreneur, running 'Merveille Catering Services,' which has enhanced my management and client relations skills. 
I'm passionate about problem-solving and eager to apply my skills to new challenges."""

print(about)

#Accessing character within your string using array means string are Arrays
mystring="Hello , World!"
print(mystring[2])

#To get the length of a string, use the len() function.
print(len(mystring))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
print("backend"in about)

#Use it in an if statement:

if "backendw" in about:
  print("backend is in the about")
else:
  print("backend is not in the about")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
if "backend" not in about:
  print("backend is not in the about")
else:
   print("backend is in the about")

"""Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string."""
mystring_1=" Hello,Mimilar"
print(mystring_1[2:5])

#slice from start ,By leaving out the start index, the range will start at the first character:
print(mystring_1[:5])

#slice to End By leaving out the end index, the range will go to the end:
print(mystring_1[1:])

#Negative Indexing ,Use negative indexes to start the slice from the end of the string:
print(mystring_1[-5:-1])#means from index of 5 from the end of index to before 1 element to the end of index 

# transform  to lower case
print(mystring_1.lower())

#transform to upper case
print(mystring_1.upper())

#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
print(mystring_1.strip())

#replace character
print(mystring_1.replace("Hello","Hey"))

#The split() method returns a list where the text between the specified separator becomes the list items.
print(mystring_1.split(",")) #return ["Hello","Mimilar"]

#To concatenate, or combine, two strings you can use the + operator.
a="Mireille "
b="Irafasha"
print(a+b)

#combine string and number But we can combine strings and numbers by using f-strings or the format() method!
age=23
name="Mendel"
txt= f"My name is {name} and age is {age}"
print(txt)
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
txt=f"My age is {age:.2f}"
print(txt)
#A placeholder can contain Python code, like math operations:
txt=f"My age is {age+23}"
print(txt)
#insert illegal character you use escape character \
txt="my name is \"Denyse\""
print(txt.capitalize())
txt1=txt.center()
print(txt1)
