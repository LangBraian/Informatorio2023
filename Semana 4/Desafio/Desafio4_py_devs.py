##### Importaciones #########################################
from time import sleep
from datetime import date
from copy import deepcopy
from os import name, system
#############################################################


##### Limpiar Pantalla ######################################
if name == "posix":
    limpiar = "clear"
elif name == "ce" or name == "nt" or name == "dos":
    limpiar = "cls"
#############################################################


##### Variables a usar en ciclos ############################
menu_inicial = '''
        ╔════════════════════════════════════════════════════╗
        ║                                                    ║
        ║       P Y T H O N I A N   R E A L   S T A T E      ║
        ║                                                    ║
        ║                   ¡ Bienvenido !                   ║
        ║                                                    ║
        ║          Operaciones:                              ║
        ║          1. Editar información de un inmueble      ║
        ║          2. Editar el estado de un inmueble        ║
        ║          3. Agregar un nuevo inmueble              ║
        ║          4. Eliminar un inmueble                   ║
        ║          5. Seleccionar inmuebles por precio       ║
        ║          6. Listar inmuebles existentes            ║
        ║          EXIT ->                                   ║
        ║                                                    ║
        ╚════════════════════════════════════════════════════╝
        '''

# Lista de inmuebles:
listado_inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]
# Lista de opciones del menú principal:
''' Si se agregan opciones al menú deben agregarse números a esta lista '''
opciones = [1,2,3,4,5,6]

# Año actual:
''' Se determina el año actual para poder calcular la antigüedad de un inmueble '''
current_year = int(date.today().strftime('%Y'))

# Reglas para edición o agregado de inmuebles:

''' Este texto se muestra al momento de efectuar una operación de edición
    o agregado de la lista de inmuebles.
'''
reglas_inmuebles =''' Reglas que deben cumplirse al trabajar con inmuebles:
    * Las zonas sólo pueden ser: A, B o C.
    * El estado sólo puede ser: Disponible, Reservado o Vendido.
    * El garaje puede ser: Si o No.
    * No se opera con inmuebles:
      * Anteriores al año 2000.
      * Menores de 60 metros cuadrados.
      * Menores de 2 habitaciones.
'''

''' Estas son reglas usadas para automatizar la verificación de datos al editar
    o agregar un inmueble de la lista.
'''
reglas = {
    'zonas': ['A', 'B', 'C'],
    'estado': ['Disponible', 'Reservado', 'Vendido'],
    'garaje': ['Si', 'No'],
    'valores_minimo': {
        'año': 2000,
        'metros': 60,
        'habitaciones': 2
    }
}

''' Estas son reglas usadas para automatizar el cálculo del precio y poder devolver
    una lista con aquellos inmuebles que cumplen con dichas reglas.
'''
reglas_precio = {
    'metros': 100,
    'habitaciones': 500,
    'estado': ['Disponible', 'Reservado'],
    'garaje': 1500,
    'zonas': {
        'A': 1,
        'B': 1.5,
        'C': 2
    }
}

#############################################################


##### Definimos funciones ###################################

''' ------- Funciones para servicios repetitivos -------- '''
def limpiar_pantalla():
    ''' Limpiamos pantalla '''
    system(limpiar)

def presentacion():
    ''' Se da la bienvenida y se muestra el menú de opciones disponibles '''
    limpiar_pantalla()
    print(menu_inicial, sep=' ')

def mensaje_error1():
    ''' Se emite un mensaje al no ingresar una opción correcta '''
    print(f'\nUsted no ingresó una opción válida. Intente nuevamente.')
    sleep(2)
    return

def mensaje_error2():
    ''' Se emite un mensaje al no ingresar datos correctamente '''
    print('El dato ingresado no respeta las reglas señaladas. Intente nuevamente.')
    sleep(2)
    return

def listar_inmueble(listado_de_inmuebles=listado_inmuebles):
    # limpiar_pantalla()
    print('\nListado de inmuebles:\n')
    print('Orden de lista')
    no_matches = 0
    for index, each in enumerate(listado_de_inmuebles):
      if len(each) != 0:
        print(f'   ( {index+1} )----> {each}')
        no_matches += 1
      else:
          continue
    if no_matches == 0:
        print('----> No hay inmuebles que cumplan con lo solicitado <----')
    input('\nPresione << ENTER >> para continuar.')

def get_orden_lista(len_listado_inmuebles):
    ''' Se verifica en cada ingreso que el dato proporcionado sea un número de orden
        válido según la longitud de la lista de inmuebles ingresada.
        Se permite salir de esta opción con la palabra " EXIT ".
    '''
    limpiar_pantalla()
    listar_inmueble()
    print('\nA continuación ingrese el dato solicitado. Si desea salir escriba EXIT.')
    
    while True:
        orden_de_lista = input('Orden de lista: ').lower()

        if orden_de_lista == 'exit': break
        
        if orden_de_lista.isdigit():
            orden_de_lista = int(orden_de_lista) - 1
            if orden_de_lista <= (len_listado_inmuebles - 1):
                break
            else:
                mensaje_error1()
                continue
        else:
            mensaje_error1()
            continue

    return orden_de_lista

