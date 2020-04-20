import sys
 #variables del correo y la contrasena del login
 #es obligatoria  
correo = "actividad@gmail.com"
expediente = 21732599
count = 0

#-------------------------------CREAR ARBOL EJEMPLO B y C-------------------------------------------

#clase Node para crear nodos en el arbol
class Node:
    def __init__ (self,val):
        self.derecha=None
        self.izquierda=None
        self.val = val
#funcion agregar para agregar nodos a la derecha o izquierda    
def agregar(root,node):
    #caso base
    if root is None:
        root = node
    else:
        #si el dato es mayor que el de la raiz se coloca a la derecha
        if root.val < node.val:
            if root.derecha is None:
                root.derecha = node
            else:
                agregar(root.derecha, node)
        else:
            #si el dato es menor que el de la raiz se coloca a la izquierda
            if root.izquierda is None:
                root.izquierda = node
            else:
                agregar(root.izquierda, node)
#ejecucion
root = Node(20)
agregar(root, Node(12))
agregar(root, Node(10))
agregar(root, Node(32))
agregar(root, Node(17))
agregar(root, Node(24))
agregar(root, Node(40))

#------------------------------------------------------------------------------------------

#---------------------------------APARTADO B-----------------------------------------------

#vamos a recorrer el arbol inorder e iremos contando la cantidad de 
#elementos que lee la funcion para obtener la cantidad de nodos
#que tiene el arbol  
def inorder(root):
    #empezamos por la raiz y comprobamos que hay mas elmentos
    if root is not None:
        #vamos al nodo de la izquierda
        inorder(root.izquierda)
        #print(root.data)
        global count 
        count+=1
        #recorrido por la derecha
        inorder(root.derecha)
#------------------------------------------------------------------------------------

#-----------------------------------APARTADO C--------------------------------------

#funcion que calcula la altura del arbol (contando el nivel inferior como 0)
def altura(root):
    #si el arbol esta vacio devuelve -1
    if root is None:
        return -1
    #obtenemos el valor maximo de las alturas del lado izquierdo y el
    #lado derecho y le sumamos uno de la altura del nodo raiz
    else:
        return (1+max(altura(root.izquierda),altura(root.derecha)))
#------------------------------------------------------------------------------------

#-------------------------------------APARTADO D-------------------------------------

#clase Node para crear nodos en el arbol
class NodoLetras:
    def __init__ (self,data,val):
        self.derecha=None
        self.izquierda=None
        self.val = val
        self.data = data
 

#funcion para saber si el nodo tiene dos hijos, solo uno derecho o izquierdo
# o si no tienen ningujo(hoja)
def esPadre(root):
    if root.derecha is not None:
        padre= "derecha"
        if root.izquierda is not None:
            padre = "doble"
    else:
        if root.izquierda is not None:
            padre = "izquierda"
        else:
            padre = "hoja"
    return padre

#varaible para saber si estamos en la raiz del arbol        
casoInicial = 0
#funcion que recorre el camino dependiendo de los hijos que tenga el nodo
def camino(root,array):
    global casoInicial 
    if esPadre(root) == "doble":
        if casoInicial == 0:
            #agrego el nodo raiz (en el caso ejemplo es la letra B)
            array.append(root.data)
            casoInicial = 1
        #si es doble, tiene dos hijos asique recorre el camino de la derecha y el de la izquierda
        imprimirDerecha(array,root)
        imprimirIzquierda(array,root)
    elif esPadre(root) == "derecha":
        imprimirDerecha(array, root)
    elif esPadre(root) == "izquierda":
        imprimirIzquierda(array, root)
    #cuando el nodo es hoja ya hemos llegado al final del recorrido por lo tanto imprimimos
    #el array con las letras obtenidas 
    elif esPadre(root) == "hoja":
        #join sirve para convertir el array en string 
        print("palabra encontrada:","".join(array))
        
#funcion que crea una copia del array que nos pasan por parametros y luego agrega el valor de 
#la derecha y continua con la funcion camino por el nodo derecho 
def imprimirDerecha(array,raiz):
    arrayD=[]
    for i in range (0,len(array)):
        arrayD.append(array[i])
    arrayD.append(raiz.derecha.data)
    camino(raiz.derecha,arrayD)

#funcion que crea una copia del array que nos pasan por parametros y luego agrega el valor de 
#la izquierda y continua con la funcion camino por el nodo izquierdo 
def imprimirIzquierda(array,raiz):
    arrayI=[]
    for i in range (0,len(array)):
        arrayI.append(array[i])
    arrayI.append(raiz.izquierda.data)
    camino(raiz.izquierda,arrayI)
    

#--------------------------------------------------------------------------------------------------        


def login():
   #se pide el correo
    email = input("Ingrese su email de la uem:")
    correo = email
    contrasena = (input("Ingrese la contrasena (numero de expediente):"))
    #la contrasena tiene que ser 21732599 obligatoriamente
    icontrasena = int(contrasena)
    if(icontrasena != expediente):
        print("No autorizado\nSALIENDO DEL PROGRAMA...")
    else: menu()
           
        
#Funcion para imprimir el menu y elegir opcion
def menu():
    print("\n******************** UNIVERSIDAD EUROPEA DE MADRID *************************\n"
         + ( "Escuela de Ingenieria Arquitectura y Diseno\n\n"))

    print("*****************MENU**********************\n"
          "B: Ejercicio B\n"
          "C: Ejercicio C\n"
          "D: Ejercicio D\n"
          "S: Salir\n")
    opcion = input("Elija una opcion:")

    if opcion == "B" or opcion =="b":
        print("\n------------------------------EJERCICIO B---------------------------------------------")
        inorder(root)
        print("El numero de elementos del arbol es" , count)
        print("---------------------------------------------------------------------------------------\n")
        menu()
    elif opcion == "C" or opcion =="c":
        print("\n------------------------------EJERCICIO C---------------------------------------------")
        alt = altura(root)
        #como la funcion altura devuelve la profundidad contando que el nivel 
        #inferior es 0, le sumamos uno para que el nivel inferior sea 1
        alt+=1
        print("La altura del arbol es" , alt)
        print("---------------------------------------------------------------------------------------\n")
        menu()
    elif opcion == "D" or opcion =="d":
            #crear el arbol de letras
        raiz = NodoLetras("B",20)
        agregar(raiz, NodoLetras("U",8))
        agregar(raiz, NodoLetras("E",7))
        agregar(raiz, NodoLetras("N",4))
        agregar(raiz, NodoLetras("O",3))
        agregar(raiz, NodoLetras("A",5))
        agregar(raiz, NodoLetras("S",6))
        agregar(raiz, NodoLetras("R",9))
        agregar(raiz, NodoLetras("R",11))
        agregar(raiz, NodoLetras("A",10))
        agregar(raiz, NodoLetras("O",12))
        agregar(raiz, NodoLetras("S",13))
        agregar(raiz, NodoLetras("I",23))
        agregar(raiz, NodoLetras("E",22))
        agregar(raiz, NodoLetras("N",21))
        agregar(raiz, NodoLetras("L",27))
        agregar(raiz, NodoLetras("B",26))
        agregar(raiz, NodoLetras("A",25))
        agregar(raiz, NodoLetras("O",24))
        print("\n------------------------------EJERCICIO D---------------------------------------------")
        array = []
        camino(raiz,array)
        print("---------------------------------------------------------------------------------------\n")
        menu() 
    else:
        print("SALIENDO DEL PROGRAMA...")
        sys.exit(-1)

#ejecucion
login()
