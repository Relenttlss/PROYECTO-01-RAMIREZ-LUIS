#Se importan en el Módulo la base de datos correspondiente a LifeStore
#así como las listas a utilizar, Usuario y contraseña

import operator
from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products
import user
import passw


#<!-- DECLARACIÓN DE VARIABLES  -->

#Listas
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]

comprasTotales=[]
preciosTotales=[]
stock=[]

#Valores
Enero=0 
Febrero=0 
Marzo=0 
Abril=0 
Mayo=0 
Junio=0 
Julio=0 
Agosto=0 
Septiembre=0 
Octubre=0 
Noviembre=0 
Diciembre=0
y=('')
z=1


#El codigo empezará con una validación por parte del usuario creando credenciales
#para permitirle el acceso al menú.
#En el menú se le permitirá seleccionar la información que desea ver en la pantalla
#para evitar mostar todas las consignas al mismo tiempo

#<!--  CREDENCIALES  -->

def run():
    print("Registro\n")
    correcto=False
    while correcto==False:                                          #Primero en un ciclo que pedirá
            nombre=input("Ingrese nombre de usuario:\n")            #el nickname hasta ser validado
            if user.nickname(nombre) == True:
                print("\nUsuario creado con éxito\n")
                correcto=True

    while correcto==True:                                           #Segundo ciclo, esta vez solicitando 
        contrasenia=input("Ingrese contraseña:\n")                  #la contraseña hasta ser validada
        if passw.clave(contrasenia)==True:
            print("\nContraseña creada con éxito\n")
            correcto=False

    #Inicia el menú para mostrar la información que elegirá el usuario
    print("¡Bienvenido", nombre,"!")
    menu()

#<!--  ALGORITMOS DE ORDENAMIENTO  -->

#<!--  VENTAS  -->

