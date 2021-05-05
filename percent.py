while True:
    try:
        print("Please enter the numerator and then the denominator")
        numerator = input("Numerator: ")
        denominator = input("Denominator: ")
        print("Is the missing variable the Denominator or the Numerator?")
        variable = input("Numerator (1) or Denominator (2): ")
        if variable == "1":
            variable = float(input("What is the denominator? "))
            decimal = float(numerator) / float(denominator)
            answer: float = variable * decimal
            print(numerator + "/" + denominator, "=", "X/" + str(variable))
            print(numerator + "/" + denominator, "=", decimal)
            print(variable, "*", str(decimal), "=", answer, "\n" + 'X =', answer)
        elif variable == "2":
            variable = float(input("What is the numerator? "))
            decimal = float(numerator) / float(denominator)
            answer = variable / decimal
            print(numerator + "/" + denominator, "=", str(variable) + "/X")
            print(numerator + "/" + denominator, "=", decimal)
            print(variable, "/", str(decimal), "=", answer, "\nX =", answer)
        else:
            print("Please pick choices 1 or 2")
    except Exception:
        print("Please enter a number.")
