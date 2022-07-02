string1 = input("Enter a string-:")    # input string variable
print ("The original string  is : ",string1)
reverse_String1 = ""  # Empty String
count = len(string1) # Find length of a string and save in count variable
while count > 0:
    reverse_String1 = reverse_String1+string1[ count - 1 ] # save the value of str[count-1] in reverseString
    count = count - 1 # decrement index
print ("The reversed string using a while loop is : ",reverse_String1)# reversed string

print("")
# Question no.2

a=int(input("Enter your first no.-:"))    # input value of lower range
b=int(input("Enter your second no.-:"))   # input value of upper range
num1=int(input("Enter the number which you will divide on entire range-:"))      # input of number you want to divide
print("All numbers in range",(a,b),"which are divisible by",num1,"are as follows-:")
for item in range(a,b) :
    if item%num1==0:
        print(item)
print("")
# Question no.3
import random

i=0
while i<5:
    s1 = int(input("Enter your first side:-"))
    s2 = int(input("Enter your second side:-"))
    s3 = int(input("Enter your third side:-"))
    s = (s1 + s2 + s3) / 2
    if s1+s2>s3 and s3+s2>s1 and s1+s3>s3 :
        print("Area is equal to :-",(s*(s-s1)*(s-s2)*(s-s3))**(1/2))
    else :
        print("The sides entered don't for a triangle!!!")
    i=i+1
print("you were having only 5 turns to enter the sides of your triangle!!!")

print("")
# Question no.4

print("The given pattern is as follows-:")
i=1
while i<6:
    print("*"*i)
    i=i+1

i=4
while i>0:
    print("*"*i)
    i=i-1

print("")
# Question 5
x = int(input("Enter the number of rows: "))
k = 65
for i in range(1,x+1):
    for j in range(0,i):
            y = chr(k)
            print(y, end="")
            k += 1
            if (k-64)%26==0:
                k=65
    print("")

print("")
# Question No.6
print("please,Enter the range in which you want to get prime number")
lower = int(input("Enter the Lowest Range Value-:"))
upper = int(input("Enter the Upper Range Value-:"))

print("The Prime Numbers in range ",(lower,upper),"are as follows-: ")
for number in range(lower, upper + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)

print("")
# Question No.7
print("Following are the numbers which are multiple of 7 and divisible by 11 in the range (1-500)-:")
for item in range(1,500):
    if (item%7==0)&(item%11==0):
        print(item)

print("")
# Question No.8
print("you have to Enter 10 integers of your choice-:")
list1 = []
i=1
while i<11:

    num1=int(input("Enter an integer-:"))
    list1.append(num1)
    i=i+1


print("This is the list of integers entered by the user-:",list1)
print("positive numbers are as follows-:",end="")
for item in list1:
    if item>0:
        print(item,end=",")
print("\nnegative numbers are as follows-:",end="")
for item in list1:
    if item<0:
        print(item,end=",")
print("\nodd numbers are as follows-:",end="")
for item in list1:
    if (item%2!=0)&(item>0):
        print(item,end=",")
print("\neven numbers are as follows-:",end="")
for item in list1:
    if (item%2==0)&(item>0):
        print(item,end=",")
count1=int(input("\nEnter the number you want to count in list1-:"))
count_num=list1.count(count1)
print("The number -",count1,",","occurs",count_num,"times in the list1")

print("")
# Question No.9
print("you can enter 10 words in list_enter")
list_1=[]
for item in range(10):
    words=input("Enter the word you want to add in the list_enter-:")
    list_1.append(words)

count1=input("Enter the word you want to count in list_enter-:")
count_list=list_1.count(count1)
print("word -",count1,",","occurs",count_list,"times")
