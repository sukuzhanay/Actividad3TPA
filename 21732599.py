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
#-------------------------------------------------------------------------

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
#     elif opcion == "C" or opcion =="c":
#         print("\n------------------------------EJERCICIO C---------------------------------------------")
#         m=[[1,2],[3,4]]
#         print("Matriz: ",m)
#         mtx = CtrasponerDC(m, 0, len(m)-1, 0, len(m)-1)
#         print("Matriz traspuesta: ",mtx)
#         print("---------------------------------------------------------------------------------------\n")
#         menu()
#     elif opcion == "D" or opcion =="d":
#         print("\n------------------------------EJERCICIO D---------------------------------------------")
#         array = DgenerarArray()
#         print(array)
#         global listaInicial   
#         listaInicial = array
#         Ddivide(array, 0, len(array)-1)  
#     else:
#         print("SALIENDO DEL PROGRAMA...")
#         sys.exit(-1)

#ejecucion
login()
