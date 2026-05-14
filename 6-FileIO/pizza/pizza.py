import csv

pizza_list = []

with open("sicilian.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pizza_list.append({"small": row["small"]})

for price in pizza_list:
    print(f"{price['small']}")
