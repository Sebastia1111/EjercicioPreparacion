#-----------------------------------DICCIONARIOS-----------------------------------
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['LENOVO', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['ASUS', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['ASUS', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['LENOVO', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['LENOVO', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['DELL', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}
precios = {
    '8475HD': 300000,
    '2175HD': 200000,
    'JjfFHD': 600000,
    'fgdxFHD': 280000,
    'GF75HD': 350000,
    '123FHD': 180000,
    '342FHD': 320000,
    'UWU131HD': 300000
}

#-----------------------------------FUNCIONES-----------------------------------
#-----------------------------------1-----------------------------------
def stock_marca(marca):
    stock = [] # aqui se guardarán los nombres de los modelos
    for i, j in productos.items():
        if j[0] == marca: # como es lista, se usan las posiciones especificas
            stock.append(i)
    if len(stock) > 0:
        print(f'El stock es: {len(stock)}\n')
        print('Modelos disponibles: ')
        for i in stock:
            print(i)
    else:
        return False
    return True

#-----------------------------------2-----------------------------------
def buscar_por_precio(minim, maxim):
    while not validar_numero(minim) and not validar_numero(maxim):
        print('Por favor, utilice solo números enteros.')
        minim = input('Ingrese el precio minimo del producto\n >> ')
        maxim = input('Ingrese el precio maximo del producto\n >> ')
    while not minim >= 180000 and not maxim <= 600000:
        print('Los precios buscados están fuera de nuestros parámetros')
        minim = input('Ingrese el precio minimo del producto\n >> ')
        maxim = input('Ingrese el precio maximo del producto\n >> ')
    if minim:
        print
    return True

#-----------------------------------3-----------------------------------
def actualizar_precio():
    try:
        actualizar= int(input('Ingrese el precio que desea actualizar\n >> '))
        modelo= input('Ingrese el modelo del producto que desea actualizar\n >> ')
        if modelo == '8475HD':
            print(f'El {productos["8475HD"]} ha cambiado su valor a {actualizar}. \n')
        elif modelo == '2175HD':
            print(f'El {productos["2175HD"]} ha cambiado su valor a {actualizar}. \n')
        elif modelo == 'JjfFHD':
            print(f'El {productos["JjfFHD"]} ha cambiado su valor a {actualizar}. \n')
        elif modelo == 'fgdxFHD':
            print(f'El {productos["fgdxFHD"]} ha cambiado su valor a {actualizar}. \n')
        elif modelo == 'GF75HD':
            print(f'El {productos["GF75HD"]} ha cambiado su valor a {actualizar}. \n')
        elif modelo == '123FHD':
            print(f'El {productos["123FHD"]} ha cambiado su valor a {actualizar}. \n')
        elif modelo == '342FHD':
            print(f'El {productos["342FHD"]} ha cambiado su valor a {actualizar}. \n')
        elif modelo == 'UWU131HD':
            print(f'El {productos["UWU131HD"]} ha cambiado su valor a {actualizar}. \n')
        else:
            print('Lo siento. El modelo que has escrito no se ha podido encontrar\n')
    except ValueError:
        print('Error. Por favor escriba acorde a los parámetros solicitados\n')

#-----------------------------------NO FUNCIONALES-----------------------------------
def validar_texto(texto):
    if texto == '':
        return False
    for i in texto:
        if i >= 'A' and i <= 'Z':
            continue
        if i >= 'a' and i <= 'z':
            continue
        return False
    return True

def validar_numero(numero):
    if numero == '':
        return False
    for i in numero:
        if i < '0' or i > '9':
            return False
    return True

#-----------------------------------MENU-----------------------------------
while True:
    print('\n*** MENU PRINCIPAL ***')
    print('1. Stock marca')
    print('2. Busqueda por precio')
    print('3. Actualizar precio')
    print('4. Salir')
    print('5. Esta es una opcion nueva')
    print('6. Otra opcion')

    try:
        opcion= int(input('Ingrese una opción\n >> '))
        if opcion == 1:
            buscar_marca= input('Ingrese la marca a consultar\n >> ').upper()
            while not stock_marca(buscar_marca):
                print(f'No se ha encontrado la marca solicitada.\n')
                buscar_marca= input('Ingrese la marca a consultar\n >> ').upper()
            continue

        elif opcion == 2:
            minimo= input('Ingrese el precio minimo del producto\n >> ')
            maximo= input('Ingrese el precio maximo del producto\n >> ')
            while not buscar_por_precio(minimo, maximo):
                print('Lo sentimos, nuestros productos no cuentan con esas cantidades.\n' \
                'Por favor intente con otros mínimos y máximos:')
                minimo= input('Ingrese el precio minimo del producto\n >> ')
                maximo= input('Ingrese el precio maximo del producto\n >> ')
            continue

        elif opcion == 3:
            while not actualizar_precio():
                print('Error')
            continue
        
        elif opcion == 4:
            print('Saliendo del sistema...') 
            break
    except ValueError:
        print('Error. Por favor escriba acorde a los parámetros solicitados\n')