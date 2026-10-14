import pandas as pd

# Load the dataset
df = pd.read_csv("data/dublin_bikes_feb_2024.csv")


# Display the first 5 rows
print("\n=== First 5 Rows ===")
print(df.head())


# Check the number of rows and columns
print("\n=== Dataset Shape ===")
print(df.shape)


# Check column names, data types, and non-null values
print("\n=== Dataset Information ===")
df.info()


# List all column names for reference
print("\n=== Column Names ===")
print(df.columns.tolist())


# Check missing values in each column
print("\n=== Missing Values ===")
print(df.isna().sum())


# Convert TIME to datetime so dates and hours can be extracted
df["TIME"] = pd.to_datetime(df["TIME"])

# Check date range
print("\n=== Time Range ===")
print("Start:", df["TIME"].min())
print("End:", df["TIME"].max())


# Count the number of stations
print("\n=== Number of Stations ===")
print(df["STATION ID"].nunique())


# Check duplicate rows
print("\n=== Duplicate Rows ===")
print(df.duplicated().sum())


# Count records by station status
print("\n=== Station Status ===")
print(df["STATUS"].value_counts())


# Display summary statistics for bike capacity and availability
print("\n=== Numerical Summary ===")
print(
    df[
        [
            "BIKE_STANDS",
            "AVAILABLE_BIKE_STANDS",
            "AVAILABLE_BIKES",
        ]
    ].describe()
)


# Summarise the number of records per station
print("\n=== Records per Station ===")
print(df["STATION ID"].value_counts().describe())


# Check time intervals between records across all stations
# Note: these intervals do not represent the recording frequency
# of an individual station
print("\n=== Time Differences ===")
time_differences = df["TIME"].sort_values().diff()
print(time_differences.describe())


# Check for negative values
print("\n=== Negative Values ===")
print(df[["AVAILABLE_BIKES", "AVAILABLE_BIKE_STANDS"]].lt(0).sum())


# Check whether bike counts match the total number of stands
print("\n=== Bike Stand Consistency ===")
inconsistent_rows = (
    df["AVAILABLE_BIKES"] + df["AVAILABLE_BIKE_STANDS"]
    != df["BIKE_STANDS"]
)
print("Inconsistent rows:", inconsistent_rows.sum())    


# Count inconsistent records by station
print("\n=== Inconsistent Records by Station ===")
print(
    df.loc[inconsistent_rows]
    .groupby("NAME")
    .size()
    .sort_values(ascending=False)
)

