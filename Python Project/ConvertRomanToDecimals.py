tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # Add more if needed
}

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum

# Taking user input as a single Roman numeral string
user_input = input("Enter a Roman numeral string : ").upper()

try:
    # Converting the entire input string to decimal
    result = RomanNumeralToDecimal(user_input)
    print(f"The decimal value of '{user_input}' is: {result}")
except KeyError:
    print("Invalid Roman numeral detected. Please check your input.")
