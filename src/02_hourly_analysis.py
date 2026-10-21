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



# Compare bike availability during morning peak hours and other hours

# Define morning peak hours as 7 AM to 9 AM
morning_peak = df[df["HOUR"].between(7, 9)]
other_hours = df[~df["HOUR"].between(7, 9)]

# Calculate average available bikes
morning_avg = morning_peak["AVAILABLE_BIKES"].mean()
other_avg = other_hours["AVAILABLE_BIKES"].mean()

print("\n=== Morning Peak vs Other Hours ===")
print(f"Morning peak (7 AM-9 AM): {morning_avg:.2f} bikes")
print(f"Other hours: {other_avg:.2f} bikes")

# Plot the comparison
plt.figure(figsize=(7, 5))

plt.bar([0, 0.3], [morning_avg, other_avg], width=0.10)

plt.xticks([0, 0.3], ["Morning Peak\n(7-9 AM)", "Other Hours"])

plt.xlim(-0.15, 0.45)

plt.title("Average Bike Availability: Morning Peak vs Other Hours")
plt.ylabel("Average Available Bikes")

plt.tight_layout()

plt.savefig("outputs/morning_peak_comparison.png", dpi=300)

plt.show()

