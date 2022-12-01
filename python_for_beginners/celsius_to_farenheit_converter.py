user_input = input("Enter a temperature to convert. Temperature should be an integer: ")
temperature_in_celsius = int(user_input)


def farenheit(celsius_temperature):
    farenheit_temperature = 1.8 * celsius_temperature + 32
    return float(farenheit_temperature)


temperature_in_farenheit = farenheit(temperature_in_celsius)
print("The Fahrenheit equivalent of " + user_input + " degrees Celsius is " + str(temperature_in_farenheit))
