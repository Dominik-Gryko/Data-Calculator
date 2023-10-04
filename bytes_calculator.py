import math

class byte_calculator:
    def __init__(self, value = None, unit = None, conversion_type = None):

        self.unit_type = unit.lower()
        self.unit_value = 0
        self.value_in_bytes = 0
        self.value = value
        self.conversion_type = conversion_type
        self.conversion_value = None

    def find_conversion_type(self):
        if self.conversion_type.lower() == "binary": self.conversion_value = 1024
        elif self.conversion_type.lower() == "decimal": self.conversion_value = 1000
        else: print("ERROR: Incorrect Conversion Type.")
    
    
    def find_unit_value(self):

        if self.conversion_type == None: return
        
        if self.unit_type in ["kilobytes", "kb"]: self.unit_value = self.conversion_value
        elif self.unit_type in ["megabytes", "mb"]: self.unit_value = self.conversion_value ^ 2
        elif self.unit_type in ["gigabytes", "gb"]: self.unit_value = self.conversion_value ^ 3
        elif self.unit_type in ["terrabytes", "tb"]: self.unit_value = self.conversion_value ^ 4
        elif self.unit_type in ["petabytes", "pb"]: self.unit_value = self.conversion_value ^ 5
    
    def calculate_bytes(self):
        self.value_in_bytes = self.value / self.unit_value
        return self.value_in_bytes
