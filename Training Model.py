#Training Model

import csv
import random

# Read data
X = []
y = []

with open("fuel_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
    # Skip row if any value is missing
        if row[0] == "" or row[1] == "" or row[2] == "" or row[3] == "":
            continue

        X.append([float(row[0]), float(row[1]), float(row[2])])
        y.append(float(row[3]))

# Initialize weights randomly
w0 = random.random()
w1 = random.random()
w2 = random.random()
w3 = random.random()

learning_rate = 0.0000000000001
epochs = 1000

# Training loop
for _ in range(epochs):
    for i in range(len(X)):
        x1, x2, x3 = X[i]

        # scale inputs (VERY IMPORTANT)
        x1 = x1 / 40000
        x2 = x2 / 900
        x3 = x3 / 180000
        actual = y[i]

        predicted = w0 + w1*x1 + w2*x2 + w3*x3

        error = actual - predicted

        # Update weights
        w0 += learning_rate * error
        w1 += learning_rate * error * x1
        w2 += learning_rate * error * x2
        w3 += learning_rate * error * x3

# Save model
with open("model.txt", "w") as f:
    f.write(f"{w0},{w1},{w2},{w3}")

print("Model trained!")
