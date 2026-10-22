import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/dublin_bikes_feb_2024.csv")


# Calculate average available bikes by station
print("\n=== Average Available Bikes by Station ===")
station_avg = df.groupby("NAME")["AVAILABLE_BIKES"].mean()
print(station_avg.round(2))


# Find stations with the highest and lowest average available bikes
print("\n=== Highest Average Available Bikes ===")
print(station_avg.sort_values(ascending=False).head(5).round(2))

print("\n=== Lowest Average Available Bikes ===")
print(station_avg.sort_values().head(5).round(2))


# Plot the top 10 stations by average available bikes

# Create a figure
plt.figure(figsize=(12, 6))

# Select the top 10 stations by average available bikes
top_10_stations = station_avg.sort_values(ascending=False).head(10)

# Draw the bar chart
plt.bar(top_10_stations.index, top_10_stations.values)

# Add labels
plt.title("Top 10 Stations by Average Available Bikes")
plt.xlabel("Station")
plt.ylabel("Average Available Bikes")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save the graph
plt.savefig("outputs/top_10_stations_by_bike_availability.png", dpi=300)

plt.show()


# Plot the bottom 10 stations by average available bikes

# Create a figure
plt.figure(figsize=(12, 6))

# Select the bottom 10 stations by average available bikes
bottom_10_stations = station_avg.sort_values(ascending=True).head(10)

# Draw the bar chart
plt.bar(bottom_10_stations.index, bottom_10_stations.values)

# Add labels
plt.title("Bottom 10 Stations by Average Available Bikes")
plt.xlabel("Station")
plt.ylabel("Average Available Bikes")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save the graph
plt.savefig("outputs/bottom_10_stations_by_bike_availability.png", dpi=300)

plt.show()



# Calculate average available bike stands by station
print("\n=== Average Available Bike Stands by Station ===")
station_stands_avg = df.groupby("NAME")["AVAILABLE_BIKE_STANDS"].mean()
print(station_stands_avg.round(2))


# Find stations with the highest and lowest average available bike stands
print("\n=== Highest Average Available Bike Stands ===")
print(station_stands_avg.sort_values(ascending=False).head(10).round(2))

print("\n=== Lowest Average Available Bike Stands ===")
print(station_stands_avg.sort_values().head(10).round(2))



# Compare hourly bike availability at selected stations

# Select the top 3 and bottom 3 stations by average bike availability
selected_stations = pd.concat(
    [
        station_avg.sort_values(ascending=False).head(3),
        station_avg.sort_values().head(3),
    ]
).index

# Calculate average available bikes by station and hour
df["TIME"] = pd.to_datetime(df["TIME"])
df["HOUR"] = df["TIME"].dt.hour

hourly_station_avg = (
    df[df["NAME"].isin(selected_stations)]
    .groupby(["HOUR", "NAME"])["AVAILABLE_BIKES"]
    .mean()
    .unstack()
)

# Plot hourly bike availability for the selected stations
plt.figure(figsize=(12, 6))

for station in hourly_station_avg.columns:
    plt.plot(hourly_station_avg.index, hourly_station_avg[station], label=station)


plt.title("Hourly Bike Availability at Selected Stations")
plt.xlabel("Hour of Day")
plt.ylabel("Average Available Bikes")
plt.xticks(range(0, 24))
plt.legend(fontsize=9)

plt.tight_layout()

# Save the graph
plt.savefig("outputs/hourly_station_bike_availability.png", dpi=300)

plt.show()
