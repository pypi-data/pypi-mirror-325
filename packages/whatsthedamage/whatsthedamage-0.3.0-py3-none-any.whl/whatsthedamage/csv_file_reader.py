import csv
from typing import Sequence
from whatsthedamage.csv_row import CsvRow


class CsvFileReader:
    def __init__(self, filename: str, dialect: str = 'excel-tab', delimiter: str = '\t'):
        """
        Initialize the CsvFileReader with the path to the CSV file, dialect, and delimiter.

        :param filename: The path to the CSV file to read.
        :param dialect: The dialect to use for the CSV reader.
        :param delimiter: The delimiter to use for the CSV reader.
        """
        self.filename: str = filename
        self.dialect: str = dialect
        self.delimiter: str = delimiter
        self.headers: Sequence[str] = []  # List to store header names
        self.rows: list[CsvRow] = []  # List to store CsvRow objects

    def read(self) -> None:
        """
        Read the CSV file and populate headers and rows.

        :return: None
        """
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                csvreader = csv.DictReader(file, dialect=self.dialect, delimiter=self.delimiter, restkey='leftover')
                if csvreader.fieldnames is None:
                    raise ValueError("CSV file is empty or missing headers.")
                self.headers = csvreader.fieldnames  # Save the header
                self.rows = []
                for row in csvreader:
                    self.rows.append(CsvRow(row))
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")

    def get_headers(self) -> Sequence[str]:
        """
        Get the headers of the CSV file.

        :return: A list of header names.
        """
        return self.headers

    def get_rows(self) -> list[CsvRow]:
        """
        Get the rows of the CSV file as CsvRow objects.

        :return: A list of CsvRow objects.
        """
        return self.rows
