class data_calculator:
    def __init__(self, value = None, unit = None, conversion_type = None):

        self.unit_type = unit.lower() #like megabytes or gigabytes
        self.conversion_type = conversion_type # binary or decimal conversion. 1024 or 1000
        
        
        self.value = value # value before conversion
        self.conversion_value = None #used to calculate the value that will be used to find the final value.
        self.byte_value = None

        self.calculate_bytes()

    
    def find_conversion_type(self):
        if self.conversion_type.lower() == "binary": self.conversion_value = 1024
        elif self.conversion_type.lower() == "decimal": self.conversion_value = 1000
        else: print("ERROR: Incorrect Conversion Type.")
    
    
    def calculate_bytes(self):
        unit_value = 0 #this will be used to calculate the final value into bytes
        temp_value = self.value

        if self.conversion_value == None:
            self.find_conversion_type()

        if self.unit_type in ["kilobytes", "kb"]:
            unit_value = self.conversion_value 
        elif self.unit_type in ["megabytes", "mb"]: 
            unit_value = self.conversion_value ** 2
        elif self.unit_type in ["gigabytes", "gb"]: 
            unit_value = self.conversion_value ** 3
        elif self.unit_type in ["terrabytes", "tb"]: 
            unit_value = self.conversion_value ** 4
        elif self.unit_type in ["petabytes", "pb"]: 
            unit_value = self.conversion_value ** 5

        #temp_value = temp_value * (self.conversion_value ** )

        #self.byte_value = temp_value    
        self.byte_value = self.value * unit_value
        return self.byte_value
    
    def calculate_kilobytes(self):
        if self.byte_value == None: self.calculate_bytes()
        return self.byte_value / self.conversion_value

    def calculate_megabytes(self):
        if self.byte_value == None: self.calculate_bytes()
        return self.byte_value / (self.conversion_value ** 2)
    
    def calculate_gigabytes(self):
        if self.byte_value == None: self.calculate_bytes()
        return self.byte_value / (self.conversion_value ** 3)

    def calculate_terrabytes(self):
        if self.byte_value == None: self.calculate_bytes() 
        return self.byte_value / (self.conversion_value ** 4)

    def calculate_petabytes(self):
        if self.byte_value == None: self.calculate_bytes() 
        return self.byte_value / (self.conversion_value ** 5)



calc = data_calculator(value=1, unit = "pb", conversion_type="binary")
print(calc.calculate_kilobytes())