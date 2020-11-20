#01. Python program to print the following string in a specific format
"""
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
"""

#02. Python program to get the Python version you are using
"""
import sys
print("Python Version : ")
print(sys.version)
print("Version Info : ")
print(sys.version_info)
"""

#03. Display the current date and time
"""
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
"""

#04. Python program which accepts the radius of a circle from the user and compute the area.
"""
import math
r = float(input("please enter the value of radius : "))
print(math.pi * r * r)
"""

#05. Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""
first = "Aditya"
last = "Anand"
print(last + " " + first)
"""

#06. Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
"""
no = 3, 5, 7, 23
l = list(no)
print("List : ", l)
t = tuple(no)
print("Tuple : ", t)
"""

#07. Python program to accept a filename from the user and print the extension of that.
"""
name = input("enter the filename : ")
ext = name.split(".")
print("The extension of your filename is : ", repr(ext[-1]))
"""

#08. Python program to display the first and last colors from the following list.
"""
color_list = ["red", "black", "yellow", "green", "blue"]
print("the first and last color of list is : ", color_list[0], color_list[-1])
"""

#09. Python program to display the examination schedule.
"""
exam_st_date = (24, 5, 2000)
print("Examination date is : %i / %i / %i" %exam_st_date)
"""

#10. Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("Enter the value of n : "))

n1 = int("%d" %n)
n2 = int("%d%d" %(n, n))
n3 = int("%d%d%d" %(n, n, n))
print(n1 + n2 + n3)