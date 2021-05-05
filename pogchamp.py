def lol():
    import random
    random.random()
    global a
    global c
    b = random.randint(1, 2)
    print(b)
    if b == 1:
        a = a + 1
    elif b == 2:
        c = c + 1


while True:
    try:
        pog = int(input('How many times:'))
        i = 1
        a = 0
        c = 0
        while i <= pog:
            lol()
            i = i + 1
        print("1 has been said", a, "times.", "2 has been said", c, "times.")
    except Exception:
        print("Please enter a whole number")
