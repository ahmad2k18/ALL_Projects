# File and Exceptions 
from pathlib import Path

path = Path('Domain names.txt')
contents = path.read_text()
print(contents)


# NEW EXAMPLE

import os

file_path = 'pi_digits.txt'
with open(file_path, 'r') as file:
    contents = file.read()
    
print(contents)

