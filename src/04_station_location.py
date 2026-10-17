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

# Calculate average available bikes by station
station_avg = df.groupby("STATION ID")["AVAILABLE_BIKES"].mean()

# Add average available bikes to station locations
stations = stations.merge(
    station_avg.rename("AVG_AVAILABLE_BIKES"),
    on="STATION ID"
)

# Draw the scatter plot
plt.scatter(stations["LONGITUDE"], stations["LATITUDE"], c=stations["AVG_AVAILABLE_BIKES"])

# Add labels
plt.title("Dublin Bike Station Locations by Average Bike Availability")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.colorbar(label="Average Available Bikes")

plt.tight_layout()

# Save the graph
plt.savefig("outputs/dublin_bike_station_locations.png", dpi=300)

plt.show()


