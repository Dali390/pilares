import random
import string

# Importación del archivo de palabras y del diccionario visual
from palabras import palabras
from vidas_ahorcado1 import vidas_ahorcado1


def obtener_palabra_válida(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def ahorcado():
    print("========================================")
    print("¡ Bienvenido(a) al juego del Ahorcado !")
    print("========================================")

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra)
    abecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()
    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"\nTe quedan {vidas} vidas y has usado estas letras: {' '.join(sorted(letras_adivinadas))}")

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_ahorcado1[7])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input('Escoge una letra : ').upper()
        #Validación de entrada
        if len(letra_usuario)!= 1 or letra_usuario not in abecedario:
            print("\nEntrada inválida.Por favor ingresa una sola letra abecedario")
            continue
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("¡Bien hecho! Esa letra está en la palabra.")
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario}, no está en la palabra.")
        elif letra_usuario in letras_adivinadas:
            print(f"\nYa escogiste esa letra{letra_usuario}Por favor escoge una letra nueva.")
            continue
        else:
            print("\nEsta letra no es válida.")

    # Resultado final del juego
    if vidas == 0:
        print(vidas_ahorcado1[7]) # Última imágen del ahorcado
        print(f"¡Ahorcado! Perdiste. La palabra era: {palabra}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")
# Corrección en la ejecución principal
if __name__ == '__main__':
    ahorcado () 