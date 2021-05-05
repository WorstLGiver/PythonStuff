import math
while True:
    print("Chose one \n (1) Blocks to Kb,Mb,Gb \n (2) Kb,Mb,Gb to Blocks")
    choice = input('Enter choice (1/2): ')
    if choice == "1":
        try:
            blocks = int(input("Blocks: "))
            kb = blocks * 128
            unit = "kb"
            if kb >= 1024:
                kb = kb / 1024
                unit = "mb"
                if kb >= 1024:
                    kb = kb / 1024
                    unit = "gb"
            print('Amount in', unit + ':', math.ceil(kb))
        except Exception:
            print('Please type a whole number')
    elif choice == "2":
        try:
            print("What unit is the file? \n (1)" "Mb \n (2)" "Gb \n (3)" "Kb")
            unit = input("Enter unit (1/2/3): ")
            if unit == "1":
                print("How many Megabytes is the file?")
                megabytes = float(input("Amount of Megabytes: "))
                blocks = megabytes * 8
                print("Amount in Blocks:", math.ceil(blocks))
            elif unit == "2":
                print("How many Gigabytes is the file?")
                gigabytes = float(input("Amount of Gigabytes: "))
                blocks = gigabytes * 8192
                print("Amount in Blocks:", math.ceil(blocks))
            elif unit == "3":
                print("How many Kilobytes is the file?")
                kilobytes = float(input("Amount of Kilobytes: "))
                blocks = kilobytes / 128
                print("Amount in Blocks:", math.ceil(blocks))
            else:
                print("Please chose one of the choices")
        except Exception:
            print("Please enter a number")
