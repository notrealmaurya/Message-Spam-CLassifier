import pandas as pd


df = pd.read_csv('emails.csv')

print(df.sample(5))