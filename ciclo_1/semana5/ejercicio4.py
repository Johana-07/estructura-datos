# Libreria pandas - leer archivos excel

import pandas as pd

ruta = r"C:\Users\Majo\Desktop\REPOSITORIO GITHUB\estructura-datos\ciclo_1\semana5\archivo.xlsx"


datosDataframe = pd.read_excel(ruta, sheet_name="personas")
print(datosDataframe)
"""    Unnamed: 0 first_name  last_name  age  amount_1 amount_2
0           0     Sigrid    Mannock   27      7.17     8.06
1           1        Joe    Hinners   31      1.90        ?
2           2  Theodoric     Rivers   36      1.11      5.9
3           3    Kennedy    Donnell   53      1.41        ?
4           4    Beatrix    Parlett   48      6.69        ?
5           5    Olimpia   Guenther   36      4.62     7.48
6           6     Grange      Douce   40      1.01     4.37
7           7     Sallee  Johnstone   34      4.88        ? """

datosDataframe = pd.read_excel(
    ruta, sheet_name="personas", header=None, skiprows=1)
print(datosDataframe)
print()
""" 0          1          2   3     4     5
0  0     Sigrid    Mannock  27  7.17  8.06
1  1        Joe    Hinners  31  1.90     ?
2  2  Theodoric     Rivers  36  1.11   5.9
3  3    Kennedy    Donnell  53  1.41     ?
4  4    Beatrix    Parlett  48  6.69     ?
5  5    Olimpia   Guenther  36  4.62  7.48
6  6     Grange      Douce  40  1.01  4.37
7  7     Sallee  Johnstone  34  4.88     ? """


datosDataframe = pd.read_excel(
    ruta, sheet_name="personas", header=None, skiprows=1, names=["Id", "Pr Nombre", "Sg Nombre", "Edad", "Salario 1", "Salario 2"])
print(datosDataframe)
print()
""" Id  Pr Nombre  Sg Nombre  Edad  Salario 1 Salario 2
0   0     Sigrid    Mannock    27       7.17      8.06
1   1        Joe    Hinners    31       1.90         ?
2   2  Theodoric     Rivers    36       1.11       5.9
3   3    Kennedy    Donnell    53       1.41         ?
4   4    Beatrix    Parlett    48       6.69         ?
5   5    Olimpia   Guenther    36       4.62      7.48
6   6     Grange      Douce    40       1.01      4.37
7   7     Sallee  Johnstone    34       4.88         ?
"""
