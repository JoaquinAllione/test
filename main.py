import logging

logger = logging.getLogger("Main APP")
logger.setLevel(logging.DEBUG)

def Imprimir(texto:str):
    if isinstance(texto,str):
        print(texto)
        logger.info("Se imprimió correctamente.")
    else:
        logger.error("Debe ser un string.")

Imprimir("Hola")