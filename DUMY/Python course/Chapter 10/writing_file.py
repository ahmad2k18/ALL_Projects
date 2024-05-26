# from pathlib import Path

# file_p = Path('programming.txt')
# file_p.write_text('i love pythons')

import os

file_path = 'python_writing.txt'

with open(file_path, 'w') as file:
    file.write('i love python programming')
    
print('writing python successfully')

