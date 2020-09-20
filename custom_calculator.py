'''
README:

Project Name: Reading Calculator

Description: Given the user's reading speed and word count, this calculator will return the amount of minutes it will take to read a book.

Language: Python 3.7.9

''' 

# Print statement to welcome user to calculator
print("Howdy, and welcome to the reading calculator! 🤠 ")

# Gets the user's avg reading print
reading_speed = input("What is your average reading speed per minute? ")
reading_speed = int(reading_speed)

# Gets the word count of book the user is reading 

word_count = input("What is the word count of your book? ")
word_count = int(word_count)

# Calculate how much time it takes to read based on reading speed and word count
 
time_needed = word_count / reading_speed

# Prints a message to user with the result
print(f"The amount of minutes needed to read: {time_needed} minutes")