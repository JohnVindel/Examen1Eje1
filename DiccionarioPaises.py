#*****Examen, Ejercicio 1 - Diccionario*****#

paises = {
    "Honduras": 9746000,
    "Guatemala": 16600000,
    "Nicaragua": 6546000,
    "El Salvador": 6454000,
    "Costarica": 5048000
}

try:
    intro = input("Ingrese el pais: ")
    print("El pais es {} y tiene {} de habitanes.".format(intro, format(paises[intro], ",d")))
except KeyError:
    print ("El pais que ingreso no existe")