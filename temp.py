print("Temperaure Converter: Fahrenheit to Celsius")

fah_numb = input("Please enter the °F temperature that you would like to convert: ")
fah_numb = int(fah_numb)

cel_numb = (fah_numb - 32) * 5 / 9
cel_numb = int(cel_numb)

print(f"{fah_numb}°F is equal to {cel_numb}°C")
