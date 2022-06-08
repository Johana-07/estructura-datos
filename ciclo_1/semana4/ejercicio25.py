# libreria nympy y pandas

import numpy as np

import pandas as pd

unidad_datos = np.array(
    [
        [2, 5, 3, 2],
        [4, 6, 7, 2],
        [3, 2, 4, 1]
    ]
)

unidades = pd.DataFrame(unidad_datos)
print(unidades)
""" 0  1  2  3
0  2  5  3  2
1  4  6  7  2
2  3  2  4  1 """

unidades = pd.DataFrame(unidad_datos, index=[2015, 2016, 2017], columns=[
                        "Ag", "Au", "Cu", "Pt"])
print(unidades)
"""       Ag  Au  Cu  Pt
2015   2   5   3   2
2016   4   6   7   2
2017   3   2   4   1
"""
