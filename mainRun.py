from datetime import datetime
from colors import colorize, VERDE, ROJO, AMARILLO, AZUL, CYAN, MAGENTA, NORMAL, BOLD, UNDERLINE, ITALIC
import openpyxl
from docx import Document


def generar_docx_desde_plantilla(ruta_plantilla, ruta_salida, reemplazos):
    """
    Genera un archivo .docx basado en una plantilla, reemplazando los placeholders.

    Args:
        ruta_plantilla (str): Ruta al archivo de plantilla .docx.
        ruta_salida (str): Ruta donde se guardará el archivo generado.
        reemplazos (dict): Diccionario con los placeholders y sus valores.
    """
    # Cargar la plantilla
    doc = Document(ruta_plantilla)
    
    # Reemplazar placeholders en cada párrafo
    for parrafo in doc.paragraphs:
        for placeholder, valor in reemplazos.items():
            if placeholder in parrafo.text:
                parrafo.text = parrafo.text.replace(placeholder, valor)
    
    # Reemplazar placeholders en tablas (opcional)
    for tabla in doc.tables:
        for fila in tabla.rows:
            for celda in fila.cells:
                for placeholder, valor in reemplazos.items():
                    if placeholder in celda.text:
                        celda.text = celda.text.replace(placeholder, valor)
    
    # Guardar el archivo generado
    doc.save(ruta_salida)
    print(f"Archivo generado en: {ruta_salida}")

# Ejemplo de uso
ruta_plantilla = "Data/Plantillas/Pantilla1.docx"  # Ruta del archivo de plantilla
ruta_salida = "Data/Contratos/resultado.docx"  # Ruta del archivo generado
reemplazos = {
    "{nombre}": "Alexis",
    "{fecha}": "21 de enero de 2025",
    "{mensaje}": "¡Este es un ejemplo generado dinámicamente!"
}

generar_docx_desde_plantilla(ruta_plantilla, ruta_salida, reemplazos)