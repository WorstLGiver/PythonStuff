print('Who invented the stethoscope? (Caps matter)')

while True:
    Answer = input('Answer: ')

    if Answer in ('René Laennec', "Rene Laennec"):
        if Answer == 'René Laennec':
            print('Correct')

        elif Answer == "Rene Laennec":
            print('Correct')
        break

    else:
        print("Wrong")
        try_again = input("Try again? (yes/no): ")
        if try_again.lower() != "yes":
            break
