import random
import string


def generate_id(lgt=20):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(0, lgt))

