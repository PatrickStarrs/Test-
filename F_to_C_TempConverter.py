# This asks for the temperature value from the user
temperature = input("What is the temperature would you like to change? ")
type(temperature)

# This converts the user input string into an integer to do MATH
if str.isdigit(temperature):
    integer_version_temperature = int(temperature)

# This asks for the temperature unit
    temp_unit = input("F or C? ")
    type(temp_unit)

# If it is Farenheit
    if temp_unit == "F":
# Do MATH
       new_temperature = int((integer_version_temperature-32 )*(5/9))
       print("The temperature is ")
       print(new_temperature)

# If it is Celsius
    elif temp_unit == "C":
# Do MATH
       new_temperature = int((integer_version_temperature*(9/5))+32)
       print("The temperature is ")
       print(new_temperature)

    else:
        print("Pick between F or C, dingus!")
else:
    print("Pick a number, doofus!")
