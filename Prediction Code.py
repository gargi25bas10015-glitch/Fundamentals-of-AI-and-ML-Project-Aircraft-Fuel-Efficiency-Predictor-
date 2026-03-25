#Prediction Code

# Load weights
with open("model.txt", "r") as f:
    w0, w1, w2, w3 = map(float, f.read().split(","))

# Input
altitude = float(input("Enter altitude: "))
speed = float(input("Enter speed: "))
weight = float(input("Enter weight: "))

# Prediction
altitude = altitude / 40000
speed = speed / 900
weight = weight / 180000

fuel = w0 + w1*altitude + w2*speed + w3*weight

print("Predicted Fuel:", round(fuel, 2))
