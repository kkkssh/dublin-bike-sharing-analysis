# Dublin Bike Sharing Analysis
A Python project analyzing bike availability patterns by time and station using Pandas


## Project Overview
This project analyses Dublin's bike-sharing station data from February 2024 using Python, Pandas, and Matplotlib.

I looked at how bike availability changed throughout the day, compared availability across stations, and plotted station locations. I also checked the dataset for missing values, duplicates, and inconsistencies in station capacity.


## Dataset

**File:** `data/dublin_bikes_feb_2024.csv`

The dataset contains bike station status snapshots recorded throughout February 2024.

| Column | Description | Purpose |
|---|---|---|
| `STATION ID` | Unique station identifier | Station-level analysis |
| `TIME` | Timestamp of the station status record | Hourly analysis |
| `LAST UPDATED` | Last update timestamp for station information | Station update information |
| `NAME` | Station name | Station-level analysis |
| `BIKE_STANDS` | Total number of bike stands | Station capacity |
| `AVAILABLE_BIKE_STANDS` | Number of available bike stands | Dock availability |
| `AVAILABLE_BIKES` | Number of available bikes | Bike availability |
| `STATUS` | Station operating status | Status checks |
| `ADDRESS` | Station address | Location information |
| `LATITUDE` | North–south geographic coordinate | Geographic visualisation |
| `LONGITUDE` | East–west geographic coordinate | Geographic visualisation |


## Data Cleaning and Quality Checks

| Check | Result |
|---|---|
| Dataset size | 158,574 rows × 11 columns |
| Analysis period | February 2024 |
| Number of stations | 114 |
| Missing values | None |
| Exact duplicate rows | None |
| Records per station | 1,391 each |
| Station status | All records marked `OPEN` |
| Negative values | None in the checked availability columns |
| Capacity inconsistencies | 7,334 records |

The dataset contains 1,391 records for each of the 114 stations. A capacity inconsistency was identified when the sum of `AVAILABLE_BIKES` and `AVAILABLE_BIKE_STANDS` did not equal `BIKE_STANDS`.


## Analysis

### Hourly Bike Availability

#### Average Available Bikes by Hour
![Average Available Bikes by Hour](outputs/hourly_bike_availability.png)
- Average available bikes peaked at 4 AM.
- Average bike availability was relatively high between 1 AM and 5 AM.
- Average available bikes reached their lowest levels between 8 AM and 9 AM.


#### Average Available Bike Stands by Hour
![Average Available Bike Stands by Hour](outputs/hourly_bike_stands_availability.png)
- Average available bike stands peaked at 5 PM.
- Average available bike stands reached their lowest levels between 1 AM and 5 AM.

<br>

### Station-Level Analysis
#### Top 10 Stations by Average Available Bikes
![Top 10 Stations by Average Available Bikes](outputs/top_10_stations_by_bike_availability.png)
- The highest average bike availability was recorded at `HEUSTON BRIDGE (NORTH)`, with 29.24 bikes.


#### Bottom 10 Stations by Average Available Bikes
![Bottom 10 Stations by Average Available Bikes](outputs/bottom_10_stations_by_bike_availability.png)
- The lowest average bike availability was recorded at `ST. STEPHEN'S GREEN SOUTH`, with 1.94 bikes.


#### Average Available Bike Stands by Station
- Highest average number of available bike stands: `MOUNTJOY SQUARE EAST` - 36.25
- Lowest average number of available bike stands: `DAME STREET` - 4.38

<br>

### Geographic Visualisation
![Dublin Bike Station Locations by Average Bike Availability](outputs/dublin_bike_station_locations.png)
- The map shows the locations of 114 Dublin bike stations.
- Colours represent the average number of available bikes at each station.


## Key Findings
- Average bike availability was relatively high during the early morning, peaking at 4 AM.
- Average bike availability was lowest between 8 AM and 9 AM.
- Available bikes and available bike stands generally showed opposite patterns, but their totals did not always match station capacity.


## Limitations
- The dataset contains station status snapshots rather than individual bike rental and return transactions.
- Average bike availability does not directly measure rental demand or the number of trips.
- In 7,334 records, `AVAILABLE_BIKES + AVAILABLE_BIKE_STANDS` did not equal `BIKE_STANDS`. The cause of these inconsistencies was not established.
- The analysis covers February 2024 only, so the findings may not represent other months or current conditions.


## Tools and Technologies
- Python
- Pandas
- Matplotlib


## Data Source
- **Dataset:** [DublinBikes Historical Data - February 2024](https://data.gov.ie/dataset/dublinbikes-api/resource/1244290a-9568-4cb6-ae1f-3a19b5300842)
- **Publisher:** Dublin City Council
- **License:** [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)