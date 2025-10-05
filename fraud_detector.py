import pandas as pd
import numpy as np
from transaction_data import generate_transactions

def flag_anomalies(df: pd.DataFrame):
    # The standard threshold for statistical anomalies is 3 standard deviations
    threshold = 3  
    mean = df["Amount"].mean()
    std = df["Amount"].std()

    # Calculate Z-Score
    df["Z-Score"] = (df["Amount"] - mean) / std
    
    # Flag transactions with an absolute Z-Score > threshold
    df["Flagged"] = df["Z-Score"].abs() > threshold

    return df