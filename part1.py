import pandas as pd
import multiprocessing as mp
from functools import partial
from geopy.distance import distance

def calculate_distance(user_id, df):
    """
    A helper function to calculate the total distance traveled by a user
    """
    user_data = df[df['individual_id'] == user_id]
    total_distance = 0.0
    for i in range(len(user_data)-1):
        lat1 = user_data.iloc[i]['latitude']
        lon1 = user_data.iloc[i]['longitude']
        lat2 = user_data.iloc[i+1]['latitude']
        lon2 = user_data.iloc[i+1]['longitude']
        total_distance += distance((lat1, lon1), (lat2, lon2)).km
    return user_id, total_distance

def calculate_total_distance(df):
    """
    A function to calculate the total distance traveled by each user in the dataset using parallel programming
    """
    pool = mp.Pool(processes=mp.cpu_count())
    user_ids = df['individual_id'].unique()
    func = partial(calculate_distance, df=df)
    result = pool.map(func, user_ids)
    pool.close()
    pool.join()
    result = pd.DataFrame(result, columns=['user_id', 'total_distance'])
    return result

df = pd.read_csv('combined_trajectories.csv')
df = df[:2]
result = calculate_total_distance(df)
print(result)






