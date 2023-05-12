import pandas as pd
import folium
from folium.plugins import HeatMap
import matplotlib.pyplot as plt

#function for part 2 of question 2

def find_hotspots(df):
    

    beijing_boundary = ((39.442357, 115.425874), (40.532994, 117.502329))


    df = df[(df['latitude'] >= beijing_boundary[0][0]) & (df['latitude'] <= beijing_boundary[1][0]) & (df['longitude'] >= beijing_boundary[0][1]) & (df['longitude'] <= beijing_boundary[1][1])]
    
    #spatial hotspots
    heatmap_data = df[['latitude', 'longitude']].values.tolist()
    map_obj = folium.Map(location=[39.9, 116.4], zoom_start=11)
    HeatMap(heatmap_data, radius=15).add_to(map_obj)
    map_obj.save('spatial_hotspots.html')
    
    df['time'] = pd.to_datetime(df['time'], format="%H:%M:%S")
    #temporal hotspots
    hourly_counts = df.groupby(df['time'].dt.hour).size()
    hourly_counts.plot(kind='line', figsize=(10,5))
    plt.xlabel('Hour of the day')
    plt.ylabel('Number of location points')
    plt.title('Temporal hotspots')
    plt.savefig('temporal_hotspots.png')

df = pd.read_csv('combined_trajectories.csv')
# df = df[:100000]
find_hotspots(df)
