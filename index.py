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


