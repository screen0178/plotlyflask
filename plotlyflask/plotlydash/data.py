"""Prepare data for Plotly Dash."""
import pandas as pd
import numpy as np


# def create_dataframe():
#     """Create Pandas DataFrame from local CSV."""
#     df = pd.read_csv('data/311-calls.csv', parse_dates=['created'])
#     df['created'] = df['created'].dt.date
#     df.drop(columns=['incident_zip'], inplace=True)
#     num_complaints = df['complaint_type'].value_counts()
#     to_remove = num_complaints[num_complaints <= 30].index
#     df.replace(to_remove, np.nan, inplace=True)
#     return df

def instalytics_dataframe():
    """DataFrame from local tbl_scraping.csv"""
    df = pd.read_csv('data/tbl_scrapingEdited.csv')
    df['taken_at'] = pd.to_datetime(df['taken_at']).dt.date
    df.set_index('taken_at',inplace=True)
    print(df)
    return df
    
