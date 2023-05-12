import pandas as pd
from geopy.distance import distance
#part 1 of question 2

def calculate_distance(df):
    
    user_ids = df['individual_id'].unique()
    result = []
    for user_id in user_ids:
        user_data = df[df['individual_id'] == user_id]
        total_distance = 0.0
        for i in range(len(user_data)-1):
            lat1 = user_data.iloc[i]['latitude']
            lon1 = user_data.iloc[i]['longitude']
            lat2 = user_data.iloc[i+1]['latitude']
            lon2 = user_data.iloc[i+1]['longitude']
            total_distance += distance((lat1, lon1), (lat2, lon2)).km
        result.append((user_id, total_distance))
    result = pd.DataFrame(result, columns=['user_id', 'total_distance'])
    return result

df = pd.read_csv('combined_trajectories.csv')

result = calculate_distance(df)
result.to_csv('data.csv', index = False)
print(result)