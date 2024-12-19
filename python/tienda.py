# Ejercicio para determinar si la tienda obtuvo ganancias o perdidas a final de mes

ingresos = float(input("Escrinba el valor de los Ingresos del mes: "))
gastos = float(input("Escrinba el valor de los Gastos del mes: "))

if ingresos == gastos :
    print(" La tienda no obtuvo ni perdidas ni ganancias.")
  
elif ingresos > gastos :
    resultado = ingresos - gastos
    print(" la tienda obtuvo ganancias durante el mes por valor de: ", resultado)
else:
    resultado = gastos - ingresos
    print(" la tienda obtuvo perdidas durante el mes por valor de: ", resultado)
    
