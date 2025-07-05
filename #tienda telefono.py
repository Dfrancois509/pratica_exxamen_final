#tienda telefono
 
telefonos = { 
    'A123': ['Samsung', 6.5, '4GB', '64GB', 'Exynos 9611', '48MP'], 
    'B234': ['Apple', 6.1, '6GB', '128GB', 'A15 Bionic', '12MP'], 
    'C345': ['Xiaomi', 6.43, '8GB', '256GB', 'Snapdragon 778G', '108MP'], 
    'D456': ['Motorola', 6.7, '4GB', '128GB', 'MediaTek Helio G85', '50MP'], 
    'E567': ['Samsung', 6.4, '6GB', '128GB', 'Exynos 850', '64MP'], 
    'F678': ['Apple', 5.4, '4GB', '64GB', 'A14 Bionic', '12MP'], 
    'G789': ['Xiaomi', 6.67, '12GB', '512GB', 'Snapdragon 8 Gen 1', '200MP'], 
} 

def menu(): 
    print('*** MENÚ PRINCIPAL ***')
    print('1. Buscar por marca')
    print('2. Buscar por rango de precios') 
    print('3. Actualizar precio de modelo ')
    print('4. Salir') 

stock = { 

    'A123': [199990, 5], 

    'B234': [849990, 2], 

    'C345': [349990, 8], 

    'D456': [179990, 0], 

    'E567': [229990, 10], 

    'F678': [399990, 1], 

    'G789': [699990, 3], 
} 

#CODIGO DE CHATGPT MAS SIMPLE
def busca_por_marca():
    la_marca = str(input('¿Cuál es el nombre de la marca? ').capitalize())
    encontrados = False
    
    for clave, datos in telefonos.items():
        if datos[0] == la_marca:
            encontrados = True
            print(f'{clave} → {datos}')
            if clave in stock:
                precio = stock[clave][0]
                cantidad = stock[clave][1]
                print(f'Precio: ${precio:,} | Stock: {cantidad} unidades')
            else:
                print('    No hay información de stock para este modelo.')
    if not encontrados:
        print('No tenemos esta marca en nuestra tienda.')




def rango_de_precio ():
    global stock , telefonos
    while True:
        try:
                precio_min = int(input('Ingrese un precio Minimo: '))
                precio_max = int(input('Ingrese un precio Maximo: '))
                break
        except ValueError:
            print('Ingrese un valor valido')
    encontrados = False
    for clave, datos in stock.items():
        precio = datos[0]
        if precio_min <= precio <= precio_max:
            encontrados = True
            print(f'Modelo {clave}: {precio:,}$ | Stock: {datos[1]} unidades')
            if clave in telefonos:
                print(f'Marca: {telefonos[clave][0]}, RAM: {telefonos[clave][2]}, Cámara: {telefonos[clave][-1]}')

    if not encontrados:
        print('No tenemos productos en este rango de precio.')



def actualiza_precios ():
    global stock , telefonos
    selecciona_por_clave = (input('Ingrese la clave de producto deseado: '))
        
    encontrados = False
    for clave , datos in stock.items() : 
        if clave == selecciona_por_clave : 
            encontrados = True
            print('Agregar: ')
            print('Eliminar: ')
            print('Sacar en la cantidad')
            que_hacer = int(input('Que quieres hacer? '))
            
            if que_hacer == 1: 
                nueva_cantidad = int(input('Cuanto Deseas Agregar? '))
                datos[1] += nueva_cantidad
                print(f'Cantidad el stock ha sido actualizado | Nueva Cantidad : {datos[1]}')
            elif que_hacer == 2 : 
                    tele = str(input('clave del telefono '))
                    if clave == tele : 
                        del telefonos[clave]
                        print('Producto ha Sido Eliminado En El Sistema!')
    if not encontrados :
        print('Clave no registrado en el sistema!')


def ejecuta ():
    while True :
        menu()
        try : 
            selecciona_opcion = int(input('OPCIONES ? '))
        except : 
            print('Ingrese un valor valido para seleccionar una opcion (NUMERO ENTERO)')
            continue
        
        if selecciona_opcion == 1 : 
            busca_por_marca()
        elif selecciona_opcion == 2 :
            rango_de_precio()
        elif selecciona_opcion == 3 : 
            actualiza_precios()
        elif selecciona_opcion == 4 : 
            print('SALIENDO DEL PROGRAMA')
            break

ejecuta()
