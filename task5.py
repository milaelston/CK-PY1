import string
import random


def get_random_password(n=8) -> str:
    usablesymbstr = string.ascii_uppercase + string.ascii_lowercase + string.digits
    symblist = random.sample(usablesymbstr, n)
    password = ''.join(symblist)
    return password


print(get_random_password())
