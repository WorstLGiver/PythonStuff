while True:
    try:
        rectangles = int(input('\033[94m' + '\033[1m' "How many rectangles do you want?:    " + '\033[0m'))
        break
    except ValueError:
        print(
            '\033[91m' + '\033[1m' + "YO, YOU SO DUMB MATE I BE ASKIN YOU A SIMPLE QUESTION YEA, SO GIMME A SIMPLE ANSWER INNIT:    " + '\033[0m')
        continue
costid = float()
lengthid = []
widthid = []
typeslab = ('\033[91m' + '\033[1m' + "Dover", "Exeter", "London", "Portland", "Shaftesbury", "York" + '\033[0m')
priceofslab = (30, 35, 42, 49.50, 55, 62.75)
for gay in range(0, len(typeslab)):
    print("\033[91m", '\033[1m', typeslab[gay], "  =    $", priceofslab[gay], '\033[0m')


def lol(r1, r2):
    return [item for item in range(r1, r2 + 1)]


r1, r2 = 1, rectangles

from decimal import Decimal as D

while True:
    NameSlab = input('\033[92m' + '\033[1m' + "Gimme slab name:   " + '\033[0m')
    if NameSlab == typeslab[0].lower() or typeslab[0]:
        costid = float(priceofslab[0])
        break
    elif NameSlab == typeslab[1].lower() or typeslab[1]:
        costid = float(priceofslab[1])
        break
    elif NameSlab == typeslab[2].lower() or typeslab[2]:
        costid = float(priceofslab[2])
        break
    elif NameSlab == typeslab[3].lower() or typeslab[3]:
        costid = float(priceofslab[3])
        break
    elif NameSlab == typeslab[4].lower() or typeslab[4]:
        costid = float(priceofslab[4])
        break
    elif NameSlab == typeslab[5].lower() or typeslab[5]:
        costid = float(priceofslab[5])
        break
    else:
        print('\033[91m' + '\033[91m' + "Bruh its invalid you retard, try again" + '\033[0m')
        continue

for lol in range(0, rectangles):
    while True:
        try:
            print('\033[95m' + '\033[1m' + "FOR RECTANGLE NUMBER: ", lol + 1, '\033[0m')
            length = float(input(
                '\033[93m' + "What length u want boi? Gimme length in metres for rectangle number:   " + '\033[0m'))
            if length >= 0.5:
                lengthid.append(float(length))
                break
            else:
                print(
                    '\033[200m' + '\033[1m' + "OMG U RETARD I SAID GIMME MORE THAN OR EQUAL TO 0.5 METRES YOU NUTCASE." + '\033[0m')
                continue
        except ValueError:
            print('\033[91m' + '\033[91m' + "OMG u so dumb you retard, GIMME NUMBERS NOTHING ELSE!!!     " + '\033[0m')
            continue

for lol in range(0, rectangles):
    while True:
        try:
            print('\033[91m', '\033[1m', "FOR RECTANGLE NUMBER: ", lol + 1, '\033[0m')
            width = float(
                input('\033[1m' + '\033[34m' + "What width you want boi? Gimme width in metres:   " + '\033[0m'))
            if length >= 0.5:
                widthid.append(float(width))
                break
            else:
                print(
                    '\033[91m' + '\033[1m' + "OMG U RETARD I SAID GIMME MORE THAN OR EQUAL TO 0.5 METRES YOU NUTCASE." + '\033[0m')
                continue
        except ValueError:
            print('\033[91m' + '\033[1m' + "OMG u so dumb you retard, GIMME NUMBERS NOTHING ELSE!!!    " + '\033[0m')
            continue

for lol in range(0, rectangles):
    AreaBruh = [(width) * (length) for width, length in zip(widthid, lengthid)]

TotalArea = sum(AreaBruh)

Costlol = TotalArea * costid

Waste = float(input('\033[95m' + '\033[1m' + "Now gimme ur waste in %: " + '\033[0m'))

NewArea = TotalArea + (TotalArea * (Waste / 100))

TotalCost = NewArea * costid

for lol in range(0, rectangles):
    print('\033[34m', '\033[1m', "The area for rectangle ", lol + 1, "is:   ", round(AreaBruh[lol], 2), '\033[0m')

print('\033[93m', '\033[1m', "The total area for all rectangle without wastage is:\n", round(TotalArea, 2), "m\u00b2",
      '\033[0m')
print('\033[92m', '\033[1m', "The total area for all rectangles with wastage included is:\n", round(NewArea, 2),
      "m\u00b2", '\033[0m')
print('\033[21m', '\033[1m', "The total cost excuding wastage is:\n$", round(Costlol, 2), '\033[0m')
print('\033[21m', '\033[1m', "The total cost including wastage is:\n$", round(TotalCost, 2), '\033[0m')
