# Program to count the number of each char in a string

# Enter the text
userMessage = input("Enter the text")

# Enter the char

userChar = input ("Enter the char you want ")

userMessage = userMessage.casefold()

count = {}.fromkeys(userChar,0)

for char in userMessage:
   if char in count:
       count[char] += 1

print("The vowels in the text are ", count)