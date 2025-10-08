print("Welcome to the Boolean Quiz!")
print("Please type whole numbers to answer.\n")

answer1 = int(input("Q1: Type a number bigger than 10:\n"))
print(answer1 > 10)   

answer2 = int(input("Q2: Type the number 7:\n"))
print(answer2 == 7)  

answer3 = int(input("Q3: Type a number less than or equal to 5:\n"))
print(answer3 <= 5)   

answer4 = int(input("Q4: Type a number that is NOT 3:\n"))
print(answer4 != 3)   

answer5 = int(input("Q5: Type a number zero or bigger:\n"))
print(answer5 >= 0)   

print("\nNow some questions with AND / OR / NOT:")

answer6 = int(input("Q6: Type a number bigger than 5 AND smaller than 15:\n"))
print(answer6 > 5 and answer6 < 15)   

answer7 = int(input("Q7: Type a number less than 3 OR bigger than 20:\n"))
print(answer7 < 3 or answer7 > 20)  

answer8 = int(input("Q8: Type a number that is NOT 10:\n"))
print(not (answer8 == 10))   

print("\nThanks for playing!")