# Defining basic Variables
cas_number = "7732-18-5"
rho = 1000  # Density
mu = 1  # Viscosity
Tm = 273.15  # Melting Point
Tb = 373.13  # Boiling Point
k = 0.58  # Thermal Conductivity

def convert_to_kelvin(temperature, units):
    checkValid = False

    while checkValid is False:
        try:
            temperature = float(temperature)
            checkValid = True
        except:
            return None

    if units == "C":
        temperature = temperature + Tm
        return temperature
    elif units == "F":
        temperature = (temperature - 32) * 5 / 9 + Tm
        return temperature
    elif units == "K":
        return temperature
    else:
        return None


def is_gas(temperature):
    checkValid = False

    while checkValid is False:
        try:
            temperature = float(temperature)
            checkValid = True
        except:
            return None

    if temperature >= Tb:
        return True
    else:
        return False


def is_liquid(temperature):
    checkValid = False

    while checkValid is False:
        try:
            temperature = float(temperature)
            checkValid = True
        except:
            return None

    if temperature < Tb and temperature >= Tm:
        return True
    else:
        return False


def is_solid(temperature):
    checkValid = False

    while checkValid is False:
        try:
            temperature = float(temperature)
            checkValid = True
        except:
            return None

    if temperature < Tm:
        return True
    else:
        return False


unit = input("Which unit would you like to use (C, F, K): ")

temperature = input("Input the temperature: ")

temperatureInKelvin = convert_to_kelvin(temperature, unit)

if temperatureInKelvin is None:
    print("Invalid input!")
elif is_gas(temperatureInKelvin) is True:
    print("Water at this temperature is a gas ! ")
elif is_liquid(temperatureInKelvin) is True:
    print("Water at this temperature is a liquid ! ")
elif is_solid(temperatureInKelvin) is True:
    print("Water at this temperature is a solid ! ")