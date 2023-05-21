import os
import time

##### Limpiar Pantalla ######################################

# Para Unix/Linux/MacOS/BSD
if os.name == "posix":
    limpiar = "clear"
# Para DOS/Windows
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    limpiar = "cls"
#############################################################


usuarios = {
    'admin': ['123', 'Miguel', 'Puente', 'ADMIN'],
    'meli': ['meli23', 'Meliza', 'Gonzalez', 'VENTA'],
    'juana': ['juana23', 'Juana', 'Mastaza', 'CAJA'],
    'pepe': ['pepe23', 'Pedro', 'Arklin', 'ENTREGAS']
}

articulos = {
#       {id: [ proveedor,     nombre,    marca,  stock]}
    '10000': ['3012435872', 'Martillo', 'Martin SA', 25],
    '10001': ['3012435872', 'Tornillo', 'Torni SA', 2500],
    '10002': ['3012435872', 'Tornillo 2x', 'Torni SA', 500],
    '10003': ['3098423121', 'Pintura Latex x 20 lts', 'Alba SA', 500],
    '10004': ['3098423121', 'Pintura Latex x 10 lts', 'Alba SA', 300],
    '10005': ['3098423121', 'Pintura Latex x 5 lts', 'Alba SA', 400],
    '10006': ['2714536751', 'Cal x 20kg', 'Calcina SA', 200],
    '10007': ['2714536751', 'Cemento x 20kg', 'Lomana Negra SA', 1200],
    '10008': ['2714536751', 'Cemento x 20kg', 'Minetti SA', 1000]
}

proveedores = {
    '3012435872': ['El Tornillo SRL','pedidos@eltornillosrl.com.ar', '3465367239'],
    '2714536751': ['La Construcción SA','pedidos@construccion.com.ar', '4465243775'],
    '3098423121': ['La Ferretería SA','pedidos@ferretería.com.ar', '2565536992']
}

lista_precio = {
#     {id:   [% ganancia, precio_compra, precio_venta]}
    '10000': [0.2, 450.0, 540.0],
    '10001': [0.2, 450.0, 540.0],
    '10002': [0.2, 450.0, 540.0],
    '10003': [0.2, 450.0, 540.0],
    '10004': [0.2, 450.0, 540.0],
    '10005': [0.2, 450.0, 540.0],
    '10006': [0.2, 450.0, 540.0],
    '10007': [0.2, 450.0, 540.0],
    '10008': [0.2, 450.0, 540.0]
}

cliente = {
#   { dni:    [ Nombre,  Apellido,  Localidad, dirección, telefono, email]}
    '30224556': ['Juan', 'Perez', 'Sanez Peña', 'Belgrano 1890', '3644234767', 'juanperez@hotmail.com'],
    '20224556': ['Cecilia', 'Garcia', 'Resistencia', 'Blas Parera 1800', '3624535678', 'ceci1980@gmail.com'],
    '39346783': ['Mariano', 'Klerl', 'Villa Angela', 'San Lorenzo 250', '3735987336', 'galo@klerl.com.ar'],
    '8342876': ['Hugo', 'Curcobain', 'Charata', 'Guemes 480', '3731765299', 'compras@curcobain.com']
}

operaciones = {
#   {id:    [id cliente,  [(id art, cantidad), (id art, cantidad)]]}
    50000: ['30224556', [('10000', 3), ('10001', 10)]],
    50001: ['10000', 4294000, 'meli']
}

estados = ('DISPONIBLE', 'RESERVADO', 'SEÑADO', 'PAGADO', 'ENTREGADO')

usuario_logueado = False

#############################################################
#                                                           #
#                   Pantalla Ingreso                        #
#                                                           #
#############################################################

