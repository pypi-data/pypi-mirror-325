import pandas as pd

pd.set_option('display.max_colwidth', None) 
from .file_loader import FileLoader
from .data_preprocessor import DataPreprocessor
from .exploratory_data_analyzer import ExploratoryDataAnalyzer
from .data_visualizer import Visualizer


class DataProcessor(FileLoader, DataPreprocessor, ExploratoryDataAnalyzer):

    def __init__(self, 
                 file_path: str, 
                 name: str = None, 
                 parse_dates: list = None,
                 cat_cols: list = None, 
                 num_cols: list = None, 
                 time_cols: list = None, 
                 target_name: str = None):

        FileLoader.__init__(self, file_path, name, parse_dates)

        DataPreprocessor.__init__(self, self.data, self.name)

        ExploratoryDataAnalyzer.__init__(self, self.data, self.name, cat_cols, num_cols, time_cols, target_name)

    def info(self):
        
        data_info = pd.DataFrame(
            {
                'file_path': [self.file_path],
                'name': [self.name],
                'cat_cols': [self.cat_cols],
                'num_cols': [self.num_cols],
                'time_cols': [self.time_cols],
                'target_name': [self.target_name]
            }
        )
        
        return data_info

    
    def data_preprocessor(self, threshold: int = 0.8, string_columns: list = None):

        Visualizer.show_title('Типы данных')
        display(self.check_types())
        
        Visualizer.show_title('Пропуски')
        display(self.get_missing_info())
        
        Visualizer.show_title('Полные дубликаты')
        count, part, sample = self.get_duplicates_info()
        print(f'В таблице {count} ({round(part, 6)*100}%) дубликатов')
        display(sample)

        fuzzy_duplicates = self.find_fuzzy_duplicates(threshold=threshold, string_columns=string_columns)
        if fuzzy_duplicates:
            Visualizer.show_title('Неявные дубликаты в строковых столбцах')
            for column, df in fuzzy_duplicates.items():
                Visualizer.show_title(column)
                display(df)
        else:
            Visualizer.show_title('Не обнаружено неявных дубликатов')
                
        return None        

    
    def analyze_categorical_features(self, categorical_columns: list = None, unique_threshold: int = 15, include_numeric: bool = True):
       
        unique_summary, frequent_rare_values, figs = self.analyze_categorical(
            categorical_columns=categorical_columns, unique_threshold=unique_threshold, include_numeric=include_numeric
        )

        if unique_summary is not None:

            Visualizer.show_title('Анализ категориальных признаков')
            Visualizer.show_title('Количество уникальных значений в столбцах')
            display(unique_summary)

            Visualizer.show_title('Наиболее и наименее популярные категории')
            display(frequent_rare_values)

            Visualizer.show_title('Распределения')
            for fig in figs:
                display(fig)

    
    def analyze_numerical_features(self, numerical_columns: list = None):
       
        num_description, extrems, figs = self.analyze_numerical(numerical_columns=numerical_columns)

        if num_description is not None:
            
            Visualizer.show_title('Анализ количественных признаков')

            Visualizer.show_title('Сводная статистика')
            display(num_description)

            Visualizer.show_title('Экстремальные значения')
            display(extrems)

            Visualizer.show_title('Распределения')
            for fig in figs:
                display(fig)

    
    def analyze_time_features(self, time_columns: list = None, target_value: str = None):
       
        time_description, avg_deltas, intervals, rolling_means = self.analyze_time_series(
            time_columns=time_columns, target_value=target_value
        )

        if time_description is not None:
            
            Visualizer.show_title('Анализ временных признаков')
            Visualizer.show_title('Сводная статистика')
            display(time_description)

            for i, column in enumerate(self.time_cols):
                Visualizer.show_title(column)
                print(f"Средний интервал между записями: {avg_deltas[i]}\n")
                display(intervals[i])
                display(rolling_means[i])

            
    def eda(self, categorical_columns: list = None, unique_threshold: int = 15, include_numeric: bool = True, 
            numerical_columns: list = None, time_columns: list = None, target_value: str = None):
        
        self.analyze_categorical_features(categorical_columns, unique_threshold, include_numeric)
        self.analyze_numerical_features(numerical_columns)
        self.analyze_time_features(time_columns, target_value)

