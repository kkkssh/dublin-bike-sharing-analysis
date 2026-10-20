import pandas as pd
import folium

# Load the dataset
df = pd.read_csv("data/dublin_bikes_feb_2024.csv")


stations = df[["STATION ID", "NAME", "LATITUDE", "LONGITUDE"]].drop_duplicates(
    subset="STATION ID"
)

station_avg = df.groupby("STATION ID")["AVAILABLE_BIKES"].mean()

stations = stations.merge(station_avg.rename("AVG_AVAILABLE_BIKES"), on="STATION ID")


# Create a map centred on Dublin
bike_map = folium.Map(
    location=[53.35, -6.26],
    zoom_start=13,
    tiles="https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}.png",
    attr="© Stadia Maps © OpenStreetMap contributors",
)


# Add a marker for each station
for _, row in stations.iterrows():
    avg_bikes = row["AVG_AVAILABLE_BIKES"]

    # Set the marker colour based on average bike availability
    if avg_bikes < 10:
        colour = "red"
    elif avg_bikes < 20:
        colour = "orange"
    else:
        colour = "green"

    # Add station location and information to the map
    folium.CircleMarker(
        location=[row["LATITUDE"], row["LONGITUDE"]],
        radius=5,
        popup=f'{row["NAME"]}: {avg_bikes:.1f} bikes',
        tooltip=row["NAME"],
        color=colour,
        fill=True,
    ).add_to(bike_map)


# Create a legend for marker colours
legend_html = """
<div style="
    position: fixed;
    bottom: 30px;
    left: 30px;
    width: 210px;
    background-color: white;
    border: 2px solid grey;
    z-index: 9999;
    padding: 10px;
    font-size: 14px;
">
    <b>Average Available Bikes</b><br>
    <span style="color:red;">●</span> Below 10 bikes<br>
    <span style="color:orange;">●</span> 10 to less than 20 bikes<br>
    <span style="color:green;">●</span> 20 bikes or more
</div>
"""

# Add the legend to the map
bike_map.get_root().html.add_child(folium.Element(legend_html))


# Adjust the map to show all stations
bike_map.fit_bounds(
    [
        [stations["LATITUDE"].min(), stations["LONGITUDE"].min()],
        [stations["LATITUDE"].max(), stations["LONGITUDE"].max()],
    ]
)


# Save the map as an HTML file
bike_map.save("outputs/dublin_bike_map_average.html")
