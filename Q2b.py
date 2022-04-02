def switch(option):
    
    if option == "CSC1006":
        print("Mathematics 2")
    elif option == "CSC1007":
        print("Operating Systems")
    elif option == "CSC1008":
        print("Data Structures and Algorithms")
    elif option == "CSC1009":
        print("Object-Oriented Programming")
    elif option == "CSC2902":
        print("Career and Professional Development")
    else:
        print("Invaild option.")

        
option = input("Please enter the module code:")
switch(option.upper())


