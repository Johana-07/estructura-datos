import pandas as pd
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str):
    if ".csv" in rutaFileCsv:
        try:
            datos = pd.read_csv(rutaFileCsv)
            info = datos[["Country", "Language", "Gross Earnings"]]
            resumen = info.pivot_table(index=["Country", "Language"]).head(10)
            return resumen
        except:
            print("Error al leer el archivo de datos.")
    else:
        print("Extensión inválida.")


print(listaPeliculas(rutaFileCsv))
