import csv
from typing import List, Optional
from rivm.rivm.utils import file_path_and_mode


class ServiceError(Exception):
    massage = "File name not provided"


class CSVService:
    def __init__(self,
                 headers: Optional[List] = None,
                 source: str = None,
                 destination: str = None,
                 delimiter=","):
        self.headers = headers
        self.source = source
        self.destination = destination
        self.delimiter = delimiter

    def read(self):
        try:
            with open(*file_path_and_mode(self.source)) as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    yield row
        except TypeError:
            raise ServiceError