for z in range(97):                                        #CICLO PRINCIPAL PARA RECABAR LA INFORMARCION
    x=0                                                    #DE CADA PRODUCTO (96 productos). Categoría (y), 
    i=0                                                    #ID_Producto (z), compras (i), calif (prom)
    r=0                                                    #devoluciones (d), ventas (s) y mes (m)
    d=0
    s=0
    prom=0


    #De la lista "lifestore_sales" se obtienen los valores con los que se trabajaran en este ciclo

    for row in lifestore_sales:

        valX = lifestore_sales[x][1]                       #Selecciona el Spot 1 de cada linea asignado a ID
                                                           #para contar cuantas veces se compró un objeto
        valW = lifestore_sales[x][2]                       #De igual manera el Spot 2 para las reseñas

        valD = lifestore_sales[x][4]                       #Spot 4 para revisar las devoluciones

        valF = lifestore_sales[x][3]                       #Spot 3 para revisar la fecha de venta
        valF = valF[3:5]                                   #Solo nos interesa el mes de la compra

        x+=1

        #Filtro de categorías (Decidí hacerlo con if para no hacer un hardcoding con las listas)
        #Se detecta el producto analizado en el loop actual (z), si corresponde, se suma una compra,
        #se le asigna su categoría y el mes de compra

    
        if valX == z:                                      
            if valD == 1:                                  #Revisa si hay alguna devolución
                d-=1
            #Categoría
            if z<10:
                y = 'Procesadores'            
            elif z>9 and z<29:
                y = 'Tarjetas de video'           
            elif z>28 and z<47:
                y = 'Tarjetas madre'        
            elif z>46 and z<60:
                y = 'Discos duros'           
            elif z==60 or z==61:
                y = 'Memorias USB'           
            elif z>61 and z<74:
                y = 'Pantallas'           
            elif z>73 and z<84:
                y = 'Bocinas'          
            elif z>83:
                y = 'Audifonos'
            
            i+=1                                             #Suma las compras (i), las calificaciones (r)
            r=r+valW                                         #y finalmente, el promedio de calif (prom)
            prom=r/i
        
        #Se filtra el mes de compra para saber en que mes se realizaron mas compras
            if valF=='01':
                Enero+=1
            elif valF=='02':
                Febrero+=1
            elif valF=='03':
                Marzo+=1
            elif valF=='04':
                Abril+=1
            elif valF=='05':
                Mayo+=1
            elif valF=='06':
                Junio+=1
            elif valF=='07':
                Julio+=1
            elif valF=='08':
                Agosto+=1
            elif valF=='09':
                Septiembre+=1
            elif valF=='10':
                Octubre+=1
            elif valF=='11':
                Noviembre+=1
            elif valF=='12':
                Diciembre+=1

        #Para evitar mostrar en los peores calificados a los productos que no han tenido compras
        #se detecta si las compras (i) son iguales a Cero (0) para luego eliminarlas de la lista F
        if i==0:
            prom=0
        
        #Toplas que asignan las veces que se compra (i) a cada producto (z), 
        #categoría (y), calif (prom), devoluciones (d)
        sumaAscendente = [i,z,y]                           
        sumaDescendente = [y,i,z]                         
        sumaE = [y,prom,i,z,d]
        sumaF = [y,prom,i,z,d]
        sumaM = [[Enero,1],[Febrero,2],[Marzo,3],[Abril,4],[Mayo,5],[Junio,6],[Julio,7],[Agosto,8],[Septiembre,9],[Octubre,10],[Noviembre,11],[Diciembre,12]]
    


    #A = [Posición, [veces_comprado, producto, Categoría]]
    #B = [Posición, [Categoría, veces_comprado, producto]]
    #E = [Posición, [Categoría, Calificación, veces_comprado, producto, devoluciones]]
    #F = [Posición, [Categoría, Calificación, veces_comprado, producto, devoluciones]]
    #G = [Posición, [Compras_mes, Mes]]

    #Inserta Topla "SUMA" a las listas A, B, C, D, E, F, G con estas en posicion de cada producto (z)
    A.insert(z, sumaAscendente)                                
    E.insert(z, sumaE)                                         
    B.insert(z, sumaDescendente)
    F.insert(z, sumaF)
    G.insert(z, sumaM)

    #Compras hechas de cada producto en posicion del producto (z)
    comprasTotales.insert(z, i)

    if prom == 0:                                             #Si no hay compras del producto, no se mostrará
            F.pop()                                           #en los peores calificados (evita mostrar 0)


#<!--  BUSQUEDAS  -->

    x=0
    i=0

    #De la lista lifestore_searches obtiene las busquedas por producto

    for row1 in lifestore_searches:

        valY = lifestore_searches[x][1]                     #Revisar el numero de busquedas de cada producto
        x+=1

        #Asigna la categoría al producto
        if valY == z:
            if z<10:
                y = 'Procesadores'
            
            elif z>9 and z<29:
                y = 'Tarjetas de video'
            
            elif z>28 and z<47:
                y = 'Tarjetas madre'
        
            elif z>46 and z<60:
                y = 'Discos duros'
            
            elif z==60 or z==61:
                y = 'Memorias USB'
            
            elif z>61 and z<74:
                y = 'Pantallas'
            
            elif z>73 and z<84:
                y = 'Bocinas'
            
            elif z>83:
                y = 'Audifonos'

            i+=1
        
        #Toplas que asignan busquedas (i) al producto (z) de categoría (y)
        sumaSearch = [i,z,y]
        sumaSearchCat = [y,i,z]

    #C = [Posición, [veces_buscado, producto, Categoría]]
    #D = [Posición, [Categoría, veces_buscado, producto]]

    C.insert(z, sumaSearch)

    D.insert(z, sumaSearchCat)
    z+=1


#<!--  PRECIOS  -->

x=0

#Ciclo para obtener el precio (valP) y stock (valS) de cada producto (x)
for row in lifestore_products:

    valP = lifestore_products[x][2]
    valS = lifestore_products[x][4]
    x+=1
    preciosTotales.insert(x,valP)
    stock.insert(x, valS)

