from conciertos import Concierto, Usuario, EntradaGrada, EntradaPista, EntradaVIP

# Crear 3 conciertos activos y sin entradas vendidas
concierto1 = Concierto('Rosalía', 'Madrid', 40.0, 100, [], True)
concierto2 = Concierto('Coldplay', 'Barcelona', 60.0, 50, [], True)
concierto3 = Concierto('Vetusta Morla', 'Sevilla', 50.0, 20, [], True)

lista_conciertos = [concierto1, concierto2, concierto3]

# Crear 3 usuarios (set() crea un set vacío, porque {} crearía un diccionario)
usuario1 = Usuario('Ana', 25, [], set(), {})
usuario2 = Usuario('Luis', 32, [], set(), {})
usuario3 = Usuario('Marta', 19, [], set(), {})

# Compras: cada usuario compra entradas para 2 conciertos
usuario1.comprar_entrada(concierto1, 'pista')
usuario1.comprar_entrada(concierto2, 'vip')
usuario2.comprar_entrada(concierto1, 'grada')
usuario2.comprar_entrada(concierto3, 'vip')
usuario3.comprar_entrada(concierto1, 'vip')
usuario3.comprar_entrada(concierto2, 'grada')

print('===== ENTRADAS COMPRADAS =====')
print(f'Entradas de {usuario1.nombre}:')
for entrada in usuario1.entradas_compradas:
    print(f'  {entrada}')
print(f'Entradas de {usuario2.nombre}:')
for entrada in usuario2.entradas_compradas:
    print(f'  {entrada}')
print(f'Entradas de {usuario3.nombre}:')
for entrada in usuario3.entradas_compradas:
    print(f'  {entrada}')

# Valoraciones: cada usuario valora 1 concierto
usuario1.valorar(concierto1, 9)
usuario2.valorar(concierto3, 7)
usuario3.valorar(concierto2, 8)

print()
print('===== VALORACIONES =====')
print(f'{usuario1.nombre} valora el {concierto1} con un {usuario1.valoraciones[concierto1]}')
print(f'{usuario2.nombre} valora el {concierto3} con un {usuario2.valoraciones[concierto3]}')
print(f'{usuario3.nombre} valora el {concierto2} con un {usuario3.valoraciones[concierto2]}')

# Imprimir los conciertos y los usuarios
print()
print('===== CONCIERTOS =====')
for concierto in lista_conciertos:
    print(concierto)
    print(f'  Recaudación: {concierto.calcular_recaudacion()} €')
    print(f'  Precio medio: {concierto.calcular_precio_medio()} €')
    print(f'  Entradas disponibles: {concierto.entradas_disponibles()}')

print()
print('===== USUARIOS =====')
print(usuario1)
print(usuario2)
print(usuario3)

print()
print('===== ESTADÍSTICAS =====')

# i. Número total de entradas vendidas
total_entradas = 0
for concierto in lista_conciertos:
    for entrada in concierto.entradas_vendidas:
        total_entradas += 1
print(f'Total de entradas vendidas: {total_entradas}')

# ii. Número de entradas vendidas de cada tipo
entradas_pista = 0
entradas_grada = 0
entradas_vip = 0
for concierto in lista_conciertos:
    for entrada in concierto.entradas_vendidas:
        if type(entrada) == EntradaPista:
            entradas_pista += 1
        elif type(entrada) == EntradaGrada:
            entradas_grada += 1
        elif type(entrada) == EntradaVIP:
            entradas_vip += 1
print(f'Entradas de pista vendidas: {entradas_pista}')
print(f'Entradas de grada vendidas: {entradas_grada}')
print(f'Entradas VIP vendidas: {entradas_vip}')

# iii. Recaudación total
recaudacion_total = 0.0
for concierto in lista_conciertos:
    recaudacion_total += concierto.calcular_recaudacion()
print(f'Recaudación total: {recaudacion_total} €')

# iv. Precio medio de todas las entradas
if total_entradas == 0:
    precio_medio_total = 0.0
else:
    precio_medio_total = recaudacion_total / total_entradas
print(f'Precio medio de todas las entradas: {precio_medio_total} €')

# v. Concierto con más entradas vendidas, y cuántas
concierto_mas_vendido = lista_conciertos[0]
mas_entradas = 0
for entrada in concierto_mas_vendido.entradas_vendidas:
    mas_entradas += 1
for concierto in lista_conciertos:
    numero_entradas = 0
    for entrada in concierto.entradas_vendidas:
        numero_entradas += 1
    if numero_entradas > mas_entradas:
        concierto_mas_vendido = concierto
        mas_entradas = numero_entradas
print(f'Concierto con más entradas vendidas: {concierto_mas_vendido}')
print(f'Entradas vendidas en ese concierto: {mas_entradas}')

# vi. Concierto con menos entradas vendidas, y cuántas
concierto_menos_vendido = lista_conciertos[0]
menos_entradas = 0
for entrada in concierto_menos_vendido.entradas_vendidas:
    menos_entradas += 1
for concierto in lista_conciertos:
    numero_entradas = 0
    for entrada in concierto.entradas_vendidas:
        numero_entradas += 1
    if numero_entradas < menos_entradas:
        concierto_menos_vendido = concierto
        menos_entradas = numero_entradas
print(f'Concierto con menos entradas vendidas: {concierto_menos_vendido}')
print(f'Entradas vendidas en ese concierto: {menos_entradas}')
