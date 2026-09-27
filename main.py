"""IQ TEST --- USING PYTHON CODE"""

import time
import random

ques = [
    {
        "question": "What comes next in the series? 2, 4, 8, 16, ?",
        "option": ["A) 18", "B) 24", "C) 32", "D) 20"],
        "ans": "C"
    },
    {
        "question": "If CAT is coded as DBU, how is DOG coded?",
        "option": ["A) EPH", "B) EPH", "C) EQH", "D) EPI"],
        "ans": "A"
    },
    {
        "question": "Find the odd one out: Triangle, Square, Circle, Apple",
        "option": ["A) Triangle", "B) Square", "C) Circle", "D) Apple"],
        "ans": "D"
    },
    {
        "question": "5, 10, 15, 20, ? — What comes next?",
        "option": ["A) 22", "B) 25", "C) 30", "D) 35"],
        "ans": "B"
    },
    {
        "question": "A is the father of B. B is the father of C. "
                     "What is A to C?",
        "option": ["A) Brother", "B) Uncle", "C) Grandfather", "D) Son"],
        "ans": "C"
    },
    {
        "question": "Which number is a prime number?",
        "option": ["A) 21", "B) 33", "C) 37", "D) 45"],
        "ans": "C"
    },
    {
        "question": "Complete the analogy: Book is to Reading as Fork is to?",
        "option": ["A) Drawing", "B) Writing", "C) Eating", "D) Cutting"],
        "ans": "C"
    },
    {
        "question": "What is 15% of 200?",
        "option": ["A) 20", "B) 25", "C) 30", "D) 35"],
        "ans": "C"
    },
    {
        "question": "Complete the sequence below by determining the missing number:1, 8, 27, ?, 125, 216",
        "option": ["A) 36", "B) 45", "C) 64", "D) 99"],
        "ans": "C"
    },
    {
        "question": "A boy walked 4 kilometres towards the North, turned to his left and walked 6 kilometres, and again turned \nleft and walked 4 kilometres. What is his absolute straight-line distance from his starting point?",
        "option": ["A) 10KM", "B) 6KM", "C) 0KM", "D) 4KM"],
        "ans": "B"
    },
    {
        "question": "In a specific code language, if the word BRAIN is written as PGKCP, how would the word LOGIC be written in that same code?",
        "option": ["A) NQIKE", "B) EKIQN", "C) ENKQI", "D) NQEK-I"],
        "ans": "C"
    },
    {
        "question": "A father is 4 times as old as his son. Their total age is 50. How old is the son?",
        "option": ["A) 8", "B) 10", "C) 12", "D) 15"],
        "ans": "B"
    },
    {
        "question": "Ravi walks 5 km north, then 5 km east, then 5 km south. How far is he from his starting point?",
        "option": ["A) 0KM", "B) 5KM", "C) 10KM", "D) 15KM"],
        "ans": "B"
    },
    {
        "question": "If it is 3:00 PM now, what time will it be after 125 minutes?",
        "option": ["A) 4:55 PM", "B) 5:00 PM", "C) 5:05 PM", "D) 5:15 PM"],
        "ans": "C"
    },
    {
        "question": "Five people are standing in a line. Amit is taller than Raj but shorter than Vijay. Raj is taller than Mohan. Who is definitely the shortest among these four?",
        "option": ["A) Amit", "B) Raj", "C) Vijay", "D) Mohan"],
        "ans": "D"
    },
]


def ask_ques():
    """Loop through all questions, take user input, and return the score."""
    score = 0
    total = len(ques)

    print("=" * 55)
    print("!!!WELCOME TO THE IQ TEST BY NISHANTA BHARALI!!!")
    print("Answer each question by typing 'A' or 'B' or 'C' or 'D'")
    print("All the Best")
    print("=" * 55)
    time.sleep(1)

    random.shuffle(ques)
    for i, q in enumerate(ques, start=1):
        print(f"\nQ{i}. {q['question']}")
        for option in q["option"]:
            print("   " + option)

        user_ans = input("Your answer: ").strip().upper()
	
        if user_ans in ("A","B","C","D"):
            if user_ans == q["ans"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer was: {q['ans']}")
        else:
              print("Enter valid option...")
              print(f"You score 0 for this question!!!")

    return score, total


def calc_iq(score, total):
    """
    Convert the raw score into an approximate IQ value.
    Average IQ is considered to be 100.
    """
    percentage = (score / total) * 100
    iq_score = (80+percentage * 0.6)    #simple scaling formula
    return round(iq_score)

def classify_iq(iq_score):
    """Return a category label based on the IQ score."""
    if iq_score >= 140:
        return "Genius"
    elif iq_score >= 120:
        return "Very Superior"
    elif iq_score >= 110:
        return "Superior"
    elif iq_score >= 90:
        return "Average"
    elif iq_score >= 80:
        return "Below Average"
    else:
        return "Low"


def main():
    name = input("Enter your full name: ").strip()
    score, total = ask_ques()
    iq_score = calc_iq(score, total)
    category = classify_iq(iq_score)
    time.sleep(1)
    print("\n" + "=" * 55)
    print("RESULT")
    print("=" * 55)
    print(f"Name        : {name}")
    print(f"Score       : {score}/{total}")
    print(f"Estimated IQ: {iq_score}")
    print(f"Category    : {category}")
    print("=" * 55)
    print("Note:This is just a project and not a certified psychometric IQ test.")
    time.sleep(1)


if __name__ == "__main__":
    main()
