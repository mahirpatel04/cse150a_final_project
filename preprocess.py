import pandas as pd
import os
from pathlib import Path

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


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
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
            # First calculate the 75th percentile (top 25% threshold)
            percentile = data[column].quantile(0.75)
            # Then convert to binary (1 if in top 25%, 0 otherwise)
            data[column] = data[column].apply(lambda x: 1 if x > percentile else 0)
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

if __name__ == "__main__":
    main()