def get_nuevo_estado_inmueble(orden_lista):
    ''' Se verifica en cada ingreso que el dato proporcionado sea un estado
        válido según las reglas establecidas para el ESTADO.
        Se permite salir de esta opción con la palabra " EXIT ".
    '''
    str_estados = ', '.join(reglas["estado"])
    print(f'\nUSTED ESTÁ POR EDITAR EL ESTADO DEL INMUEBLE DE ORDEN "{orden_lista + 1}".')
    print('\nA continuación ingrese el dato solicitado. Si desea salir escriba EXIT.')
    print(f'(Los únicos ESTADOS aceptados son: {str_estados})')
    
    while True:
        new_estado = input('Nuevo estado: ').lower()

        if new_estado == 'exit': break
        
        new_estado = new_estado.capitalize()
        if new_estado in reglas['estado']:
            break
        else:
            mensaje_error1()
            continue

    return new_estado

def get_data_inmueble(orden_lista=None, isEditing=None):
    ''' Asignamos a un variable características del inmueble a editar '''
    new_inmueble = {'año': None, 'metros': None, 'habitaciones': None, 'garaje': None, 'zona': None, 'estado': None}
    indexes_new_inmueble = 0  #comenzamos a pedir datos en el orden ' 0 '

    ''' Comenzamos a solicitar los datos que el usuario desea actualizar/editar de un inmueble en particular
        verificando que sean correctos o decida salirse con la palabra " EXIT "
    '''
    # limpiar_pantalla()
    if isEditing:
        # listar_inmueble()
        print(f'\nUSTED ESTÁ POR EDITAR LOS DATOS DEL INMUEBLE DE ORDEN "{orden_lista + 1}".')
        print('\n',reglas_inmuebles, sep=' ')
        print('A continuación ingrese los datos solicitados RESPETANDO las reglas indicadas.')
        print('Si no desea EDITAR un dato existente ingrese NONE.')
        print('Si desea salir en cualquier momento escriba EXIT.\n')
    else:
        limpiar_pantalla()
        print('\nUSTED SE ENCUENTRA INGRESANDO DATOS DE UN NUEVO INMUEBLE QUE SE AGREGARÁ A LA LISTA.')
        print('\n',reglas_inmuebles, sep=' ')
        print('A continuación ingrese los datos solicitados RESPETANDO las reglas indicadas.')
        print('Si desea salir en cualquier momento escriba EXIT.\n')
    
    while indexes_new_inmueble < len(new_inmueble):
        atributo = list(new_inmueble.keys())[indexes_new_inmueble]
        dato = input(f'{atributo.capitalize()}: ').capitalize()
        
        if dato.lower() == 'exit':
            dato = dato.lower()
            break
        
        if atributo == 'año' and dato.isdigit():
            if reglas['valores_minimo']['año'] <= int(dato) <= current_year:
                new_inmueble[atributo] = int(dato)
                indexes_new_inmueble += 1
            else:
                mensaje_error2()
                continue
        elif atributo == 'metros' and  dato.isdigit():
            if int(dato) >= reglas['valores_minimo']['metros']:
                new_inmueble[atributo] = int(dato)
                indexes_new_inmueble += 1
            else:
                mensaje_error2()
                continue
        elif atributo == 'habitaciones' and dato.isdigit():
            if int(dato) >= reglas['valores_minimo']['habitaciones']:
                new_inmueble[atributo] = int(dato)
                indexes_new_inmueble += 1
            else:
                mensaje_error2()
                continue
        elif atributo == 'garaje' and dato in reglas['garaje']:
            new_inmueble[atributo] = True if dato == reglas['garaje'][0] else False
            indexes_new_inmueble += 1
        elif atributo == 'zona' and dato in reglas['zonas']:
            new_inmueble[atributo] = dato
            indexes_new_inmueble += 1
        elif atributo == 'estado' and dato in reglas['estado']:
            new_inmueble[atributo] = dato
            indexes_new_inmueble += 1
        elif isEditing and dato.lower() == 'none':
            indexes_new_inmueble += 1
        else:
            mensaje_error2()
            continue

    return dato if dato=='exit' else new_inmueble

