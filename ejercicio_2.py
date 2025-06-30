'''un estduiante presenta tres evaluaciones con peos del 30%, 30% y 40%. Se requiere calcular el promedio final '''
# declaramos las variables y pedimos datos por teclado
nota_1 = float(input("ingrese la nota 1: "))
nota_2 = float(input("ingrese la nota 2: "))
nota_3 = float(input("ingrese la nota 3: "))

#  impementamos operadores

nota_1 *= 0.30
nota_2 *= 0.30
nota_3 *= 0.40

promedio = nota_1 + nota_2 + nota_3

print(f"el promedio es: {promedio}")