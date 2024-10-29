'''
CARRERA DE DADOS
'''
import random

def carrera_datos():
    puntos_jugador=0
    puntos_computadora=0
    print("Bienvenido a la Carrera de Dados, el primero en llegar a 20, gana!!")
    
    while puntos_jugador<20 and puntos_computadora<20:
        input("Presionar Enter para lanzar los dados")
        lanzamiento_jugador= random.randint(1,6)
        puntos_jugador+=lanzamiento_jugador
        print(f"Has sacado un {lanzamiento_jugador}. Tienes {puntos_jugador} puntos")
        
        lanzamiento_computadora=random.randint(1,6)
        puntos_computadora+=lanzamiento_computadora         
        print(f"Has sacado un {lanzamiento_computadora}. Tienes {puntos_computadora} puntos")

    if puntos_jugador>=20:
            print("Felicidades has ganado!!!")
    else:
            print("La computadora te ha ganado,pipipipi :(")
            
            
carrera_datos()