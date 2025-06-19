# Day 3: Input and String Manipulation

# Ask for user input
name = input("What's your name? ")
city = input("Which city do you live in? ")

# Combine using f-string
print(f"Hello {name} from {city}!")

# Bonus: Clean whitespace and capitalize
clean_name = name.strip().title()
clean_city = city.strip().title()

print(f"Cleaned: Hello {clean_name} from {clean_city}!")


# Bio Generator

name = input("What's your full name? ")
age = input("How old are you? ")
city = input("Which city do you live in? ")
hobby = input("What's your hobby? ")

# Clean & Format
name = name.strip().title()
city = city.strip().title()
hobby = hobby.strip().lower()

# Output
print("\n--- Your Bio ---")
print(f"My name is {name}, I'm {age} years old, I live in {city}, and I love {hobby}.")
