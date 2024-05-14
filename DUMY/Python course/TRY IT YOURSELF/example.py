#Personal Message
# Define the person's name
name = "Eric"

# Print a message to the person
print("Hello " + name + ", would you like to learn some Python today?")

#Name Cases
# Define the person's name
name = "Mark"

# Print the person's name in lowercase
print("Lowercase:", name.lower())

# Print the person's name in uppercase
print("Uppercase:", name.upper())

# Print the person's name in title case
print("Title case:", name.title())

#Famous Quote
# Define the quote and its author
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"

# Print the quote and its author in the specified format
print(author + " once said, " + '"' + quote + '"')


#Famous Quote 2
# Define the famous person's name
famous_person = "Albert Einstein"

# Define the quote and its author
quote = "A person who never made a mistake never tried anything new."

# Compose the message
message = famous_person + " once said, " + '"' + quote + '"'

# Print the message
print(message)

#Stripping Names
# Define the person's name with whitespace characters
name = "\t\n  John Doe \n\t"

# Print the name with whitespace around it
print("Name with whitespace:", name)

# Print the name using lstrip(), rstrip(), and strip() functions
print("Name using lstrip():", name.lstrip())
print("Name using rstrip():", name.rstrip())
print("Name using strip():", name.strip())


#File Extensions
# Assign the filename to a variable
filename = 'python_notes.txt'

# Find the index of the last '.' character
dot_index = filename.rfind('.')

# Use slicing to get the filename without the extension
filename_without_extension = filename[:dot_index]

# Display the filename without the extension
print("Filename without extension:", filename_without_extension)

#Second example: filename
# Assign the filename to a variable
filename = 'python_notes.txt'

# Use the removesuffix() method to remove the file extension
filename_without_extension = filename.removesuffix('.txt')

# Display the filename without the extension
print("Filename without extension:", filename_without_extension)
