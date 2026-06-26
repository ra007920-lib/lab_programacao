def celsius_para_fahrenheit (c):
    f = c *1.8 + 32
    return (f)

celsius = float(input("Insira o valor em celsius: "))

print("Farenheit = Celsius * 1.8 + 32")
print(f"A conversão de {celsius} para Fahrenheit será: {celsius_para_fahrenheit(celsius)}")