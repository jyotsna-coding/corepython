d ={1:'Apple',2:'Ball',3:'Cat',4:'Dog',5:'Eye'}
list = []
input = int(input("Enter any number from 1 to 5: "))
try:
    print("The value for your number is:",d[input])
except KeyError:
    print("Enter a valid number")
