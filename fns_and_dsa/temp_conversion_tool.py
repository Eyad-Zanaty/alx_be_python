try:
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
    temperature = int(input("Enter the temperature to convert:"))
    specify = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    def convert_to_celsius(fahrenheit):
        celisuis = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f'{fahrenheit}°F is {celisuis}°C')
    def convert_to_fahrenheit(celsius):
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f'{celsius}°C is {fahrenheit}°F')
    if specify == 'F':
        convert_to_celsius(temperature)
    elif specify == 'C':
        convert_to_fahrenheit(temperature)
except ValueError as ve:
    print("Invalid temperature. Please enter a numeric value.")