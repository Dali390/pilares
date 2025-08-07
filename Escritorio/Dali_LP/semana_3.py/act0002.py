print("!Hola¡")
nombre=input("Ingrese su nombre , por favor: ")
print(f"Bienvenido a este programa", {nombre}, "gracias por estar con con nosotros ... \n" )
deuda_pagos=float(input("¿Cuántos pagos debera hacer para cubrir su deuda total?   \n"))
print(f"Producto comprado a crédito, a {deuda_pagos} pagos mensuales,sigue una Progresión geométirca en la que:\n")
a=float(input("Ingrese su primer pago  del mes que da: \n "))
b=float(input("Ingrese su Segundo pago del mes que da: \n "))
c=float(input("Ingrese su Tercer  pago del mes que da: \n "))

#Suponiendo una progresión geométrica con razón r=2
r=2
#Fórmula de la suma de una progresión  geométrica: 

n=deuda_pagos #número  de pagos totales.

Sn= a* (r** n-1)/(r--1)

print(f"\nLa persona debe pagar un total de {Sn:.2f} euros en {n} meses.")




