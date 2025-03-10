"""
This module orchestrates the weather data analysis process using DataLoader and DataProcessor.
"""

from .data_loader2 import DataLoader
from .data_processor import (DataProcessor)


class WeatherAnalysis:
    """
    A high-level class orchestrating data loading and processing.
    """

    def __init__(self, file_path):
        """
        Initializes the WeatherAnalysis class.

        Parameters:
            file_path (str): The path to the CSV file.
        """
        self.loader = DataLoader(file_path)
        self.data = None
        self.processor = None

    def run_analysis(self):
        """
        Performs the weather data analysis by loading data and computing statistics.
        """
        self.data = self.loader.load_data()
        self.processor = DataProcessor(self.data)

        print(self.data.head())  # Print the first 5 rows
        self.processor.print_statistics()

        # Detailed statistics
        detailed_stats = self.processor.get_statistics()
        print("\nDetailed Statistics (Mean, Median, Mode, Range):")
        for column, stats in detailed_stats.items():
            print(f"{column}: {stats}")


if __name__ == "__main__":
    file_path = r"C:\Users\Jory_\Documents\PYCHARM\Pycharm-Projects\CS3270\weatherTestData.csv"
    analysis = WeatherAnalysis(file_path)
    analysis.run_analysis()
