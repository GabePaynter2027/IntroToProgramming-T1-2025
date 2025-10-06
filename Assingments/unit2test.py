#Create a program that uses three input statements to ask the user for three words, print the concatenation of those three words
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")

print(word1 + word2 + word3)

#Create a function called add_three that takes three parameters. Outside the function, use three input statements that ask for one integer each. Run add_three using those integers. add_three should print the sum of those integers.
def add_three(a, b, c):
    print(a + b + c )

num1 = int(input("Enter the first integer:"))
num2 = int(input("Enter the second integer:"))
num3 = int(input("Enter the third integer:"))

add_three(num1, num2, num3)

#Create a function called data_three that takes zero parameters. Inside of the function create three input statements that ask for a word, an integer, and a float. Add the integer and the float and then concatenate that sum with the word, then print.
def data_three():
    word = input("Enter a word: ")
    integer = int(input("enter an integer"))
    decimal = float(input("Enter a float:")) 

    total = integer + decimal 
    print(word + str(total))

 

