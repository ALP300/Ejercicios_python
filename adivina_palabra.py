'''
JUEGO ADIVINA LA PALABRA
'''
def adivina_palabra():
    palabra_secreta= "barcelona real madrid"
    letras_adivinadas=[]
    intentos=6
    print("Bienvenido al juego de Adivina palabra!")
    print("_ "*len(palabra_secreta))
    while intentos>0:
        letra= input("Adivina una letra: ").lower()
        if letra in letras_adivinadas:
            print("Ya adivinaste una letra")
        elif letra in palabra_secreta:
            letras_adivinadas.append(letra)
        else:
            intentos-=1
            print(f"Incorrecto. Te quedan {intentos} intentos")
        
        palabra_oculta= [ letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print("".join(palabra_oculta))

        if "_" not in palabra_oculta:
            print("Felicidades, ganaste!")
            break
    else:
        print(f"Perdiste, la palabra era: {palabra_secreta}")
    
adivina_palabra()