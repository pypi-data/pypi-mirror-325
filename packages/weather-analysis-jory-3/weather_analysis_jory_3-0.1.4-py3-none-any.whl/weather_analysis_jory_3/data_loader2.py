"""
data_loader2.py

This module contains the DataLoader class for loading data from a CSV file into a pandas DataFrame.
"""

import pandas as pd
import logging


class DataLoader:
    """
    A class responsible for loading data from a CSV file.
    """

    def __init__(self, file_path, chunk_size=1000):
        """
        Initializes the DataLoader with a file path and a chunk size.

        Parameters:
            file_path (str): The path to the CSV file.
            chunk_size (int): Number of rows to read at a time (default:1000)
        """
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.logger = logging.getLogger(__name__)
        self.data = None

        # Logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        )

    def load_data(self):
        """
        Loads a CSV file into a pandas DataFrame.

        Returns:
            DataFrame: A chunk of the dataset.
        """
        try:
            self.logger.info(f"Starting to load data from {self.file_path}")
            for chunk in pd.read_csv(self.file_path, chunksize=self.chunk_size):
                self.logger.info(f"Loaded a chunk of {len(chunk)} rows.")
                yield chunk
        except FileNotFoundError:
            self.logger.error(f"The file at {self.file_path} was not found.")
            raise
        except pd.errors.ParserError as e:
            self.logger.error(f"Error parsing the CSV file: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error while loading data: {e}")
            raise
