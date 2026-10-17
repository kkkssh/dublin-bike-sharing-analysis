import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/dublin_bikes_feb_2024.csv")


# Check station locations
print("\n=== Station Locations ===")
print(df[["STATION ID", "NAME", "LATITUDE", "LONGITUDE"]].head())


# Count unique stations
print("\n=== Number of Stations ===")
print(df["STATION ID"].nunique())


# Plot station locations

# Create a figure
plt.figure(figsize=(8, 7))

# Get unique station locations
stations = df[
    ["STATION ID", "NAME", "LATITUDE", "LONGITUDE"]
].drop_duplicates(subset="STATION ID")

# Check the number of unique stations
print("\n=== Number of Unique Stations ===")
print(len(stations))

# Draw the scatter plot
plt.scatter(stations["LONGITUDE"], stations["LATITUDE"])

# Add labels
plt.title("Dublin Bike Station Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()

# Save the graph
plt.savefig("outputs/dublin_bike_station_locations.png", dpi=300)

plt.show()
