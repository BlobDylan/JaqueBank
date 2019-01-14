import random


def generate(length, level):
    p = ''
    if(level == 1):
        for i in range(length):
            p+= str(random.randint(0,9))
        return p


    elif(level == 2):
        for i in range(length):
            p += str(chr(random.randint(97, 122)))
        return p


    elif(level == 3):
        for i in range(length):
            p+= random.choice([str(chr(random.randint(65,90))), str(chr(random.randint(97,122)))])
        return p

    elif(level == 4):
        for i in range(length):
            p+= random.choice([str(chr(random.randint(65,90))), str(chr(random.randint(97,122))), str(random.randint(0,9))])
        return p

    elif(level == 5):
        for i in range(length):
            p += str(chr(random.randint(33, 126)))
        return p
    else:
        return "not a valid level please choose 1-5"

