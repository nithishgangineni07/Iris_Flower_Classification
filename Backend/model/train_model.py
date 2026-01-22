import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(df):

    X = df.drop("species",axis=1)
    y = df["species"]

    #Pipeline
    model = Pipeline(
        steps = [
            
                ("classifier",RandomForestClassifier(
                n_estimators=100,
                random_state=42
            ))
        ]
    )

    #train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X,y,test_size=0.2,random_state=42, stratify=y
    )

    #Train

    model.fit(X_train, y_train)

    return model