import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/dublin_bikes_feb_2024.csv")


# Convert TIME to datetime so dates and hours can be extracted
df["TIME"] = pd.to_datetime(df["TIME"])


# Extract the hour from TIME for hourly analysis
df["HOUR"] = df["TIME"].dt.hour

print(df[["TIME", "HOUR"]].head(10))


# Calculate average available bikes by hour
print("\n=== Average Available Bikes by Hour ===")
hourly_avg = df.groupby("HOUR")["AVAILABLE_BIKES"].mean()
print(hourly_avg.round(2))


# Plot average available bikes by hour

# Create a figure
plt.figure(figsize=(10, 5))

# Draw the line chart
plt.plot(hourly_avg.index, hourly_avg.values, marker="o")

# Add labels
plt.title("Average Available Bikes by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Available Bikes")

plt.xticks(range(24))
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the graph
plt.savefig("outputs/hourly_bike_availability.png", dpi=300)

plt.show()



# Calculate average available bike stands by hour
print("\n=== Average Available Bike Stands by Hour ===")
hourly_stands_avg = df.groupby("HOUR")["AVAILABLE_BIKE_STANDS"].mean()
print(hourly_stands_avg.round(2))


# Plot average available bike stands by hour

# Create a figure
plt.figure(figsize=(10, 5))

# Draw the line chart
plt.plot(hourly_stands_avg.index, hourly_stands_avg.values, marker="o")

# Add labels
plt.title("Average Available Bike Stands by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Available Bike Stands")

plt.xticks(range(24))
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the graph
plt.savefig("outputs/hourly_bike_stands_availability.png", dpi=300)

plt.show()



# Plot average available bikes and bike stands by hour

# Create a figure
plt.figure(figsize=(10, 5))

# Draw both line charts
plt.plot(
    hourly_avg.index,
    hourly_avg.values,
    marker="o",
    label="Available Bikes"
)

plt.plot(
    hourly_stands_avg.index,
    hourly_stands_avg.values,
    marker="o",
    label="Available Bike Stands"
)

# Add labels and legend
plt.title("Average Available Bikes and Bike Stands by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Count")
plt.legend()

plt.xticks(range(24))
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the graph
plt.savefig("outputs/hourly_bike_availability_comparison.png", dpi=300)

plt.show()