while True:
    menu = input('''
        *************************************
        *       Sistema Comisión_3          *
        *************************************
        *                                   *
        *       1 - Ingresar                *
        *       2 - Registrarse             *
        *       3 - Salir                   *
        *                                   *
        *************************************
    Ingrese una opción: ''')

    os.system(limpiar)

    if menu == '1':
        usuario = input('Ingresa usuario: ')
        clave = input('Ingresa contraseña: ')
        if usuario in usuarios and clave == usuarios[usuario][0]:
            print(f'Bienvenido al sistema Comisión_3 {usuarios[usuario][1]} {usuarios[usuario][2]}')
            usuario_logueado = usuario
            time.sleep(3)
            os.system(limpiar)
            break
        else:
            print('usuario o contraseña incorrectos')
            time.sleep(3)
            os.system(limpiar)

    elif menu == '2':
        while True:
            usuario = input('Ingresa nombre de usuario: ')

            if usuario in usuarios:
                print('Nombre de usuario no disponible, ingresa otro')
                time.sleep(3)
                os.system(limpiar)
            else:
                break

        while True:
            os.system(limpiar)

            print(f'usuario:    {usuario}')
            clave = input('Ingresa la contraseña: ')

            if len(clave) <= 5:
                print('* La contraseña debe tener mínimo 6 caracteres')
                time.sleep(3)
                os.system(limpiar)
            else:
                break

        while True:
            os.system(limpiar)

            print(f'usuario:    {usuario}')
            print(f'contraseña: {clave}')
            nombre = input('Ingresa tu nombre: ')

            if len(nombre) < 3:
                print('* nombre debe tener mínimo 3 caracteres')
                time.sleep(3)
                os.system(limpiar)
            else:
                break

        while True:
            os.system(limpiar)

            print(f'usuario:    {usuario}')
            print(f'contraseña: {clave}')
            print(f'nombre:     {nombre}')
            apellido = input('Ingresa tu apellido: ')

            if len(apellido) < 3:
                print('* apellido debe tener mínimo 3 caracteres')
                time.sleep(3)
                os.system(limpiar)
            else:
                break

        usuarios[usuario] = [clave, nombre, apellido, 'USER']
        print(f'Usuario {usuario} registrado correctamente')

        print(f'Bienvenido al sistema Comisión_3 {usuarios[usuario][1]} {usuarios[usuario][2]}')
        usuario_logueado = usuario
        time.sleep(3)
        os.system(limpiar)
        break

    elif menu == '3':
        print('Ha salido del sistema Comisión3')
        time.sleep(3)
        break

    else:
        print(f'{menu} No es una opción válida')
        time.sleep(3)
        os.system(limpiar)




#############################################################
#                                                           #
#                   Pantalla Administración                 #
#                                                           #
#############################################################


