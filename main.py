while True:

    menu_unit_options = {
    "1": "kilobytes",
    "2": "megabytes",
    "3": "gigabytes",
    "4": "terabytes",
    "5": "petabytes"
}
    print("""
1.Go to Calculator
2.View previous calculations 
""")
    Selection_main=input("Select an option:\n")
    if Selection_main =="1":
        Answer=input("Enter yes to continue\n")
    elif Selection_main =="2":
        pass
    else:
        print("error, invalid input")
    
    if Answer == "yes":
        print(menu_unit_options)
    else:
        print("error,invalid input")

    Selection_unit = input("Select an option:\n")
    if Selection_unit == "1":
        print("Enter yes to continue")
    elif Selection_unit == "2":
        print("Enter yes to continue")
    elif Selection_unit == "3":
        print("Enter yes to continue")
    elif Selection_unit == "4":
        print("Enter yes to continue")
    elif Selection_unit == "5":
        print("Enter yes to continue")
    else:
        print("Error, invalid input")

    number = int(input("Enter the amount"))

    if Selection_unit == "1":
        print(number * 1024)
    elif Selection_unit == "2":
        print(number * (1024 ** 2) )
    elif Selection_unit == "3":
        print(number * (1024 ** 3) )
    elif Selection_unit == "4":
        print(number * (1024 ** 4))
    elif Selection_unit == "5":
        print(number * (1024 ** 5))
    else:
        print("Error, invalid input")
    if not input("Do you want to continue? (y/n) ").lower().startswith("y"):
        break
    else:
        continue

