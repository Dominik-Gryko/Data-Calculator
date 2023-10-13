def main_menu():
    print("""
1.Go to Calculator
2.View previous calculations (WIP)
0.Exit program
""")
    
    while True:
        mm_choice = int(input("Enter the number corresponding to your choice: "))
        if mm_choice == 1:
            
            from interfaces import calculator_interfaces
            calculator_interface.interface()
            break
        elif mm_choice == 2:
            print("Work in progress, not available yet.")
            break
        elif mm_choice == 0:
            import sys
            sys.exit()
        else:
            print("Error: Invalid choice please try again.")   



main_menu()






