#! python3

def tateti():
    juego_terminado = False
    first_player = 'X'
    second_player = 'O'
    turn = 0
    tablero = {'ArribaIzquierda' : ' ','ArribaCentro' : ' ', 'ArribaDerecha' : ' ', 
    'CentroIzquierda' : ' ', 'CentroCentro' : ' ', 'CentroDerecha' : ' ',
    'AbajoIzquierda' : ' ', 'AbajoCentro' : ' ','AbajoDerecha' : ' '}
    
    #Loop principal
        #Instrucciones
    print('Para jugar, usa el numepad como si fuera el tablero de tateti\no elegi una posicion en el tablero con las primeras dos iniciales de la fila\ny la primer letra de la posicion dentro de la fila.\nPor ejemplo para ponerla arriba al centro es: arc (AR-riba C-entro). \n\n')
    print('TA TE TI')
    while juego_terminado == False:
        
        #Separando los turnos
        if turn % 2 == 0:
            player = first_player
        else:
            player = second_player
        
        print('|{}|{}|{}|\n- - - -\n|{}|{}|{}|\n- - - -\n|{}|{}|{}|'.format(tablero['ArribaIzquierda'],tablero['ArribaCentro'],tablero['ArribaDerecha'],tablero['CentroIzquierda'],tablero['CentroCentro'],tablero['CentroDerecha'],tablero['AbajoIzquierda'],tablero['AbajoCentro'],tablero['AbajoDerecha']))
        #Pedirle al jugador donde quiero poner su figura
        jugada = str(input('¿Donde queres poner la {}?: '.format(player)))

        #Asignando cruz o cicedulo al dicecionario
        if jugada == 'ari' or jugada == '7':
            if tablero['ArribaIzquierda'] == ' ': 
                tablero['ArribaIzquierda'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        elif jugada == 'arc' or jugada == '8':
            if  tablero['ArribaCentro'] == ' ':   
                tablero['ArribaCentro'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        elif jugada == 'ard' or jugada == '9':
            if tablero['ArribaDerecha'] == ' ':
                tablero['ArribaDerecha'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        elif jugada == 'cei' or jugada == '4':
            if tablero['CentroIzquierda'] == ' ':
                tablero['CentroIzquierda'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        elif jugada == 'cec' or jugada == '5':
            if tablero['CentroCentro'] == ' ':
                tablero['CentroCentro'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        elif jugada == 'ced' or jugada == '6':
            if tablero['CentroDerecha'] == ' ':
                tablero['CentroDerecha'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        elif jugada == 'abi' or jugada == '1':
            if tablero['AbajoIzquierda'] == ' ':
                tablero['AbajoIzquierda'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        elif jugada == 'abc' or jugada == '2':
            if tablero['AbajoCentro'] == ' ':
                tablero['AbajoCentro'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        elif jugada == 'abd' or jugada == '3' :
            if tablero['AbajoDerecha'] == ' ':
                tablero['AbajoDerecha'] = player
            else:
                print('Este posición ya fue ocupada, por favor elegi otra')
                continue
        else:
            print('Jugada invalida, por favor realice una jugada valida') 
            continue

        #Condiciones para ganar
        if tablero['AbajoDerecha'] == tablero['AbajoCentro'] and tablero['AbajoCentro'] == tablero['AbajoIzquierda'] and tablero['AbajoDerecha'] != ' ' :
            juego_terminado = True
        elif tablero['CentroDerecha'] == tablero['CentroCentro'] and tablero['CentroCentro'] == tablero['CentroIzquierda'] and tablero['CentroDerecha'] != ' ' :
            juego_terminado = True
        elif tablero['ArribaDerecha'] == tablero['ArribaCentro'] and tablero['ArribaCentro'] == tablero['ArribaIzquierda'] and tablero['ArribaDerecha'] != ' ':
            juego_terminado = True
        elif tablero['ArribaDerecha'] == tablero['CentroCentro'] and tablero['CentroCentro'] == tablero['AbajoIzquierda'] and tablero['ArribaDerecha'] != ' ':
            juego_terminado = True
        elif tablero['ArribaIzquierda'] == tablero['CentroCentro'] and tablero['CentroCentro'] == tablero['AbajoDerecha'] and tablero['ArribaIzquierda'] != ' ':
            juego_terminado = True
        elif tablero['ArribaDerecha'] == tablero['CentroDerecha'] and tablero['CentroDerecha'] == tablero['AbajoDerecha'] and tablero['ArribaDerecha'] != ' ':
            juego_terminado = True
        elif tablero['ArribaIzquierda'] == tablero['CentroIzquierda'] and tablero['CentroIzquierda'] == tablero['AbajoIzquierda'] and tablero['ArribaIzquierda'] != ' ':
            juego_terminado = True
        elif tablero['ArribaCentro'] == tablero['CentroCentro'] and tablero['CentroCentro'] == tablero['AbajoCentro'] and tablero['ArribaCentro'] != ' ':
            juego_terminado = True
        
        #Si el tablero esta lleno    
        if turn == 8 and juego_terminado == False:
            print('|{}|{}|{}|\n- - - -\n|{}|{}|{}|\n- - - -\n|{}|{}|{}|'.format(tablero['ArribaIzquierda'],tablero['ArribaCentro'],tablero['ArribaDerecha'],tablero['CentroIzquierda'],tablero['CentroCentro'],tablero['CentroDerecha'],tablero['AbajoIzquierda'],tablero['AbajoCentro'],tablero['AbajoDerecha']))
            print('Empate')
            break
        elif juego_terminado == True:
            print('|{}|{}|{}|\n- - - -\n|{}|{}|{}|\n- - - -\n|{}|{}|{}|'.format(tablero['ArribaIzquierda'],tablero['ArribaCentro'],tablero['ArribaDerecha'],tablero['CentroIzquierda'],tablero['CentroCentro'],tablero['CentroDerecha'],tablero['AbajoIzquierda'],tablero['AbajoCentro'],tablero['AbajoDerecha']))
            print('{} gano'.format(player))
            
                  
        turn += 1

        
        
tateti()
    


