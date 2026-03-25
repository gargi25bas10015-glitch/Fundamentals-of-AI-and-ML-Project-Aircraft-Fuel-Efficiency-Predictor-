#DATASET GENERATION

import random
import csv

file = open("fuel_data.csv", "w", newline="")
writer = csv.writer(file)

# Header
writer.writerow(["altitude", "speed", "weight", "fuel"])

for i in range(200):
    altitude = random.randint(2000, 40000)
    speed = random.randint(200, 900)
    weight = random.randint(30000, 180000)

    fuel = (0.0005 * altitude) + (0.05 * speed) + (0.0003 * weight)

    writer.writerow([altitude, speed, weight, fuel])

file.close()

print("Dataset created!")
