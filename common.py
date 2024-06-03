import pandas as pd
from config import *

def LOAD_DATASET():

    chunks = []

    for chunk in pd.read_csv(
            DATASET_PATH, 
            chunksize=CHUNK_SIZE, 
            low_memory=False
        ):
        chunks.append(chunk)
        
    df = pd.concat(chunks, axis=0)
    del chunks
    return df

def set_unkown_if_null(dataframe, key):
    mask = dataframe[key] == STR_NULL
    dataframe.loc[mask, key] = UNKNOWN
    
def is_time_difference_within_threshold(start_time, end_time, threshold_hours):
    start = pd.to_datetime(start_time, format='%H:%M:%S', errors=ERROR_HANDLING_STRATEGY)
    end = pd.to_datetime(end_time, format='%H:%M:%S', errors=ERROR_HANDLING_STRATEGY)
    
    if pd.isna(start) or pd.isna(end):
        return False
    time_diff = (end - start).total_seconds() / 3600.0
    return time_diff <= threshold_hours