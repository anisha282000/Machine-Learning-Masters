"""
Question 2
Write a Python program to accept the user's first and last name and then
getting them printed in the the reverse order with a space between first name
and last name
"""
def name(x,y):
    f_n = x[::-1]
    l_n = y[::-1]
    print(f_n + " " + l_n)
first_name = input("Enter your first name")
last_name = input("Enter your last name")
name(first_name, last_name)
