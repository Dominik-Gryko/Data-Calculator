class data_calculator:
    def __init__(self, value = None, unit = None): # conversion_type = "Decimal" removed binary conversion for now!

        self.unit_type = unit.lower() #like megabytes or gigabytes
        self.conversion_type = "decimal" # binary or decimal conversion. 1024 or self.decimal_value
        
        
        self.value = value # value before conversion
        self.conversion_value = None #used to calculate the value that will be used to find the final value.
        self.byte_value = None

        self.unit_value = 0 #this will be used to calculate the final value into bytes
        self.decimal_value = 1000
        self.binary_value = 1024
        
        self.find_conversion_type()

        if "bit" in self.unit_type: 
            self.init_bits()
        elif "byte" in self.unit_type:
            self.init_bytes()
        else:
            print("ERROR: COULD NOT RECOGNISE THE DATA TYPE")

        
    
    def init_bits(self):
        if self.unit_type in ["bits"]: 
            self.bit_value = self.value
        elif self.unit_type in ["kilobits"]:
            self.bit_value = (self.value * self.decimal_value)
        elif self.unit_type in ["megabits"]:
            self.bit_value = (self.value * (self.decimal_value ** 2))
        elif self.unit_type in ["gigabits"]:
            self.bit_value = (self.value * (self.decimal_value ** 3))
        elif self.unit_type in ["terabits"]:
            self.bit_value = (self.value * (self.decimal_value ** 4))
        elif self.unit_type in ["petabits"]:
            self.bit_value = (self.value * (self.decimal_value ** 5))      
        else:
            return "ERROR: CANT RECOGNISE THIS DATA TYPE (FROM init_bits)"
        
        self.byte_value = self.bit_value/8  

    def init_bytes(self):

        if self.unit_type in ["bytes"]:
            self.byte_value = self.value   
        elif self.unit_type in ["kilobytes"]:
            self.byte_value = self.value * (self.decimal_value)
        elif self.unit_type in ["megabytes"]: 
            self.byte_value = self.value * (self.decimal_value ** 2)
        elif self.unit_type in ["gigabytes"]: 
            self.byte_value = self.value * (self.decimal_value ** 3)
        elif self.unit_type in ["terabytes"]: 
            self.byte_value = self.value * (self.decimal_value ** 4)
        elif self.unit_type in ["petabytes"]: 
            self.byte_value = self.value * (self.decimal_value ** 5)
        else:
            return "ERROR: CANT RECOGNISE THIS DATA TYPE (FROM init_bytes)"
        self.bit_value = self.byte_value * 8
        #self.byte_value = self.value * self.unit_value

    def find_conversion_type(self):
        if self.conversion_type.lower() == "binary": self.conversion_value = 1024
        elif self.conversion_type.lower() == "decimal": self.conversion_value = 1000
        else: print("ERROR: Incorrect Conversion Type.")
    
    
    def convert_to_bytes(self):
        return self.byte_value
    
    def convert_to_kilobytes(self):
        return self.byte_value / self.decimal_value

    def convert_to_megabytes(self):
        return self.byte_value / (self.decimal_value ** 2)
    
    def convert_to_gigabytes(self):
        return self.byte_value / (self.decimal_value ** 3)

    def convert_to_terabytes(self):
        return self.byte_value / (self.decimal_value ** 4)

    def convert_to_petabytes(self):
        return self.byte_value / (self.decimal_value ** 5)

    def convert_to_bits(self):
        return (self.byte_value * 8)
    
    def convert_to_kilobits(self):
        return (self.byte_value * 8) / self.decimal_value
    
    def convert_to_megabits(self):
        return (self.byte_value * 8) / (self.decimal_value ** 2)
    
    def convert_to_gigabits(self):
        return (self.byte_value * 8) / (self.decimal_value ** 3)
    
    def convert_to_terabits(self):
        return (self.byte_value * 8) / (self.decimal_value ** 4)
    
    def convert_to_petabits(self):
        return (self.byte_value * 8) / (self.decimal_value ** 5)
