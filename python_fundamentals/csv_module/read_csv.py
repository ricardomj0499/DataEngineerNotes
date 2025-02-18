import csv

FILENAME = "python_fundamentals/csv_module/spark_application_properties.csv"

with open(FILENAME, "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(
        csvfile
    )  # toma el objeto de archivo como entrada y devuelve un objeto iterable
    # for row in csvreader:
    # print(row)
    fields = next(csvreader)
    # print(fields)


# declarar filas
rows = [
    ["foo", "bar", "spam"],
    ["oof", "rab", "maps"],
    ["writerow", "isn't", "writerows"],
]

FILENAME2 = "python_fundamentals/csv_module/university_records.csv"
header = ["1", "2", "3"]
with open(FILENAME2, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)


# DictReader
with open(FILENAME2, "r", encoding="utf-8") as csvfile:
    csvreader = csv.DictReader(csvfile)
    print(csvreader)
    data = dict(csvreader)
    # for row in csvreader:
    # print(row)
    print(data)
