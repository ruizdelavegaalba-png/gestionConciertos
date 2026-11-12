# Entrada general para un concierto
class Entrada:
    # Constructor: guarda el concierto de la entrada
    def __init__(self, concierto):
        self.concierto = concierto

    # Devuelve el precio base del concierto
    def get_precio_total(self):
        return self.concierto.precio_base

    # Devuelve el texto de la entrada general
    def __str__(self):
        return f'Entrada general para {self.concierto.artista} - {self.get_precio_total()} €'


# Entrada de grada, hereda de Entrada
class EntradaGrada(Entrada):
    # Constructor: llama al padre y guarda el asiento
    def __init__(self, concierto, asiento):
        super().__init__(concierto)
        self.asiento = asiento

    # Devuelve el precio base del concierto
    def get_precio_total(self):
        return self.concierto.precio_base

    # Devuelve el texto de la entrada de grada
    def __str__(self):
        return f'Entrada de grada para {self.concierto.artista} - {self.get_precio_total()} €'


# Entrada de pista, hereda de Entrada
class EntradaPista(Entrada):
    # Constructor: llama al padre y guarda si es de pie
    def __init__(self, concierto, de_pie):
        super().__init__(concierto)
        self.de_pie = de_pie

    # Devuelve el precio base más el 10%
    def get_precio_total(self):
        return self.concierto.precio_base + self.concierto.precio_base * 10 / 100

    # Devuelve el texto de la entrada de pista
    def __str__(self):
        return f'Entrada de pista para {self.concierto.artista} - {self.get_precio_total()} €'


# Entrada VIP, hereda de Entrada
class EntradaVIP(Entrada):
    # Constructor: llama al padre y guarda si incluye consumición
    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion

    # Devuelve el precio base más el 20% si incluye consumición, o más el 15% si no
    def get_precio_total(self):
        if self.incluye_consumicion:
            return self.concierto.precio_base + self.concierto.precio_base * 20 / 100
        else:
            return self.concierto.precio_base + self.concierto.precio_base * 15 / 100

    # Devuelve el texto de la entrada VIP
    def __str__(self):
        return f'Entrada VIP para {self.concierto.artista} - {self.get_precio_total()} €'


# Concierto con sus datos y sus entradas vendidas
class Concierto:
    # Constructor: guarda todos los datos del concierto
    def __init__(self, artista, ciudad, precio_base, aforo_maximo, entradas_vendidas, activo):
        self.artista = artista
        self.ciudad = ciudad
        self.precio_base = precio_base
        self.aforo_maximo = aforo_maximo
        self.entradas_vendidas = entradas_vendidas
        self.activo = activo

    # Devuelve la suma de los precios de las entradas vendidas (0.0 si no hay)
    def calcular_recaudacion(self):
        if self.entradas_vendidas == []:
            return 0.0
        total = 0.0
        for entrada in self.entradas_vendidas:
            total += entrada.get_precio_total()
        return total

    # Devuelve el precio medio de las entradas vendidas (0.0 si no hay)
    def calcular_precio_medio(self):
        numero_entradas = 0
        for entrada in self.entradas_vendidas:
            numero_entradas += 1
        if numero_entradas == 0:
            return 0.0
        return self.calcular_recaudacion() / numero_entradas

    # Devuelve True si se han vendido menos entradas que el aforo máximo, y False si no
    def entradas_disponibles(self):
        numero_entradas = 0
        for entrada in self.entradas_vendidas:
            numero_entradas += 1
        if numero_entradas < self.aforo_maximo:
            return True
        else:
            return False

    # Devuelve el texto del concierto
    def __str__(self):
        return f'Concierto de {self.artista} en {self.ciudad}'


# Usuario que compra entradas y valora conciertos
class Usuario:
    # Constructor: guarda todos los datos del usuario
    def __init__(self, nombre, edad, entradas_compradas, conciertos_asistidos, valoraciones):
        self.nombre = nombre
        self.edad = edad
        self.entradas_compradas = entradas_compradas
        self.conciertos_asistidos = conciertos_asistidos
        self.valoraciones = valoraciones

    # Compra una entrada del tipo indicado ('grada', 'pista' o 'vip') para un concierto
    def comprar_entrada(self, concierto, tipo_entrada):
        # El concierto debe estar activo
        if not concierto.activo:
            raise Exception(f'El {concierto} no está activo')

        # El usuario no puede haber asistido ya al concierto
        if concierto in self.conciertos_asistidos:
            raise Exception(f'{self.nombre} ya ha asistido al {concierto}')

        # Deben quedar entradas disponibles
        if not concierto.entradas_disponibles():
            raise Exception(f'No quedan entradas disponibles para el {concierto}')

        if tipo_entrada == 'grada':
            entrada = EntradaGrada(concierto, '1A')
        elif tipo_entrada == 'pista':
            entrada = EntradaPista(concierto, True)
        elif tipo_entrada == 'vip':
            entrada = EntradaVIP(concierto, True)
        # El tipo de entrada debe existir
        else:
            raise Exception(f'El tipo de entrada {tipo_entrada} no existe')

        concierto.entradas_vendidas.append(entrada)
        self.entradas_compradas.append(entrada)
        self.conciertos_asistidos.add(concierto)

    # Añade o modifica la valoración (de 0 a 10) de un concierto asistido
    def valorar(self, concierto, valoracion):
        # El usuario debe haber asistido al concierto
        if not (concierto in self.conciertos_asistidos):
            raise Exception(f'{self.nombre} no ha asistido al {concierto}')

        # La valoración debe estar entre 0 y 10
        if valoracion < 0 or valoracion > 10:
            raise Exception(f'La valoración {valoracion} debe estar entre 0 y 10')

        self.valoraciones[concierto] = valoracion

    # Devuelve el nombre y el número de conciertos asistidos
    def __str__(self):
        numero_conciertos = 0
        for concierto in self.conciertos_asistidos:
            numero_conciertos += 1
        return f'{self.nombre} (ha asistido a {numero_conciertos})'
