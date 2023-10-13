class calculator_interface():

    

    def unit_format(unit: str = None, type: str = None): 
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
    
    def units_menu():
        print("""\nThe available units are: 
bits - petabits/pebibits. 
bytes - petabytes/pebibytes.

bits - bytes
kilobits | kibibits - kilobytes | kibibytes
megabits | mebibits - megabytes | mebibytes
gigabits | gibibits - gigabytes | gibibytes
terabits | tebibits - terabytes | tebibytes
petabits | pebibits - petabytes | pebibytes

(FYI: e.g. kibibytes is the binary version of kilobytes so 1 kilobytes = 1000 bytes | 1 kibibyte = 1024 bytes)

""")
    
    
    def interface():
        
        while True:
            try:
                user_value = int(input("Enter the value of the data,(Don't include the unit): ")) 
            except Exception:
                print("Error: invalid value of data entered, please enter an integer.")
            else:
                break

        calculator_interface.units_menu()

        while True:  
            try:
                user_unit = input("Enter the unit of your data: ")
                user_unit = calculator_interface.unit_format(unit = user_unit)
                if not calculator_interface.supported_unit_check(unit=user_unit):
                    print("This unit is not recognised, please try again.")
                else:
                    break
            except Exception:
                print("Error: invalid unit entered, try again.")

    
        while True: 
            try:
                utct = input("Enter the unit you want to convert your data to: ") #Unit To Convert To
                utct = calculator_interface.unit_format(unit = utct)
                if not calculator_interface.supported_unit_check(unit=utct):
                    print("This unit is not recognised, please try again.")
                else:
                    break
            except Exception:
                print("Error: invalid unit entered, try again.")
    
    
        from data_calculator import data_calculator

        calculator = data_calculator(value=user_value, unit = user_unit)
        converted_value = calculator_interface.FR_correct_conversion(calculator_instance=calculator, unit = utct)

        if user_unit[-1:].lower() == 's': user_unit = user_unit[:-1]
        if utct[-1:].lower() == 's': utct = utct[:-1]
        
        print(f"There are {converted_value:,} {utct}(s) in {user_value:,} {user_unit}(s)")