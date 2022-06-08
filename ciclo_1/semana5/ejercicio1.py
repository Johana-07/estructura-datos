# libreria pandas -exportar cvs

import pandas as pd

datos = {'first_name': ['Sigrid', 'Joe', 'Theodoric', 'Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
         'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
         'age': [27, 31, 36, 53, 48, 36, 40, 34],
         'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
         'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

datosDataframe = pd.DataFrame(datos)

print(datosDataframe, "\n")

# first_name  last_name  age  amount_1 amount_2
# 0     Sigrid    Mannock   27      7.17     8.06
# 1        Joe    Hinners   31      1.90        ?
# 2  Theodoric     Rivers   36      1.11      5.9
# 3    Kennedy    Donnell   53      1.41        ?
# 4    Beatrix    Parlett   48      6.69        ?
# 5    Olimpia   Guenther   36      4.62     7.48
# 6     Grange      Douce   40      1.01     4.37
# 7     Sallee  Johnstone   34      4.88        ?

print(type(datosDataframe))  # <class 'pandas.core.frame.DataFrame'>

ruta = r"C:\Users\Majo\Desktop\REPOSITORIO GITHUB\estructura-datos\ciclo_1\semana5\archivo.csv"
datosDataframe.to_csv(ruta, sep=";")
