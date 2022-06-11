#menu
#Modulo para crear las funciones de impresion por pantalla para el usuario
import pandas as pd
from os import system as dossystem  #añadida para limpiar consola
dossystem('mode con: cols=120 lines=1500')

Version = "SNApp V1.0"
#Funcion para limpiar la pantalla cada vez que se abre un menu o un informe
def limpiapantalla():
    try:
        dossystem("cls")
    except :
        pass

#Funcion para imprimir en pantalla el Menu principal  (0,)
def menuInicial():
    limpiapantalla()
    opciones = 5
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Menu Principal                             |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Agregar información                                   |")
    print("| 2. Consultar información                                 |")
    print("| 3. Modificar información                                 |")
    print("| 4. Eliminar información                                  |")
    print("| 99. Salir de la aplicación                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir en pantalla el Menu Agregar (0,1)
def menuAgregar():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Agregar Información                        |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Agregar Materias                                      |")
    print("| 2. Agregar Profesores                                    |")
    print("| 3. Agregar Grupos                                        |")
    print("| 4. Agregar Estudiantes                                   |")
    print("| 5. Agregar Notas                                         |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir en pantalla el Menu Consultar (0,2)
def menuConsultar():
    limpiapantalla()
    opciones = 7
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Consultar Información                      |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Consultar Materias                                    |")
    print("| 2. Consultar Profesores                                  |")
    print("| 3. Consultar Grupos                                      |")
    print("| 4. Consultar Estudiantes                                 |")
    print("| 5. Consultar Notas                                       |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir en pantalla el subMenu Consultar Materias (0,2,1)
def menuConsultarMaterias():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Consultar Materias                         |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de materias                                   |")
    print("| 2. Materias por ciclo                                    |")
    print("| 3. Profesores por materia                                |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir Lista de Materias (0,2,1,1)
def InformeListadoMaterias(tblMaterias ):
    tblMaterias = tblMaterias.set_index('IDMateria')
    limpiapantalla()
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------- ")
    print("|                   LISTADO MATERIAS                      |")
    print(" --------------------------------------------------------- ")
    print(tblMaterias,"\n")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para imprimir Lista de Materias (0,2,1,2)
def InformeMateriasXCiclo(informe, tblMaterias):
    limpiapantalla()
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------- ")
    print("|             LISTADO MATERIAS POR CICLO                  |")
    print(" --------------------------------------------------------- ")
    print(informe(tblMaterias),"\n")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para imprimir Lista de Profesores X Materia (0,2,1,3)
def InformeProfesoresXMateria(informe, tblProfesores, tblMaterias ):
    limpiapantalla()
    listado = informe(tblProfesores,tblMaterias).sort_values(by = ['Materia','Nombre'])
    listado = listado.reset_index()
    listado = listado.set_index(['IDMateria','Materia','Nombre'])
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|               LISTADO DE PROFESORES POR MATERIA                     |")
    print(" --------------------------------------------------------------------- ")
    print(listado,"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones

 #Funcion para imprimir en pantalla el subMenu Consultar Profesores (0,2,2)
def menuConsultarProfesores():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Consultar Profesores                       |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de Profesores                                 |")
    print("| 2. Grupos activos por profesor                           |")
    print("| 3. Materias por profesor                                 |")
    print("| 4. Estudiantes por profesor                              |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir Listado de Profesores (0,2,2,1)
def InformeListadoProfesores(informe, tblProfesores, tblMaterias ):
    limpiapantalla()
    listado = informe(tblProfesores,tblMaterias).sort_values(by = ['Nombre','Materia'])
    listado = listado.reset_index()
    listado = listado.set_index(['IDProfesor','Nombre','Materia'])
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|               LISTADO DE PROFESORES POR MATERIA                     |")
    print(" --------------------------------------------------------------------- ")
    print(listado,"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones




 #Funcion para imprimir en pantalla el subMenu Consultar Grupos (0,2,3)
def menuConsultarGrupos():
    limpiapantalla()
    opciones = 4
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                   Consultar Grupos                       |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de grupos                                     |")
    print("| 2. Listado detallado de grupos activos                   |")
    print("| 3. Estudiantes por grupo                                 |")
    print("| 4. Profesores por grupo                                  |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

 #Funcion para imprimir en pantalla el subMenu Consultar Estudiantes (0,2,4)
def menuConsultarEstudiantes():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                Consultar Estudiantes                     |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de Estudantes                                 |")
    print("| 2. Listado de estudiantes por grupo                      |")
    print("| 3. Listado de notas por estudiante                       |")
    print("| 4. Listado de promedios por estudiante                   |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir Lista de Estudiantes por Grupo (0,2,4,2)
def InformeEstudiantesXGrupo(informe, tblEstudiantes, tblGrupos ):
    limpiapantalla()
    listado = informe(tblEstudiantes,tblGrupos)
    listado = listado.reset_index()
    listado = listado.sort_values(by = ['IDGrupo','Apellidos','Nombres'])
    listado = listado.set_index(['IDGrupo','Apellidos','Nombres'])
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|               LISTADO DE ESTUDIANTES POR GRUPO                      |")
    print(" --------------------------------------------------------------------- ")
    print(listado["IDEstudiante"],"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones


 #Funcion para imprimir en pantalla el subMenu Consultar Notas (0,2,5)
def menuConsultarNotas():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                   Consultar Notas                        |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Matriz general de notas                               |")
    print("| 2. Listado de notas por grupo                            |")
    print("| 3. Listado de notas por estudiante                       |")
    print("| 4. Listado de promedios ciclo por estudiante             |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones


#Funcion para imprimir en pantalla el Menu Modificar (0,3)
def menuModificar():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Modificar Información                      |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Modificar Materias                                    |")
    print("| 2. Modificar Profesores                                  |")
    print("| 3. Modificar Grupos                                      |")
    print("| 4. Modificar Estudiantes                                 |")
    print("| 5. Modificar Notas                                       |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

 #Funcion para imprimir en pantalla el Menu Eliminar (0,4)
def menuEliminar():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Eliminar Información                       |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Eliminar Materias                                     |")
    print("| 2. Eliminar Profesores                                   |")
    print("| 3. Eliminar Grupos                                       |")
    print("| 4. Eliminar Estudiantes                                  |")
    print("| 5. Eliminar Notas                                        |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones
    
#Funcion para imprimir en pantalla que fallo el cargue de informacion
def menuFallaCarga():
    print(" ---------------------------------------------------------- ")
    print("|          !Error al cargar la informacion!                |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1.  Oprima 1 para cerrar la aplicacion                   |")
    print("|     Puede revisar los archivos con extension .csv y      |")
    print("|     verificar si hace falta alguno o alguno esta dañado  |")
    print("|                                                          |")
    print("| 99. oprima 99 si desea crear una base de datos nueva     |")
    print("|     tenga en cuenta que perdera toda la informacion      |")
    print("|     que contengan todos los archivos                     |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")


#Se crea un diccionario con la ruta y lista de las funciones de los menus para ser llamadas automaticamente
DicMenu = {(0,)   :     menuInicial,
           (0,1)  :     menuAgregar,     #0 es el menu principal y 1 es la opcion 1 Agregar del menu principal por tanto la llave de esta funcion es (0,1)
           (0,2)  :     menuConsultar,
           (0,2,1) :    menuConsultarMaterias,
          #(0,2,1,1):   (ic.InformeListadoMaterias,tblMaterias),
          #(0,2,1,2):   (ic.InformeMateriasXCiclo,crud.consultaMateriasXCiclo,tblMaterias),
          #(0,2,1,3):   (ic.InformeProfesoresXMateria, crud.consultaMateriasXProfesor)
           (0,2,2) :    menuConsultarProfesores,
          #(0,2,2,1) :  (ic.InformeListadoProfesores, crud.consultaMateriasXProfesor, tblProfesores, tblMaterias ),
           (0,2,3) :    menuConsultarGrupos,
           (0,2,4) :    menuConsultarEstudiantes,
          #(0,2,4,2):   (ic.InformeEstudiantesXGrupo, crud.consultaEstudiantesXGrupo ,tblEstudiantes,tblGrupos),
           (0,2,5) :    menuConsultarNotas,
           (0,3)   :    menuModificar,
           (0,4)   :    menuEliminar,
           
    }
