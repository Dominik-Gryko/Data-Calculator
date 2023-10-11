from data_calculator import data_calculator
import menu
import sys

def unit_format(unit: str = None):
    if unit[-1:].lower() != 's':
        unit = unit + 's'
    
    return unit

def supported_unit_check(unit: str = None):
    

    supported_units = ["bytes","bits","kilobytes", "kibibytes", "megabytes", "mebibytes", "gigabytes", "gibibytes", "terabytes",
    "tebibytes","petabytes","pebibytes","kilobits", "kibibits", "megabits", "mebibits", "gigabits", "gibibits", "terabits","tebibits","petabits","pebibits"]

    if unit not in supported_units: 
        return False
    else:
        return True


def FR_correct_conversion(calculator_instance = None, unit: str = None):
    try:
        conversion = getattr(calculator_instance, f"convert_to_{unit}")
        return conversion()
    except Exception:
        return "ERROR: Cant convert to this unit, as it is not supported/recognised."

menu.main_menu()
while True:
    mm_choice = int(input("Enter the number corresponding to your choice: "))
    if mm_choice == 1:
        menu.units_menu()
        break
    elif mm_choice == 2:
        print("Work in progress, not available yet.")
    elif mm_choice == 0:
        sys.exit()
    else:
        print("Error: Invalid choice please try again.")   


while True:
    try:
        user_value = int(input("Enter the value of the data,(Don't include the unit): ")) 
    except Exception:
        print("Error: invalid value of data entered, please enter an integer.")
    else:
        break

while True:  
    try:
        user_unit = input("Enter the unit of your data: ")
        user_unit = unit_format(unit = user_unit)
        if not supported_unit_check(unit=user_unit):
            print("This unit is not recognised, please try again.")
        else:
            break
    except Exception:
        print("Error: invalid unit entered, try again.")

while True: 
    try:
        utct = input("Enter the unit you want to convert your data to: ") #Unit To Convert To
        utct = unit_format(unit = utct)
        if not supported_unit_check(unit=utct):
            print("This unit is not recognised, please try again.")
        else:
            break
    except Exception:
        print("Error: invalid unit entered, try again.")
        
calculator = data_calculator(value=user_value, unit = user_unit)
converted_value = FR_correct_conversion(calculator_instance=calculator, unit = utct)

print(converted_value)

