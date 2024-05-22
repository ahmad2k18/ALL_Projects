import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to give a function Alias

from pizza import make_pizza as mp

mp(16, 'pepperoni')

mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module

from pizza import *

make_pizza(16, 'pepperoni')

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')