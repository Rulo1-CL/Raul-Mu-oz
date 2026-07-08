def validar_codigo(codigo, juegos):
   
    if not codigo or codigo.strip() == "":
        return False
 
    codigo_limpio = codigo.strip().upper()
    for clave in juegos.keys():
        if clave.upper() == codigo_limpio:
            return False
    return True

def validar_titulo(titulo):
    return titulo is not None and titulo.strip() != ""

def validar_plataforma(plataforma):
    return plataforma is not None and plataforma.strip() != ""

def validar_genero(genero):
    return genero is not None and genero.strip() != ""

def validar_clasificacion(clasificacion):
    
    return clasificacion in ['E', 'T', 'M']

def validar_multiplayer(multiplayer):
    return multiplayer.lower() in ['s', 'n']

def validar_editor(editor):
    return editor is not None and editor.strip() != ""

def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_stock(stock_str):
    try:
        stock = int(stock_str)
        return stock >= 0
    except ValueError:
        return False



def leer_opcion():
    try:
        opcion_str = input("Ingrese opción: ")
        opcion = int(opcion_str)
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
            return None
    except ValueError:
        print("Debe seleccionar una opción válida")
        return None


def stock_plataforma(plataforma, juegos, inventario):
    total_stock = 0
    plat_buscada = plataforma.strip().lower()
    
   
    for codigo, datos in juegos.items():
        plat_juego = datos[1].lower()
        if plat_juego == plat_buscada:
            if codigo in inventario:
                total_stock += inventario[codigo][1] # Suma el stock
                
    print(f"El total de stock disponibles es: {total_stock}")


def busqueda_precio(p_min, p_max, juegos, inventario):
    resultados = []
    
    for codigo, datos_inv in inventario.items():
        precio = datos_inv[0]
        stock = datos_inv[1]
        
        
        if p_min <= precio <= p_max and stock > 0:
            if codigo in juegos:
                titulo = juegos[codigo][0]
                resultados.append(f"{titulo}--{codigo}")
                
    if len(resultados) > 0:
        
        resultados.sort()
        print(f"Los juegos encontrados son: {resultados}")
    else:
        print("No hay juegos en ese rango de precios.")


def buscar_codigo(codigo, diccionario):
   
    cod_buscado = codigo.strip().upper()
    for k in diccionario.keys():
        if k.upper() == cod_buscado:
            return True
    return False


def obtener_clave_exacta(codigo, diccionario):
   
    cod_buscado = codigo.strip().upper()
    for k in diccionario.keys():
        if k.upper() == cod_buscado:
            return k
    return codigo


def actualizar_precio(codigo, nuevo_precio, inventario):

    if buscar_codigo(codigo, inventario):
        clave_real = obtener_clave_exacta(codigo, inventario)
        inventario[clave_real][0] = nuevo_precio
        return True
    return False


def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
   
    if buscar_codigo(codigo, juegos):
        return False
        
    
    cod_key = codigo.strip().upper()
    
   
    mp_bool = True if multiplayer.lower() == 's' else False
    
   
    juegos[cod_key] = [titulo.strip(), plataforma.strip(), genero.strip(), clasificacion, mp_bool, editor.strip()]
    inventario[cod_key] = [int(precio), int(stock)]
    return True


def eliminar_juego(codigo, juegos, inventario):
    if buscar_codigo(codigo, juegos):
        clave_real = obtener_clave_exacta(codigo, juegos)
     
        juegos.pop(clave_real, None)
        inventario.pop(clave_real, None)
        return True
    return False



def main():
    
    juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
        'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
        'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
        'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
        'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
        'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
    }

    inventario = {
        'G001': [9990, 7],
        'G002': [19990, 0],
        'G003': [42990, 3],
        'G004': [14990, 5],
        'G005': [17990, 9],
        'G006': [39990, 2]
    }

    ejecutando = True

   
    while ejecutando:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================")
        
        opcion = leer_opcion()
        
        if opcion is None:
            continue
            
        if opcion == 1:
            plat = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plat, juegos, inventario)
            
        elif opcion == 2:
            while True:
                try:
                    p_min_str = input("Ingrese precio mínimo: ")
                    p_min = int(p_min_str)
                    p_max_str = input("Ingrese precio máximo: ")
                    p_max = int(p_max_str)
                    
                    
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max, juegos, inventario)
                        break
                    else:
                        print("Valores fuera de rango lógico (Mínimo debe ser menor o igual al máximo y mayores a 0)")
                        break
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
        elif opcion == 3:
            procesando_precios = True
            while procesando_precios:
                cod = input("Ingrese código del juego: ")
                nuevo_p_str = input("Ingrese nuevo precio: ")
                
                if validar_precio(nuevo_p_str):
                    nuevo_p = int(nuevo_p_str)
                    
                    if actualizar_precio(cod, nuevo_p, inventario):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                else:
                    print("Precio inválido. Debe ser un entero positivo.")
                
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp != 's':
                    procesando_precios = False
                    
        elif opcion == 4:
            cod = input("Ingrese código del juego: ")
            tit = input("Ingrese título: ")
            plat = input("Ingrese plataforma: ")
            gen = input("Ingrese género: ")
            clas = input("Ingrese clasificación: ").strip().upper()
            mult = input("¿Es multiplayer? (s/n): ")
            edit = input("Ingrese editor: ")
            prec = input("Ingrese precio: ")
            stk = input("Ingrese stock: ")
            
           
            if not validar_codigo(cod, juegos):
                print("Error en código (vacío, contiene espacios o ya se encuentra registrado).")
            elif not validar_titulo(tit):
                print("Error: El título no puede estar vacío.")
            elif not validar_plataforma(plat):
                print("Error: La plataforma no puede estar vacía.")
            elif not validar_genero(gen):
                print("Error: El género no puede estar vacío.")
            elif not validar_clasificacion(clas):
                print("Error: La clasificación debe ser exactamente 'E', 'T' o 'M'.")
            elif not validar_multiplayer(mult):
                print("Error: La opción de multiplayer debe responderse con 's' o 'n'.")
            elif not validar_editor(edit):
                print("Error: El editor no puede estar vacío.")
            elif not validar_precio(prec):
                print("Error: El precio debe ser un número entero mayor que cero.")
            elif not validar_stock(stk):
                print("Error: El stock debe ser un número entero mayor o igual a cero.")
            else:
                
                if agregar_juego(cod, tit, plat, gen, clas, mult, edit, prec, stk, juegos, inventario):
                    print("Juego agregado")
                else:
                    print("El código ya existe")
                    
        elif opcion == 5:
            cod = input("Ingrese código del juego que desea eliminar: ")
           
            if eliminar_juego(cod, juegos, inventario):
                print("Juego eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            ejecutando = False

if __name__ == "__main__":
    main()