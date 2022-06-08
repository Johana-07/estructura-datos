# Libreria pandas


from traceback import print_tb
import pandas as pd


ruta = r"C:\Users\Majo\Desktop\REPOSITORIO GITHUB\estructura-datos\ciclo_1\semana5\archivo.csv"

datosDataframe = pd.read_csv(ruta, sep=";")
print(datosDataframe)
print()
""" Unnamed: 0 first_name  last_name  age  amount_1 amount_2
0           0     Sigrid    Mannock   27      7.17     8.06
1           1        Joe    Hinners   31      1.90        ?
2           2  Theodoric     Rivers   36      1.11      5.9
# 3           3    Kennedy    Donnell   53      1.41        ?
# 4           4    Beatrix    Parlett   48      6.69        ?
# 5           5    Olimpia   Guenther   36      4.62     7.48
# 6           6     Grange      Douce   40      1.01     4.37
# 7           7     Sallee  Johnstone   34      4.88        ? """

datosDataframe = pd.read_csv(ruta, sep=";", header=None)
print(datosDataframe)
"""      0           1          2    3         4         5
0  NaN  first_name  last_name  age  amount_1  amount_2
1  0.0      Sigrid    Mannock   27      7.17      8.06
2  1.0         Joe    Hinners   31       1.9         ?
3  2.0   Theodoric     Rivers   36      1.11       5.9
4  3.0     Kennedy    Donnell   53      1.41         ?
5  4.0     Beatrix    Parlett   48      6.69         ?
6  5.0     Olimpia   Guenther   36      4.62      7.48
7  6.0      Grange      Douce   40      1.01      4.37
8  7.0      Sallee  Johnstone   34      4.88         ? """


datosDataframe = pd.read_csv(ruta, sep=";", skiprows=1, names=[
    "Id", "Pr Nombre", "Sg Nombre", "Edad", "Salario 1", "Salario 2"])
print(datosDataframe)
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


datosDataframe = pd.read_csv(ruta, sep=";", skiprows=1, names=[
    "Id", "Pr Nombre", "Sg Nombre", "Edad", "Salario 1", "Salario 2"], na_values="?")
print(datosDataframe)
""" Id  Pr Nombre  Sg Nombre  Edad  Salario 1  Salario 2
0   0     Sigrid    Mannock    27       7.17       8.06
1   1        Joe    Hinners    31       1.90        NaN
2   2  Theodoric     Rivers    36       1.11       5.90
3   3    Kennedy    Donnell    53       1.41        NaN
4   4    Beatrix    Parlett    48       6.69        NaN
5   5    Olimpia   Guenther    36       4.62       7.48
6   6     Grange      Douce    40       1.01       4.37
7   7     Sallee  Johnstone    34       4.88        NaN """


datosDataframe = pd.read_csv(ruta, sep=";", skiprows=1, names=[
    "Id", "Pr Nombre", "Sg Nombre", "Edad", "Salario 1", "Salario 2"], na_values="?",
    index_col="Id")
print(datosDataframe)
""" Id
0      Sigrid    Mannock    27       7.17       8.06
1         Joe    Hinners    31       1.90        NaN
2   Theodoric     Rivers    36       1.11       5.90
3     Kennedy    Donnell    53       1.41        NaN
4     Beatrix    Parlett    48       6.69        NaN
5     Olimpia   Guenther    36       4.62       7.48
6      Grange      Douce    40       1.01       4.37
7      Sallee  Johnstone    34       4.88        NaN
"""

datosDataframe = pd.read_csv(ruta, sep=";", skiprows=1, names=[
    "Id", "Pr Nombre", "Sg Nombre", "Edad", "Salario 1", "Salario 2"], na_values="?",
    index_col=(["Pr Nombre", "Sg Nombre"]))
print(datosDataframe)
""" Pr Nombre Sg Nombre
Sigrid    Mannock     0    27       7.17       8.06
Joe       Hinners     1    31       1.90        NaN
Theodoric Rivers      2    36       1.11       5.90
Kennedy   Donnell     3    53       1.41        NaN
Beatrix   Parlett     4    48       6.69        NaN
Olimpia   Guenther    5    36       4.62       7.48
Grange    Douce       6    40       1.01       4.37
Sallee    Johnstone   7    34       4.88        NaN
"""


print(datosDataframe)
print()
print(datosDataframe["Edad"][4])  # 48
print(type(datosDataframe["Edad"][4]))  # <class 'numpy.int64'>
