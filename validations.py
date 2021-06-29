def user_choice():
    choice = "Wrong"
    acceptable_range = range(0, 10)
    within_range = False


    while choice.isdigit() == False or within_range == False:
        choice = input("please enter a number: ")

        if choice.isdigit() == False:
            print("Sorry that is not a digit")

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Out of range")
                within_range = False

    return int(choice)


    # acceptable_values = [0, 1, 2, 3]
    # input0 in acceptable_values

user_choice()