#Multiplicar compras por precio para saber cual es el aporte de cada producto

comprasTotales.pop(0)                                         #Porque el primero valor es del producto 0 (no existe)

#Ciclo para asignar a cada producto (z) el ingreso aportado en el año
H = [[(z+1), preciosTotales[z]*comprasTotales[z], stock[z]] for z in range(len(preciosTotales))]

#Ciclo para obtener los ingresos totales en el año
I = [preciosTotales[z]*comprasTotales[z] for z in range(0,len(preciosTotales))]

#Muestra el menú hasta que el usuario seleccione la opción salir (0)

def menu():

    while True:

        print("\n<--  Menú  -->\n ")
        opcionMenu = input(" 1 - 50 Más Comprados                     | 2 - 50 Menos Comprados\n 3 - 100 Más Buscados                     | 4 - 100 Menos Buscados\n 5 - 20 Mejor Calificados                 | 6 - 20 Peor Calificados\n 7 - Total de Ingresos/Stock (Producto)   | 8 - Ventas por Mes\n 9 - Total Anual y Promedio Mensual       | 0 - Salir\n\n")
        
        #<!--  COMPRADOS  -->

        if opcionMenu=='1':
            A.sort(reverse = True)
            print("\n50 Más comprados\n \n Se compró | El producto | Categoría\n")
            print(A[:50])                                                 #Mostrar solo los primeros 50
            print()

        elif opcionMenu=='2':
            K= sorted(B, key=operator.itemgetter(0,1))
            print("\n50 Menos comprados (Por categoría)\n \n Categoría | Se compró | El producto\n")
            print(K[1:51])                                                #Mostrar solo los primeros 50
            print()

        # <!--  BUSCADOS  -->

        elif opcionMenu=='3':
            C.sort(reverse= True)
            print("\n100 Mas Buscados\n \n Se Buscó | El producto | Categoría\n")
            print(C[:100])                                                #Mostrar 100
            print()

        elif opcionMenu=='4':
            L= sorted(D, key=operator.itemgetter(0,1))
            print("\n100 Menos Buscados (Por categoría)\n \n Categoría | Se Buscó | El producto \n")
            print(L[1:101])                                               #Mostrar 100
            print()

        # <!--  RESEÑAS  -->

        elif opcionMenu=='5':
            M= sorted(E, key=operator.itemgetter(4,1,0,2), reverse= True)
            print("\n20 Mejor Calificados (Por categoría)\n \n Categoría | Calificación | Se compró | El producto | Devoluciones \n")
            print(M[:20])                                                 #Mostrar solo los primeros 20
            print()

        elif opcionMenu=='6':
            N= sorted(F, key=operator.itemgetter(4,1,0,2), reverse= False)
            print("\n20 Peor Calificados (Por categoría)\n \n Categoría | Calificación | Se compró | El producto | Devoluciones \n")
            print(N[1:21])                                                #Mostrar solo los primeros 20
            print()

        # <!--  INGRESOS  -->

        elif opcionMenu=='7':
            J= sorted(H, key=operator.itemgetter(1,2,0), reverse= False)
            print("\nIngreso por producto (En el plazo anual)\n \n Producto | Ingreso | Stock\n")
            print(J)
            print()

        elif opcionMenu=='8':
            print("\nVentas por mes (De Enero-Diciembre)\n \n Ventas | Mes \n")
            print(G[-1])
            print()

        elif opcionMenu=='9':
            print("\nTotal ingresos por venta (En el plazo anual)\n")
            print(sum(I))
            print()

            print("\nPromedio mensual (2020)\n")
            print(sum(I)/12)                                               #Total Anual/12
            print()

        elif opcionMenu=='0':
            run()

        else:
            print("\nPor favor, ingresa una opción válida\n")

#Inicio del programa y procede al menú
run()