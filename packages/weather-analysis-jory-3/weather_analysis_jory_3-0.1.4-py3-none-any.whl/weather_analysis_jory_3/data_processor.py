"""
data_processor.py

This module contains the DataProcessor class for calculating and printing descriptive statistics.
"""
import logging


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
        self.logger = logging.getLogger(__name__)

        # Logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        )

    def __iter__(self):
        """
        Returns an iterator for numerical columns in the dataset.

        Yields:
            str: The name of the numerical column
        """
        numerical_columns = self.data.select_dtypes(include="number").columns
        if not numerical_columns.any():
            self.logger.warning("No numerical columns found in the dataset.")
            return iter([])  # Return an ampty iterator if no numerical columns
        return iter(numerical_columns)

    def get_statistics(self):
        """
        Calculates and returns descriptive statistics for numerical columns.

        Returns:
            dict: A dictionary with mean, median, mode, and range for each column.
        """
        stats = {}
        # for column in self:
        #     try:
        #         self.logger.info(f"Processing statistics for column: {column}")
        #         stats[column] = {
        #             'mean': self.data[column].mean(),
        #             'median': self.data[column].median(),
        #             'mode': self.data[column].mode()[0],  # Taking the first mode if multiple
        #             'range': self.data[column].max() - self.data[column].min(),
        #         }
        #     except Exception as e:
        #         self.logger.error(f"Error processing column {column}: {e}")
        #         stats[column] = {"error": str(e)}
        # return stats
        for column in self:
            try:
                self.logger.info(f"Processing statistics for column: {column}")
                col_data = self.data[column].dropna()  # Exclude NaN values

                if col_data.empty:  # Check if column is empty after removing NaN
                    self.logger.warning(f"Column {column} contains no valid data.")
                    stats[column] = {
                        "error": "No valid data",
                    }
                else:
                    stats[column] = {
                        'mean': col_data.mean(),
                        'median': col_data.median(),
                        'mode': col_data.mode()[0] if not col_data.mode().empty else None,
                        'range': col_data.max() - col_data.min(),
                    }
            except Exception as e:
                self.logger.error(f"Error processing column {column}: {e}")
                stats[column] = {"error": str(e)}
        return stats

    def print_statistics(self):
        """
        Prints general descriptive statistics for the dataset.
        """
        self.logger.info("Printing general descriptive statistics for the dataset.")
        try:
            print("Descriptive Statistics Summary:")
            print(self.data.describe())
        except Exception as e:
            self.logger.error(f"Error while printing statistics: {e}")
            raise
