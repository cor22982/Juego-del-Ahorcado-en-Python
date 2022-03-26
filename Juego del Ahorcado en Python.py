#Autor: Mathew Alexander Cordero
#22/03/2022
#Ahorcado
import random
inicio = 0
while inicio == 0:
    palabras = ["rinoceronte", "tejuino", "quetzal", "tiranosaurio"]
    select = random.choice(palabras)

    print ("\nBienvenido al juego del ahorcado")
    enter = input("Presione enter para comenzar: ") #enter
    vidas = (len(select))*2  #las vidas
    rango = (len(select))*2  #limite
    select = list(select) #separa las letras

    mostrar = ['*']*len(select)
    
    print ("\nUsted tiene, 2 oportunidades por letra")
    print (" ")
    #dibujos de ahorcado en lista para llamarlos
    ahorcado = ['''
                +-------+
                |       |
                        |
                        |
                        |
                        |
               ===========''', '''              
                +-------+
                |       |
                0       |
                        |
                        |
                        |
               ===========''', '''
                +-------+
                |       |
                0       |
                |       |
                        |
                        |
               ===========''','''
                +-------+
                |       |
                0       |
                |\      |
                        |
                        |
               ===========''', '''
                +-------+
                |       |
                0       |
               /|\      |
                        |
                        |
               ===========''', '''
                +-------+
                |       |
                0       |
               /|\      |
               /        |
                        |
               ===========''', '''
                +-------+
                |       |
                0       |
               /|\      |
               / \      |
                        |
               ===========''']
    
    #se inicializa la primer imagen y las variables a usar
    print (ahorcado[0], "\nPalabra:", mostrar)
    seguir = 'si'
    muerte = 0
    acertados = 0
    erroneas = []
    
    while (seguir == 'si') and (vidas >= 1):
        letra = input("\nIngrese la letra: ")
        letra.lower()
        lst = [] #listas para almacenar las palabras
        if letra in select:
        #Ayuda a colocar cada palabra en una posicion
            for pos, char in enumerate(select): 
                if (char == letra):
                    lst.append(pos) #no lo devuelve como lista
            ingresado = select.count(letra) #cuenta el no de veces
            vidas = vidas - (ingresado*2) #las vidas restadas
            acertados = acertados + 1     #lo acertado
            print ("\nCORRECTO")
            
        for i in lst:                 #coloca cada valor de la lista en i
            mostrar[i] = letra        #lo muestra
        
        if letra not in select:       
            vidas = vidas - 1         #si se equivoca se le resta solo 1
            muerte = muerte + 1       #se suman las muertes
            erroneas.append(letra)    #se añaden las palabras erroneas
            print ("\nINCORRECTO")
            
        mostrar_ahorcado = (muerte*100)/rango
        if (mostrar_ahorcado == 0):
            print (ahorcado[0])
        
        if (mostrar_ahorcado > 0) and (mostrar_ahorcado <= 20):
            print (ahorcado[1])
            
        if (mostrar_ahorcado > 20) and (mostrar_ahorcado <= 40):
            print (ahorcado[2])
        
        if (mostrar_ahorcado > 40) and (mostrar_ahorcado <= 60):
            print (ahorcado[3])
            
        if (mostrar_ahorcado > 60) and (mostrar_ahorcado <= 80):
            print (ahorcado[4])
            
        if (mostrar_ahorcado > 80):
            print (ahorcado[5])
        
        if (muerte == rango):
            print (ahorcado[6])
               
        print(mostrar,"Intentos restantes: ", vidas)
        seguir = input('desea seguir? (si/no) ')
        
    print ("\nLetras incorrectas: ", erroneas)
    print ("¡TE QUEDASTE SIN INTENTOS!")
    print("Te equivocaste", muerte, "veces", "y acertaste", acertados, "veces")
    print ("La palabra era: ", select)
    continuar =  input("Iniciar nueva partida (si/no): ")
    
    if (continuar == "no"):
        inicio = 2
    if (continuar == "si"):
        select = random.choice(palabras) 

print("\nGracias por participar")