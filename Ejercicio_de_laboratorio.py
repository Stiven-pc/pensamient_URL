saldo = 3000  
intentos = 0  
maximo_intentos = 3  

while True:
    print(f"Saldo actual: Q{saldo}")
    monto = int(input("Ingrese monto a retirar (0 para salir): "))
    
    if monto == 0:
        print("Gracias por usar el cajero. Adiós.")
        break
    
    if monto > saldo:
        intentos += 1
        print(f"Saldo insuficiente. Intentos restantes: {maximo_intentos - intentos}")
        if intentos >= maximo_intentos:
            print("Se ha alcanzado el número máximo de intentos. Adiós.")
            break
    else:
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: Q{saldo}")
        
        if saldo == 0:
            print("Saldo agotado. Adiós.")
            break
        
        intentos = 0

