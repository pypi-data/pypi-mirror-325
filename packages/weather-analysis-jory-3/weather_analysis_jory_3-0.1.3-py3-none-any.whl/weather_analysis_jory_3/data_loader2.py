"""
This module contains the DataLoader class for loading data from a CSV file into a pandas DataFrame.
"""

import pandas as pd


class DataLoader:
    """
    A class responsible for loading data from a CSV file.
    """

    def __init__(self, file_path):
        """
        Initializes the DataLoader with a file path.

        Parameters:
            file_path (str): The path to the CSV file.
        """
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """
        Loads a CSV file into a pandas DataFrame.

        Returns:
            DataFrame: The loaded dataset.
        """
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Dataset loaded successfully from {self.file_path}")
        except FileNotFoundError:
            print(f"Error: The file at {self.file_path} was not found.")
            raise
        except Exception as e:
            print(f"Error loading dataset: {e}")
            raise
        return self.data