while usuario_logueado:
    menu = input('''
        *************************************
        *       Sistema Comisión_3          *
        *************************************
        *                                   *
        *       1 - Artículos               *
        *       2 - Ventas                  *
        *       3 - Caja                    *
        *       4 - Entregas                *
        *       5 - Salir                   *
        *                                   *
        *************************************
    Ingrese una opción: ''')

    os.system(limpiar)

    if menu == '1' and usuarios[usuario_logueado][3] == 'ADMIN':

        while True:

            menu_articulo = input('''
                *************************************
                *       Artículos                   *
                *************************************
                *                                   *
                *       1 - Agregar                 *
                *       2 - Modificar               *
                *       3 - Eliminar                *
                *       4 - Lista Precios           *
                *       5 - Salir                   *
                *                                   *
                *************************************
            Ingrese una opción: ''')
            os.system(limpiar)

            if menu_articulo == '1':
                pass
            elif menu_articulo == '2':
                pass
            elif menu_articulo == '3':
                pass
            elif menu_articulo == '4':
                while True:

                    print('Lista de Precios\n')
                    print('id       Ganancia        Precio Compra       Precio Venta        Nombre Artículo\n')
                    for precio in lista_precio:
                        print(F'{precio}      {lista_precio[precio][0] * 100}          ${lista_precio[precio][1]}               ${lista_precio[precio][2]}             {articulos[precio][1]} \n')

                    menu_lista_precio = input('''
                        *************************************
                        *       Lista de precios            *
                        *************************************
                        *                                   *
                        *       1 - Ver lista               *
                        *       2 - Modificar               *
                        *       3 - Eliminar                *
                        *       4 - Salir                   *
                        *                                   *
                        *************************************
                    Ingrese una opción: ''')
                    #       {id: [ proveedor,     nombre,    marca,  stock]} articulo
                    #       {id:   [% ganancia, precio_compra, precio_venta]} lista:precio
                    os.system(limpiar)
                    if menu_lista_precio == '1':
                        print('Lista de Precios\n')
                        print('id       Ganancia        Precio Compra       Precio Venta        Nombre Artículo\n')
                        for precio in lista_precio:
                            print(F'{precio}      {lista_precio[precio][0] * 100}          ${lista_precio[precio][1]}               ${lista_precio[precio][2]}             {articulos[precio][1]} \n')
                        input('Presione ENTER para volver')
                        os.system(limpiar)
                    elif menu_lista_precio == '2':

                        while True:
                            print('Lista de Precios\n')
                            print('id       Ganancia        Precio Compra       Precio Venta        Nombre Artículo\n')
                            for precio in lista_precio:
                                print(F'{precio}      {lista_precio[precio][0] * 100}          ${lista_precio[precio][1]}               ${lista_precio[precio][2]}             {articulos[precio][1]} \n')

                            articulo = input('Ingresa código artículo o N para salir: ')
                            
                            if articulo == 'N':
                                os.system(limpiar)
                                break
                            elif articulo in articulos:
                                ganancia = float(input('Ingresa "%" de ganancia por ejemplo 20 o 30: '))
                                precio_compra = float(input('ingresa precio compra: '))

                                lista_precio[articulo][0] = ganancia / 100
                                lista_precio[articulo][1] = precio_compra
                                lista_precio[articulo][2] = precio_compra + ( precio_compra * (ganancia / 100))

                                print('\n Artículo agregado exitosamente')
                                time.sleep(3)
                            else:
                                print('El artículo no existe')
                                time.sleep(3)
                            
                            os.system(limpiar)
                    elif menu_lista_precio == '3':
                        while True:
                            print('Lista de Precios\n')
                            print('id       Ganancia        Precio Compra       Precio Venta        Nombre Artículo\n')
                            for precio in lista_precio:
                                print(F'{precio}      {lista_precio[precio][0] * 100}          ${lista_precio[precio][1]}               ${lista_precio[precio][2]}             {articulos[precio][1]} \n')

                            articulo = input('Ingrese el código del artículo a eliminar o N para salir: ')
                            if articulo == 'N':
                                os.system(limpiar)
                                break
                            if articulo in lista_precio:
                                lista_precio.pop(articulo)
                                print('Artículo elimando exitosamente')
                                time.sleep(3)
                            else:
                                print('Artículo no existe')
                                time.sleep(3)

                            os.system(limpiar)

            elif menu_articulo == '5':
                pass
            else:
                print(f'{menu_articulo} No es una opción válida')
                time.sleep(3)
                os.system(limpiar)    

    elif menu == '2' and (usuarios[usuario_logueado][3] == 'ADMIN' or usuarios[usuario_logueado][3] == 'VENTA'):
        pass
    elif menu == '3' and (usuarios[usuario_logueado][3] == 'ADMIN' or usuarios[usuario_logueado][3] == 'CAJA'):
        pass
    elif menu == '4' and (usuarios[usuario_logueado][3] == 'ADMIN' or usuarios[usuario_logueado][3] == 'ENTREGA'):
        pass
    elif menu == '5':
        print('Ha salido del sistema Comisión3')
        time.sleep(3)
        break
    else:
        if menu == '1' or menu == '2' or menu == '3' or menu == '4':
            print(f'Tu rol de {usuarios[usuario_logueado][3]} no tiene los privilegios suficientes')
            print(f'Comunícate con el administrador { usuarios["admin"][1] } { usuarios["admin"][2] } pa modificar artículos')
            time.sleep(3)
            os.system(limpiar)
        else:
            print(f'{menu} No es una opción válida')
            time.sleep(3)
            os.system(limpiar)