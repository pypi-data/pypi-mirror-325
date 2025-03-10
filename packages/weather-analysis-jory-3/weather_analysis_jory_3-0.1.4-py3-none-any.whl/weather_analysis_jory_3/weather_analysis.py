"""
weather_analysis.py

This module orchestrates the weather data analysis process using DataLoader and DataProcessor.
"""
import logging
from .data_loader2 import DataLoader
from .data_processor import DataProcessor


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
        self.file_path = file_path
        self.logger = logging.getLogger(__name__)

        # Logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

    def run_analysis(self):
        """
        Performs the weather data analysis by loading data and computing statistics.
        """
        try:
            self.logger.info("Starting weather data analysis.")
            loader = DataLoader(self.file_path)

            # Load data in chunks
            for chunk_index, chunk in enumerate(loader.load_data(), start=1):
                self.logger.info(f"Processing chunk {chunk_index}")
                processor = DataProcessor(chunk)

                # Print general statistics
                processor.print_statistics()

                # Print detailed statistics
                detailed_stats = processor.get_statistics()
                self.logger.info(f"Detailed Statistics for Chunk {chunk_index}:")
                for column, stats in detailed_stats.items():
                    self.logger.info(f"{column}: {stats}")

            self.logger.info("Weather data analysis completed successfully.")
        except Exception as e:
            self.logger.error(f"Error during weather analysis: {e}")
            raise


if __name__ == "__main__":
    file_path = r"C:\Users\Jory_\Documents\PYCHARM\Pycharm-Projects\CS3270\weatherTestData.csv"
    analysis = WeatherAnalysis(file_path)
    analysis.run_analysis()
