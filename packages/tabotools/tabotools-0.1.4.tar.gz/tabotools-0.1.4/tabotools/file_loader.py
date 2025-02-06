import pandas as pd
from .data_visualizer import Visualizer


class FileLoader:

    def __init__(self, file_path:str, name: str = None, parse_dates: list = None):
        self.file_path = file_path
        self.name = name if name else file_path.split('/')[-1].split('.')[0]
        self.data = self.load(parse_dates=parse_dates)
        
        Visualizer.show_info(self.data, self.name, self.file_path)

    
    def load(self, parse_dates: list = None):
        
        if self.file_path.endswith('.csv'):
            return pd.read_csv(self.file_path, parse_dates=parse_dates)
        elif self.file_path.endswith('.xlsx'):
            return pd.read_excel(self.file_path, parse_dates=parse_dates)
        else:
            raise ValueError('Unsupported file format!')
