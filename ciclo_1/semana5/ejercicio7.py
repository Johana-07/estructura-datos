#  exportar diccionarios ha archivo json

import json

datos = dict()

datos['clients'] = []

datos['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

datos['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

datos['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})


ruta = r"C:\Users\Majo\Desktop\REPOSITORIO GITHUB\estructura-datos\ciclo_1\semana5\archivo.json"

with open(ruta, 'w') as file:
    json.dump(datos, file, indent=4)
# Declaracion "with" para aperturar el archivo destino
# "json.dump", para escribir en el archivo "data", en un archivo con indentado 4
