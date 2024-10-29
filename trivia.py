'''
JUEGO DE TRIVIA SIMPLE
'''
def trivia():
    preguntas={
        "¿Cuál es la capital de Perú?:": "Lima",
        "¿Quién fue el primer presidente del Perú?:": "José De la Riva Aguero",
        "¿Quién escribió 100 años de soledad?:": "Gabriel García Marquez",
        "¿Cuántos continentes hay en el mundo?:": "7"
    }
    puntuacion=0
    for pregunta, respuesta in preguntas.items():
        respuesta_usuario= input(pregunta+ " ")
        if respuesta_usuario.lower()==respuesta.lower():
            print("CORRECTOOO!!!!!!")
            puntuacion+=1
        else:
            print(f"Incorrecto, la respuesta correcta es: {respuesta} ")
            
    print(f"Tu puntuación final es: {puntuacion}")
    

trivia()