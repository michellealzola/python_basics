import pickle
import pandas as pd

df = pd.read_csv('electroless_plating_365day_dataset.csv')
data_dict = df.to_dict(orient='records')

with open('electroless_plating.pkl', 'wb') as f:
    pickle.dump(data_dict, f)
