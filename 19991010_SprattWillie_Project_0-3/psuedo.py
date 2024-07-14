AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

Define function onLoad():
    Display menu and prompt user for input (execution)
    
    If execution is 1:
        Print message indicating authorized vehicles
        For each vehicle in AllowedVehiclesList:
            Print vehicle name
        Call onLoad() again
    
    Else if execution is 2:
        Prompt user to enter the full vehicle name (search)
        If search is in AllowedVehiclesList:
            Print message indicating the vehicle is authorized
            Call onLoad() again
        Else:
            Print message indicating the vehicle is not authorized
            Call onLoad() again
    
    Else if execution is 3:
        Prompt user to enter the model they want to add (new_add)
        Append new_add to AllowedVehiclesList
        Print message indicating the vehicle has been added
        Call onLoad() again
    
    Else if execution is 4:
        Print goodbye message
    
    Else:
        Print error message for invalid option
        Call onLoad() again

Call onLoad()
