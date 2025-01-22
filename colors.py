#COLORES DE LA TERMINAL (CÓDIGO ANSI)

# Códigos de estilo
NORMAL = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'

# Colores de texto (foreground)
NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'

# Colores de fondo (background)
BG_NEGRO = '\033[40m'
BG_ROJO = '\033[41m'
BG_VERDE = '\033[42m'
BG_AMARILLO = '\033[43m'
BG_AZUL = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_BLANCO = '\033[47m'

# Colores brillantes de texto
BRIGHT_NEGRO = '\033[90m'
BRIGHT_ROJO = '\033[91m'
BRIGHT_VERDE = '\033[92m'
BRIGHT_AMARILLO = '\033[93m'
BRIGHT_AZUL = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_BLANCO = '\033[97m'

# Colores brillantes de fondo
BG_BRIGHT_NEGRO = '\033[100m'
BG_BRIGHT_ROJO = '\033[101m'
BG_BRIGHT_VERDE = '\033[102m'
BG_BRIGHT_AMARILLO = '\033[103m'
BG_BRIGHT_AZUL = '\033[104m'
BG_BRIGHT_MAGENTA = '\033[105m'
BG_BRIGHT_CYAN = '\033[106m'
BG_BRIGHT_BLANCO = '\033[107m'

def colorize(text: str, color: str, background: str = '', style: str = '') -> str:
    """
    Colorea un texto con los códigos ANSI especificados.
    
    Args:
        text: Texto a colorear
        color: Color del texto (foreground)
        background: Color de fondo (opcional)
        style: Estilo adicional (opcional)
    
    Returns:
        str: Texto coloreado con códigos ANSI
    """
    return f"{style}{background}{color}{text}{NORMAL}"

# Ejemplo de uso:
if __name__ == "__main__":
    print(colorize("Texto normal", BLANCO))
    print(colorize("Texto rojo", ROJO))
    print(colorize("Texto verde brillante", VERDE))
    print(colorize("Texto azul con fondo amarillo", AZUL, BG_AMARILLO))
    print(colorize("Texto negrita cyan", CYAN, style=BOLD))
    print(colorize("Texto subrayado magenta", MAGENTA, style=UNDERLINE))
    print(colorize("Texto cursivo", AMARILLO, style=ITALIC))
