 import sys
 #variables del correo y la contrasena del login
 #es obligatoria  
correo = "actividad@gmail.com"
expediente = 21732599
count = 0

#-------------------------------CREAR ARBOL EJEMPLO-------------------------------------------

#clase Node para crear nodos en el arbol
class Node:
    def __init__ (self,data):
        self.derecha=None
        self.izquierda=None
        self.data = data
#funcion agregar para agregar nodos a la derecha o izquierda    
def agregar(root,node):
    #caso base
    if root is None:
        root = node
    else:
        #si el dato es mayor que el de la raiz se coloca a la derecha
        if root.data < node.data:
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
          "A: Ejercicio A\n"
          "B: Ejercicio B\n"
          "C: Ejercicio C\n"
          "D: Ejercicio D\n"
          "S: Salir\n")
    opcion = input("Elija una opcion:")
#     
    if opcion == "A" or opcion=="a":
#         print("\n------------------------------EJERCICIO A---------------------------------------------")
#         lista1 = [1,2,3,7,8]
#         lista2 = [0,4,6,9]
#         listaV = AjuntarYOrdenar(lista1, lista2)
#         AobtenerMediana(listaV)
#         print("---------------------------------------------------------------------------------------\n")
        menu()
    elif opcion == "B" or opcion =="b":
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
#     elif opcion == "D" or opcion =="d":
#         print("\n------------------------------EJERCICIO D---------------------------------------------")
#         menu() 
    else:
        print("SALIENDO DEL PROGRAMA...")
        sys.exit(-1)

#ejecucion
login()
