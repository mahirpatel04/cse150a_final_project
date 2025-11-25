import pandas as pd
import os
from pathlib import Path
from enum import Enum

class ProcessingType(Enum):
    TWENTY_FIVE_PERCENT = "twenty_five_percent"
    AVERAGE = "average"
    TEN_PERCENT = "ten_percent"
    ONE_STANDARD_DEVIATION = "one_standard_deviation"
    

def read_data(file_path: str) -> pd.DataFrame:
    """
    Read in the data from the file and return a pandas dataframe
    
    Args:
        file_path: str - name of file in the data folder
        
    Returns:
        pd.DataFrame - the dataframe containing the data
    """
    return pd.read_csv(os.path.join(os.path.dirname(__file__), "data", file_path))


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the data by removing any rows with missing values
    """
    return data.dropna()


def preprocess(data: pd.DataFrame, processing_type: ProcessingType) -> pd.DataFrame:
    """
    Preprocess the data by converting everything into binary values.
    
    For each column, we calculate what percentile the student is in. If they are in the top 25%, they are given a 1, otherwise a 0. Keep in mind the data we need to first calculate what percentile the student's score is in for each column.
    
    Args:
        data: pd.DataFrame - the dataframe containing the data
        
    Returns:
        pd.DataFrame - the dataframe containing the preprocessed data
    """
    for column in data.columns:
        if column != "student_id":
            
            if processing_type == ProcessingType.TWENTY_FIVE_PERCENT:   
                threshold = data[column].quantile(0.75)
            elif processing_type == ProcessingType.AVERAGE:
                threshold = data[column].mean()
            elif processing_type == ProcessingType.TEN_PERCENT:
                threshold = data[column].quantile(0.9)
            elif processing_type == ProcessingType.ONE_STANDARD_DEVIATION:
                threshold = data[column].mean() + data[column].std()
            else:
                raise ValueError(f"Invalid processing type: {processing_type}")
            
            
            # Then convert to binary depending on the processing type
            data[column] = data[column].apply(lambda x: 1 if x > threshold else 0)
    return data

def save_data(data: pd.DataFrame, file_path: str) -> None:
    """
    Save the data to a csv file
    """
    file_path = os.path.join(os.path.dirname(__file__), "data", file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    data.to_csv(file_path, index=False)

def main():
    data = read_data("student_exam_scores.csv")
    cleaned_data = clean_data(data)
    processed_data = preprocess(cleaned_data.copy())
    save_data(processed_data, "processed_data.csv")