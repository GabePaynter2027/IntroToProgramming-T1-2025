
def tally_score(q1, q2, q3, q4, q5):
    score = 0

    if q1.lower() == "yes":
        score += 1
    else:
        print("Question 1 was wrong.")

    if q2.lower() == "no":
        score += 1
    else:
        print("Question 2 was wrong.")

    if q3.lower() == "1":
        score += 1
    else:
        print("Question 3 was wrong.")

    if q4.lower() == "sun":
        score += 1
    else:
        print("Question 4 was wrong.")

    if q5.lower() == "water":
        score += 1
    else:
        print("Question 5 was wrong.")

    return score

print("Welcome to the Simple Quiz! Answer the questions below:")

answer1 = input("1. Is the sky usually blue? (yes/no) ")
answer2 = input("2. Do cows fly? (yes/no) ")
answer3 = input("3. What is 1 + 0? ")
answer4 = input("4. What gives us light during the day? ")
answer5 = input("5. What do we drink to stay alive? ")

total_score = tally_score(answer1, answer2, answer3, answer4, answer5)

print(f"\nYou got {total_score} out of 5 questions correct!")