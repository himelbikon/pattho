import string, random


def generate_random_code(n):
    s = string.ascii_letters + string.digits
    return ''.join(random.choice(s) for _ in range(n))


if __name__ == '__main__':
    print(generate_code(6))