# Gestión de conciertos

Aplicación en Python para gestionar conciertos, entradas y usuarios (práctica de la UD2 de DWES, 2º DAW).

Los usuarios pueden comprar entradas de distintos tipos (grada, pista y VIP) para conciertos y valorar los conciertos a los que han asistido. El programa principal crea varios conciertos y usuarios, hace compras y valoraciones y muestra estadísticas de entradas vendidas, recaudación y precio medio.

## Estructura

```
gestionConciertos/
├── .venv/          Entorno virtual (no se sube a Git)
├── conciertos.py   Módulo conciertos: clases Entrada, EntradaGrada, EntradaPista,
│                   EntradaVIP, Concierto y Usuario
├── main.py         Módulo main: crea conciertos y usuarios, compra entradas,
│                   valora conciertos e imprime las estadísticas
├── .gitignore
└── README.md
```

### Clases del módulo conciertos

- **Entrada**: entrada general. Su precio es el precio base del concierto.
- **EntradaGrada**: hereda de Entrada y tiene un asiento. Su precio es el precio base.
- **EntradaPista**: hereda de Entrada e indica si es de pie. Su precio es el precio base más el 10%.
- **EntradaVIP**: hereda de Entrada e indica si incluye consumición. Su precio es el precio base más el 20% si incluye consumición, o más el 15% si no la incluye.
- **Concierto**: guarda los datos del concierto y sus entradas vendidas. Calcula la recaudación, el precio medio y si quedan entradas disponibles.
- **Usuario**: guarda sus entradas compradas, los conciertos a los que ha asistido y sus valoraciones. Permite comprar entradas y valorar conciertos.

## Crear el entorno virtual

Desde la carpeta del proyecto:

```bash
python -m venv .venv
```

Según el sistema operativo, el comando puede ser `python`, `python3` o `py`.

## Activar el entorno virtual

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows (PowerShell o CMD):

```
.venv\Scripts\activate
```

Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

Al activarlo, aparece `(.venv)` al inicio del prompt.

## Ejecutar

Con el entorno virtual activado:

```bash
python main.py
```

El proyecto no necesita librerías externas.
