import random
import string

random_number=random.randint(0,9)

def random_letters():
    for i in range(0,2):
        global letter
        alphabet = string.ascii_letters
        letter = random.choice(alphabet)
        return letter
random_letters()
print(letter)
"""

import random

# Importing string library function
import string

def rand_pass(size):

    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice(
                        string.ascii_letters + string.digits)
                        for n in range(size)])

    return generate_pass

# Driver Code
password = rand_pass(10)
print(password)
"""
