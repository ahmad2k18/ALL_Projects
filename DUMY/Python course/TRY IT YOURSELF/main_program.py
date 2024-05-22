# Import 8-16

# import module_name
import my_functions
my_functions.greet_user('Alice')

# from module_name import function_name
from my_functions import greet_user
greet_user('Bob')

# from module_name import function_name as fn
from my_functions import greet_user as gu
gu('Charlie')

# import module_name as mn
import my_functions as mf
mf.greet_user('Diana')

# module_name import *
from my_functions import *
greet_user('Eve')
