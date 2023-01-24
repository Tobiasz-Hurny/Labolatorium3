import secrets
import string
import random

pass_lenght = int(input('Proszę podać długość hasła'))


def generuj(pwd_lenght):
    types = [string.punctuation, string.digits, string.ascii_letters]
    haslo = ''
    ost = 0
    przed_ost = 0

    for i in range(pwd_lenght):
        if przed_ost == 2 and ost == 2:
            random_type = random.randint(0, 1)
        else:
            random_type = random.randint(0, 2)
        haslo += ''.join(secrets.choice(types[random_type]))
        przed_ost = ost
        ost = random_type
    return haslo


if __name__ == '__main__':
    for i in range(10):
        print(generuj(pass_lenght))
