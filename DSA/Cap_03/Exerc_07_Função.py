Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda f: (float(9)/5)*f + 32, Celsius)
print (list(Fahrenheit))