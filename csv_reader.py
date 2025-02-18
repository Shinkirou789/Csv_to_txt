import csv
import sys
import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", help="Nombre del archivo csv", required=True)

    args = parser.parse_args()

    # Leer el archivo CSV
    with open(args.file, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        encabezados = next(lector)  # Obtener los nombres de las columnas
        columnas = {nombre: [] for nombre in encabezados}  # Crear un diccionario para las columnas

    # Recorre cada fila y guarda los valores en las listas correspondientes
        for fila in lector:
            for i, valor in enumerate(fila):
                columnas[encabezados[i]].append(valor)

# Guardar cada columna en un archivo de texto separado
    for nombre, valores in columnas.items():
        with open(f"{nombre}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(valores))  # Escribe cada valor en una nueva línea
            print(f"Archivo {nombre}.txt creado")
    print("Proceso completado.")

if __name__ == "__main__":
    main()