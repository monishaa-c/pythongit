# #int
# a = 2310
# print(a)
# print(type(a))


# #string
# z = "Monisha"
# print(z)
# print( type(z))

# #float
# Deci = 0.2321
# print(type(Deci))

# #boolean
# x = 2310
# y = 2000
# print(x>y)
# print(type(x>y))


# def outer(x):
#     def inner(y):
#         return y*x
#     return inner

# function = outer(2)
# print(function(3))


# from turtle import *
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()

#factorial
# num = 12
# if(num == 0):
#     fact = 1

# fact = 1
# for i in range(1,num+1):
#     fact = fact*i

# print(fact)

#sum of series

# n = 4
# s = 0.0
# for i in range(1,n+1):
#     a = float(i**i)/i
#     s = s+a
# print(s)

#oddeven

# def oddeven(a):
#     if(a%2 == 0):
#         return 1

#     else:
#         return 0 
# num = 10
# if(oddeven(num)==1):
#     print("even")
# else:
#     print("odd")


#reverse a string

# def rev(str1):
#     str2 = ""
#     for i in range(0,len(str1)):
#         str2 = str1[i]+str2
#         i = i-1
#     return str2
# word = "dhaya"
# print(rev(word))


# def rev(str1):
#     str2 =""
#     i = len(str1)-1
#     while i>=0:
#         str2 = str2+str1[i]
#         i-=1
#     return str2
# word = "monisha"
# print(rev(word))

# num1 = []

# for i in range(1,11):
#     num1.append(i)
# print(num1)
# for j,i in enumerate(num1):
#     if(i%2!=0):
#         del num1[j]
# print(num1)

# string = list("sakthi")
# print(type(string))
# string.pop(0)
# print(string)

class MyClass:
    a = 10
    def myfun(self):
        print("this is class & obejct concepy")

obj=MyClass()
obj.myfun()
val = obj.a
print("value:",val )
