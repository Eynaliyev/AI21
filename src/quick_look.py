import pandas as pd

def quick_look(data):
    print("Top 5 rows:")
    print(data.head())

    print("\nBottom 5 rows:")
    print(data.tail())

    print("\nRandom sample of 5 rows:")
    print(data.sample(1))

    print("\nShape of the data:")
    print(data.shape)

    print("\nSummary of the data:")
    print(data.describe(include='all'))

    score_columns = ["Helpfulness", "Honesty", "Harmlessness", "Factuality", "Effectiveness"]
    print("\nSummary of scores:")
    print(data[score_columns].describe())
