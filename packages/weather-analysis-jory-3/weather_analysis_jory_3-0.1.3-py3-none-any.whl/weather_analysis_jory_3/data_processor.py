"""
This module contains the DataProcessor class for calculating and printing descriptive statistics.
"""


class DataProcessor:
    """
    A class responsible for processing and analyzing the dataset.
    """

    def __init__(self, data):
        """
        Initializes the DataProcessor with a dataset.

        Parameters:
            data (DataFrame): The pandas DataFrame containing the dataset.
        """
        self.data = data

    def get_statistics(self):
        """
        Calculates and returns descriptive statistics for numerical columns.

        Returns:
            dict: A dictionary with mean, median, mode, and range for each column.
        """
        stats = {}
        for column in self.data.select_dtypes(include='number').columns:
            stats[column] = {
                'mean': self.data[column].mean(),
                'median': self.data[column].median(),
                'mode': self.data[column].mode()[0],  # Taking the first mode if multiple
                'range': self.data[column].max() - self.data[column].min(),
            }
        return stats

    def print_statistics(self):
        """
        Prints general descriptive statistics for the dataset.
        """
        print("Descriptive Statistics Summary:")
        print(self.data.describe())