def get_presupuesto():
    ''' Se verifica que se ingrese un precio (un número entero o con decimales).
        Se permite salir de esta opción con la palabra " EXIT ".
    '''
    print('\nA continuación ingrese el dato solicitado. Si desea salir escriba EXIT.')
    print('(Sólo se aceptan números enteros o con decimales)')
    
    while True:
        new_presupuesto = input('Ingrese el monto del presupuesto: ').lower()

        if new_presupuesto == 'exit': break
        
        is_number = (new_presupuesto.split('.')[0].isdigit() and  new_presupuesto.split('.')[1].isdigit()) if '.' in new_presupuesto else False

        if new_presupuesto.isdigit() or is_number:
            new_presupuesto = float(new_presupuesto)
            break
        else:
            mensaje_error1()
            continue

    return new_presupuesto
''' ----------------------------------------------------- '''


''' --------------- Funciones principales --------------- '''
def editar_inmueble(orden_de_lista, data_inmueble, listado_de_inmuebles):
    ''' Ingresados los datos correctos EDITAMOS tantos atributos del inmueble como sean necesarios '''
    for each in listado_de_inmuebles[orden_de_lista]:
        if data_inmueble[each] != None:
            listado_de_inmuebles[orden_de_lista][each] = data_inmueble[each]
        else:
            continue
    print('\nLos datos han sido editados correctamente.')
    sleep(3)


def editar_estado_inmueble(orden_de_lista, data_inmueble, listado_de_inmuebles):
    ''' Ingresados los datos correctos EDITAMOS tantos atributos del inmueble como sean necesarios '''
    listado_de_inmuebles[orden_de_lista]['estado'] = data_inmueble
    print('\nEL estado ha sido editado correctamente.')
    sleep(3)


def agregar_inmueble(data_inmueble, listado_de_inmuebles):
    ''' Ingresados los datos correctos AGREGAMOS el inmueble a la lista general '''
    listado_de_inmuebles.append(data_inmueble)
    print('\nLos datos han sido agregados correctamente.')
    sleep(3)


def eliminar_inmueble(orden_de_lista, listado_de_inmuebles):
    ''' Eliminamos un inmueble a la vez, según el orden de lista ingresado. '''
    listado_de_inmuebles.pop(orden_de_lista)
    print('El inmueble fue eliminado correctamente.')
    sleep(3)


def seleccionar_inmueble_por_precio(presupuesto, listado_de_inmuebles):
    ''' Reglas de precio
        * Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
        * Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
        * Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2
    '''
    listado_copia = deepcopy(listado_de_inmuebles)
    inmuebles_con_precio = []
    
    for each in listado_copia:
        precio_basico = each['metros'] * reglas_precio['metros'] + each['habitaciones'] * reglas_precio['habitaciones'] + each['garaje'] * reglas_precio['garaje']
        antiguedad = current_year - each['año']
        precio_antiguedad = precio_basico * (1 - (antiguedad / 100)) * reglas_precio['zonas'][each['zona']]

        if presupuesto >= precio_antiguedad and each['estado'] in reglas_precio['estado']:
            each['precio'] = precio_antiguedad
            inmuebles_con_precio.append(each)
        else:
            empty = {}
            inmuebles_con_precio.append(empty)

    return inmuebles_con_precio

#############################################################


##### Inicio del programa ###################################

while True:
    presentacion()
    seleccion = input('Ingrese una opción: ').lower()
    if not seleccion.isdigit():
        if seleccion == 'exit':
            limpiar_pantalla()
            break
        else:
            mensaje_error1()
            continue
    elif int(seleccion) not in opciones:
        mensaje_error1()
        continue
    else:
        if seleccion == '1':
            # listado_inmuebles es una variable que contiene todos los inmuebles
            orden = get_orden_lista(len(listado_inmuebles))
            if orden == 'exit': continue
            data = get_data_inmueble(orden_lista=orden, isEditing=True)
            if data == 'exit':
                continue
            else:
                editar_inmueble(orden, data, listado_inmuebles)
        elif seleccion == '2':
            # listado_inmuebles es una variable que contiene todos los inmuebles
            orden = get_orden_lista(len(listado_inmuebles))
            if orden == 'exit': continue
            data = get_nuevo_estado_inmueble(orden)
            if data == 'exit':
                continue
            else:
                editar_estado_inmueble(orden, data, listado_inmuebles)
        elif seleccion == '3':
            # listado_inmuebles es una variable que contiene todos los inmuebles
            data = get_data_inmueble(orden_lista=None,isEditing=False)
            if data == 'exit':
                continue
            else:
                agregar_inmueble(data, listado_inmuebles)
        elif seleccion == '4':
            # listado_inmuebles es una variable que contiene todos los inmuebles
            orden = get_orden_lista(len(listado_inmuebles))
            if orden == 'exit':
                continue
            else:
                eliminar_inmueble(orden, listado_inmuebles)
        elif seleccion == '5':
            presupuesto= get_presupuesto()
            if presupuesto == 'exit':
                continue
            else:
                seleccion = seleccionar_inmueble_por_precio(presupuesto, listado_inmuebles)
                listar_inmueble(seleccion)
        else:
            listar_inmueble(listado_inmuebles)

#############################################################