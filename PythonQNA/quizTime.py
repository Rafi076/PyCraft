import time
import random

# Global score variable
score = 0

# Fun responses for correct and incorrect answers
correct_responses = ["🎉 Bingo!", "👏 Great job!", "🔥 You're on fire!", "✅ Correct!"]
wrong_responses = ["😕 Not quite!", "🚫 Wrong answer!", "❌ Oops, try again!"]

# Function to display hints after incorrect guesses
def get_hint(answer, attempt):
    hints = {
        "polar bear": ["It’s a bear but lives in extreme cold!", 
                       "You find it near the Arctic circle."],
        "cheetah": ["It has spots and loves speed!", 
                    "It’s a big cat that runs faster than any car!"],
        "blue whale": ["It’s bigger than any other living creature!", 
                       "It's found in oceans and sings underwater!"]
    }
    return hints[answer][attempt]

# Modified check_guess function with hints and fun responses
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print(random.choice(correct_responses))
            score += 1
            still_guessing = False
        else:
            print(random.choice(wrong_responses))
            if attempt < 2:
                print(f"Hint: {get_hint(answer, attempt)}")
                guess = input("Try again: ")
            attempt += 1

    if attempt == 3:
        print(f"The correct answer was: {answer}")

# Main quiz logic
print("🐾 Welcome to the Animal Quiz 🐾")
print("Try to answer these animal-related questions!\n")

guess1 = input("1️⃣ Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")

guess2 = input("2️⃣ Which is the fastest land animal? ")
check_guess(guess2, "cheetah")

guess3 = input("3️⃣ Which is the largest animal? ")
check_guess(guess3, "blue whale")

# Final score display with emoji feedback
print(f"\n🏆 Your final score is: {score}/3")

# Dynamic exit message based on performance
if score == 3:
    print("🎯 Perfect score! You're an animal expert!")
elif score == 2:
    print("💪 Great job! You're almost an expert!")
elif score == 1:
    print("🙂 Not bad, but keep practicing!")
else:
    print("😅 Better luck next time! You'll get it!")

