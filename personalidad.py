'''
TEST DE PERSONALIDAD
'''
print("¡DESCUBRE TU PERSONALIDAD! RESPONDE CON A O B")
respuestas=[]
respuestas.append(input("¿Prefieres la playa (A) o montaña(B)?: ").upper())
respuestas.append(input("¿Te gusta la música clásica (A) o rock(B)?: ").upper())
respuestas.append(input("¿Prefieres el día (A) o la noche(B)?: ").upper())
respuestas.append(input("¿Prefieres leer un libro (A) o ver una película(B)?: ").upper())
respuestas.append(input("¿Prefieres cocinar (A) o pedir delivery(B)?: ").upper())

if respuestas.count("A")>respuestas.count("B"):
    print("Tu personalidad es serena y tranquila")
else:
    print("Tu personalidad es de alguien energético")