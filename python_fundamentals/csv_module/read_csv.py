import csv

FILENAME = "python_fundamentals/csv_module/spark_application_properties.csv"  # csv create with the web scrapping script

with open(FILENAME, "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(
        csvfile
    )  # toma el objeto de archivo como entrada y devuelve un objeto iterable

    fields = next(csvreader)  # Headers
    # print("Headers> ", fields)

    data = list(csvreader)
    # print(data[0])

# headers
headers = ["id", "nombre", "apellido"]
# declarar filas
data = [
    ["1", "nombre1", "murillo"],
    ["2", "nombre2", "Murillo"],
    ["3", "nombre2", "murilo"],
]
# path
FILENAME2 = "python_fundamentals/csv_module/university_records.csv"

with open(FILENAME2, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)
    # Check the file


FILENAME3 = "python_fundamentals/csv_module/writer.csv"
# DictReader / leeremos el archivo creado arriba
with open(FILENAME2, "r", encoding="utf-8") as csvfile:
    csvreader = csv.DictReader(csvfile)
    headers = csvreader.fieldnames
    # print(list(csvreader))
    data: list[dict] = list(csvreader)
    # print(data)
    with open(FILENAME3, "w+", encoding="utf-8") as csvwriter:
        csvwriter = csv.DictWriter(csvwriter, fieldnames=headers)
        csvwriter.writeheader()
        for row in data:
            if row["nombre"] == "nombre1" or row["apellido"] == "murillo":
                csvwriter.writerow(row)
        # csvwriter.writerows(data)
