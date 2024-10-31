'''
CARRERA DE TORTUGAS
'''
donatello, mbappe=0,0
import random
meta=50
print("¡EMPIEZA LA CARRERA!")
while donatello<meta and mbappe<meta:
    input("Presiona Enter para el próximo turno....")
    donatello+=random.randint(1,5)
    mbappe+=random.randint(1,5)
    print(f"Donatello: {donatello} pasos, Mbappe: {mbappe} pasos")
    
if donatello>= meta and mbappe>=meta:
    print("¡Es un empate!")

elif donatello>=meta:
    print("¡Donatello ganó la carrera!")
    
else:
    print("¡Mbappe ganó la carrera!")