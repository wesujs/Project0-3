AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


def onLoad():
    
    execution = int(input(""" 
********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. Exit"                         
"""))
    
    if execution == 1:
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for make in AllowedVehiclesList:
            print(make)
        onLoad()
        
    elif execution == 2:
        search = input("""
********************************
Please Enter the full Vehicle name: """)
        if search in AllowedVehiclesList:
            print(search, "is an authorized vehichle\n\n")
            onLoad()
        else:
            print(search, "is not an authorized vehicle, if you received this in error please check the spelling and try again\n\n")
            onLoad()

    elif execution == 3:
        new_add = input("What Model Would you like to add: ")
        AllowedVehiclesList.append(new_add)
        print("You have added " + new_add + " as an authorized vehicle")
        onLoad()

    elif execution == 4:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    
    elif execution != 2 and execution != 1:
        print("Sorry Try Again with the avaialble options")
        onLoad()
        
        
onLoad()