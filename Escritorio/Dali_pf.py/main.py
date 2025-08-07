import random
import string

# Importaciones de módulos externos
from palabras import palabras
from vidas_ahorcado import vidas_ahorcado

def obtener_palabra_valida(lista_palabras):
    palabra = random.choice(lista_palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(lista_palabras)
    return palabra.upper()

def ahorcado():
    print("========================================")
    print("¡ Bienvenido(a) al juego del Ahorcado !")
    print("========================================")

    palabra = obtener_palabra_valida(palabras)
    letras_por_adivinar = set(palabra)
    abecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()
    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"\nTe quedan {vidas} vidas y has usado estas letras: {' '.join(sorted(letras_adivinadas))}")
        print(vidas_ahorcado[vidas])

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if len(letra_usuario) != 1 or letra_usuario not in abecedario:
            print("\nEntrada inválida. Por favor ingresa una sola letra del abecedario.")
            continue

        if letra_usuario in letras_adivinadas:
            print(f"\nYa escogiste la letra {letra_usuario}. Intenta con una nueva.")
            continue

        letras_adivinadas.add(letra_usuario)

        if letra_usuario in letras_por_adivinar:
            letras_por_adivinar.remove(letra_usuario)
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            vidas -= 1
            print(f"\nLa letra {letra_usuario} no está en la palabra.")

    if vidas == 0:
        print(vidas_ahorcado[0])
        print(f"¡Ahorcado! Perdiste. La palabra era: {palabra}")
    else:
        print(f"\n¡Excelente! ¡Adivinaste la palabra: {palabra}!")

if __name__ == "__main__":
    ahorcado()