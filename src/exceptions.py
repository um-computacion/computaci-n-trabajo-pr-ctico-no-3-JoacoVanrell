class NumeroDebeSerPositivo(Exception):
    
    pass

def ingrese_numero():
    pass
    
#     Returns:
#         int: El número ingresado si es válido.
        
#     Raises:
#         ValueError: Si la entrada no es un número válido.
#         NumeroDebeSerPositivo: Si el número ingresado es negativo.
#     """
#     entrada = input("Ingrese un número: ")
#     try:
#         numero = int(entrada)
#         if numero < 0:
#             raise NumeroDebeSerPositivo("El número debe ser positivo")
#         return numero
#     except ValueError:
#         raise ValueError("La entrada debe ser un número válido") 