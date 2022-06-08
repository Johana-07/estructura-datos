# libreria pandas

import pandas as pd

elementos = {
    "Numero Atomico": [1, 6, 47, 88],
    "Masa Atomica": [1.008, 12.011, 107.87, 226],
    "Familia": ["No metal", "No metal", "Metal", "Metal"]
}

tablaPeriodica = pd.DataFrame(elementos, index=["H", "C", "Ag", "Ra"], columns=[
    "Familia", "Masa Atomica", "Numero Atomico"])
print(tablaPeriodica)
""" Familia  Masa Atomica  Numero Atomico
H   No metal         1.008               1
C   No metal        12.011               6
Ag     Metal       107.870              47
Ra     Metal       226.000              88 """
