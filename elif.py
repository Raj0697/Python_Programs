var1 = 1+2j
if(type(var1)==int):
    print("Type of the variable is integer")
elif(type(var1)==float):
    print("Type of the variable is float")
elif(type(var1)==complex):
    print("Type of the variable is complex")
elif(type(var1)==bool):
    print("Type of the variable is bool")
elif(type(var1)==str):
    print("Type of the variable is string")
elif(type(var1)==tuple):
    print("Type of the variable is Tuple")
elif(type(var1)==dict):
    print("Type of the variable is dictionaries")
elif(type(var1)==list):
    print("Type of the variable is list")
else:
    print("Type of the variable is unknown")
