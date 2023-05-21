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

aticulos = {
    '10000': ['TOYOTA', 'Etios Hatchback 2024', 'X 6 M/T', 'Gris Plata (1H6)', 'SEÑADO'],
    '10001': ['TOYOTA', 'Etios Hatchback 2024', 'XLS Pack 6 M/T', 'Gris Plata (1H6)','DISPONIBLE'],
    '10003': ['TOYOTA', 'Etios Sedán 2024', 'X 6 M/T', 'Blanco (040)', 'DISPONIBLE'],
    '10004': ['TOYOTA', 'Corolla 2023', '2.0 XLI CVT', 'Blanco Perlado (089)', 'DISPONIBLE'],
    '10005': ['TOYOTA', 'Corolla 2023', '2.0 XLI M/T', 'Blanco Perlado (089)', 'RESERVADO']
}

versiones = {
    'Etios Hatchback 2024': [['X 6 M/T', 4294000], ['XLS Pack 6 M/T', 5133000], ['XLS Pack 4 A/T', 5375000]],
    'Etios Sedán 2024': [['X 6 M/T', 4480000], ['XLS Pack 6 M/T', 5245000], ['XLS Pack 4 A/T', 5483000]],
    'Corolla 2023': [['2.0 XLI M/T', 6648000], ['2.0 XLI CVT', 6901000], ['2.0 XEI CVT', 6979000], ['2.0 SEG CVT', 10981000]]
}

colores = {
    'Etios Hatchback 2024': ('Gris Plata (1H6)', 'Rojo Metalizado (3R3)', 'Gris Oscuro Metalizado (1G3)'),
    'Etios Sedán 2024': ('Blanco (040)', 'Gris Oscuro Metalizado (1G3)', 'Blanco Perlado (089)'),
    'Corolla 2023': ('Gris Plata (1E7)', 'Blanco Perlado - 089', 'Negro (209)', 'Blanco (040)')
}

cliente = {
    30224556: ['Juan', 'Perez', 'Sanez Peña', 'Belgrano 1890', '3644234767', 'juanperez@hotmail.com'],
    20224556: ['Cecilia', 'Garcia', 'Resistencia', 'Blas Parera 1800', '3624535678', 'ceci1980@gmail.com'],
    39346783: ['Mariano', 'Klerl', 'Villa Angela', 'San Lorenzo 250', '3735987336', 'galo@klerl.com.ar'],
    8342876: ['Hugo', 'Curcobain', 'Charata', 'Guemes 480', '3731765299', 'compras@curcobain.com']
}

operaciones = {
    100: ['10005',  6648000, 'meli'],
    101: ['10000', 4294000, 'meli']
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
        *       1 - Vehículos               *
        *       2 - Operaciones             *
        *       3 - Caja                    *
        *       4 - Entregas                *
        *       5 - Salir                   *
        *                                   *
        *************************************
    Ingrese una opción: ''')

    os.system(limpiar)

    if menu == '1' and usuarios[usuario_logueado][3] == 'ADMIN':
        pass
    elif menu == '2' and (usuarios[usuario_logueado][3] == 'ADMIN' or usuarios[usuario_logueado][3] == 'VENTA'):
        pass
    elif menu == '3' and (usuarios[usuario_logueado][3] == 'ADMIN' or usuarios[usuario_logueado][3] == 'CAJA'):
        pass
    elif menu == '4' and (usuarios[usuario_logueado][3] == 'ADMIN' or usuarios[usuario_logueado][3] == 'ENTREGAS'):
        pass
    elif menu == '5':
        print('Ha salido del sistema Comisión3')
        time.sleep(3)
        break
    else:
        if menu == '1' or menu == '2' or menu == '3' or menu == '4':
            print(f'Tu rol de {usuarios[usuario_logueado][3]} no tiene los privilegios suficientes')
            print(f'Comunícate con el administrador { usuarios["admin"][1] } { usuarios["admin"][1] }')
            time.sleep(3)
            os.system(limpiar)
        else:
            print(f'{menu} No es una opción válida')
            time.sleep(3)
            os.system(limpiar)