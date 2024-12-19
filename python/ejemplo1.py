print("Bienvenido")
numero1 = 80
numero2 = 30
#aqui inicia nuestro programa 
estatura = float(input("Escriba su estatura en metros: "))
edad = int(input("Escriba su edad: "))
peso = int(input("Escriba su peso en valor entero: "))
nombre = input("Escriba su nombre completo: ")
aprobo = bool(input("Escriba True si aprobo/ Fañse si reprobo el curso: "))

resultado = numero1 + numero2
print("el resultado de la operacion es", resultado)
resultado = edad * peso

if edad % 2 == 0 : 
    print("La edad corresponde a un numero par")
else: 
    print("La edad corresponde a un numero impar")
    

print(f"mi nombre es:  {nombre} mi edad es: {edad} mi estatura es: {estatura} y aprobo {aprobo} aprobo o no el año ")
print("El resultado de la multiplicación de peso x edad es: ", round(resultado,2))