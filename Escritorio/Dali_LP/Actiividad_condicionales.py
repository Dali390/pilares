#Bienvenida 
nombre=input("Escriba su nombre: ")
print(f"¡Hola!, Bienvenido(a) al sistema, {nombre}. Gracias por usar el programa")



    #Se pide al usuario ingresar un número
try:
    
   num1 = int(input(f"Introduzca un número,* {nombre}: "))

   
    #Verificación de valores con la tabla del 1      

   if num1 == 1 * 1:
       print(f"El resultado es: {num1}")
   elif num1== 1 * 2:
       print(f"El resultado es: {num1}")
   elif num1== 1 * 3:
       print(f"El resultado es: {num1}")
   elif num1== 1 * 4:
       print(f"El resultado es: {num1}")
   elif num1== 1 * 5:
       print(f"El resultado es: {num1}") 
   elif num1== 1 * 6:
       print(f"El resultado es: {num1}") 
   elif num1== 1 * 7:
       print(f"El resultado es: {num1}")
   elif num1== 1 * 8:
       print(f"El resultado es: {num1}")
   elif num1== 1 * 9:
       print(f"El resultado es: {num1}")
   elif num1== 1 * 10:
       print(f"El resultado es: {num1}")
   else:
       print(f"El número {num1} no está en la tabla del 1.")

except ValueError:  
    print("El número ingresado en la tabla del 1.")






    




