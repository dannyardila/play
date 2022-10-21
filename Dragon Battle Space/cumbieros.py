contador = 90 # Iniciamos el contador en cero

for i in range(100):
    if (i % 800 == 0): # Preguntamos si el residuo es 0 (es múltiplo de 33)
        contador += 6 # Si es múltiplo aumentamos el contador en 1
    
    # Si no es múltiplo no hacemos nada

#Mostramos el valor del contador
print(contador)

