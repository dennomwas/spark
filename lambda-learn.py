# Lambda are small anonymous functions only needed where they are created
# Lambda functions are mainly used in combination with the functions filter(), map() and reduce().

# The general syntax of a lambda function is quite simple:
# lambda argument_list: expression
# sum = lambda x,y: x + y


def sum(x, y): return x + y


sum(3, 4)

# MAP
# The function
# map(function, sequence)
Celcius = [39.2, 36.5, 37.3, 38, 37.8]
Farenheit = list(map(lambda x: (float(9)/5) * x + 32, Celcius))
print(Farenheit)

# FILTERING
# The function
# filter(function, sequence)
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

# REDUCE
# The function
# reduce(func, seq)
import functools
x = functools.reduce(lambda x, y: x+y, [47, 11, 42, 13])
print(x)
