import pandas as pd
import seaborn as sns

def load_data():
    df = sns.load_dataset("iris")
    return df