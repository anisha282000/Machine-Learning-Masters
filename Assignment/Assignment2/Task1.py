# Create the below pattern using nested for loop in Python
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* 
 """
 



def pattern():
    for i in range(1,6):
        for j in range(1, i+1):
            print("*", end = "")
        print("\n")
    for i in range(4,0,-1):
        for j in range(1,i+1):
            print("*", end = "")
        print("\n")

pattern()