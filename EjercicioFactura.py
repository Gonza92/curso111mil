'''
Created on Nov 4, 2017

@author: Fiorella
'''
#print ("Hola")

def MostrarProductos (matriz):
    for a in range(0,len(matriz[0])):
        print(str(a) + "-  " +matriz[0][a]+" -  $" + str(matriz[1][a]))

def MostrarTicket (matriz):
    SumaTotalTicket = 0 
    for a in range(0,len(matriz[0])):
        print(matriz[0][a] , "-  " +matriz[1][a]," -  $" , matriz[2][a])
        SumaTotalTicket=(SumaTotalTicket + matriz[2][a])
    print ("Total: $",SumaTotalTicket)
        

productos= [["Morfi","Droga","Amor","Puchos"],[55,648,40,60]]

MostrarProductos(productos)

ticket= [[],[],[]]

termina= 'no'
MostrarProductos(productos)

while termina=='no':
    
    codigo = input("Ingresar codigo de articulo")
    cantidad= input("Ingresar cantidad")
    ticket[0].append(int(cantidad))
    ticket[1].append(productos[0][int(codigo)])
    ticket[2].append(int(cantidad)*productos[1][int(codigo)])
    termina = input("termina? si/no")
    
MostrarTicket(ticket)
