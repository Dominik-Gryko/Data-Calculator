def main_menu():
        print("""
1.Go to Calculator
2.View previous calculations (WIP)
""")

def units_menu():
    print("""The available units are: 
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
