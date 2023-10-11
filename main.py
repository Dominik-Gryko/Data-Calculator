from data_calculator import data_calculator


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



user_value = 3
user_unit = "kibibytes"
utct = "kilobyte" #Unit To Convert To
utct = unit_format(unit = utct)

if not supported_unit_check(unit=utct):
    print("ooooopsies, we ran into a problem trying to recognise your data's unit.")

calculator = data_calculator(value=user_value, unit = user_unit)
converted_value = FR_correct_conversion(calculator_instance=calculator, unit = utct)

print(converted_value)

