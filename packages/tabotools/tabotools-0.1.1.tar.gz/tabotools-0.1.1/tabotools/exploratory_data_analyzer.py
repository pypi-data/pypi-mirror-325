import pandas as pd
pd.set_option('display.max_columns', None)  

import matplotlib.pyplot as plt
from .data_visualizer import Visualizer
import seaborn as sns

sns.set_style('whitegrid')


class ExploratoryDataAnalyzer():

    def __init__(self, data: pd.DataFrame, name: str = None, 
                 cat_cols: list = None, num_cols: list = None, time_cols: list = None, 
                 target_name: str = None):
        self.data = data
        self.name = name
        self.cat_cols = cat_cols
        self.num_cols = num_cols
        self.time_cols = time_cols
        self.target_name = target_name
        

    def set_cat_cols(self, categorical_columns: list = None, unique_threshold=15, include_numeric=True) -> None:
        
        if categorical_columns:
            self.cat_cols = categorical_columns
    
        elif not self.cat_cols:

            self.cat_cols = self.data.select_dtypes(include=['object', 'category']).columns.tolist()
        
            if include_numeric:
                numeric_candidates = [
                    column for column in self.data.select_dtypes(include=['int', 'float']).columns
                    if self.data[column].nunique() <= unique_threshold
                ]
                self.cat_cols.extend(numeric_candidates)
                
        return None


    def set_num_cols(self, numerical_columns: list = None) -> None:

        if numerical_columns:
            self.num_cols = numerical_columns
            self.cat_cols = [x for x in self.cat_cols if x not in self.num_cols]

        else:
            self.num_cols = self.data.select_dtypes(include=['int', 'float']).columns.tolist()
            self.num_cols = [x for x in self.num_cols if x not in self.cat_cols]
            
        
    def set_time_cols(self, time_columns: list = None) -> None:

        if time_columns:
            self.time_cols = time_columns

        else:
            self.time_cols = self.data.select_dtypes(include=['datetime64[ns]']).columns.tolist()
            

    def analyze_single_categorical(self, cat_column: str = None):

        if cat_column:
            result_tables = []
            
            column_data = self.data[cat_column].value_counts().reset_index()
            column_data.columns = [cat_column, 'count']
            column_data['part,%'] = column_data['count'].apply(lambda x: round(x/column_data['count'].sum() * 100, 2))
    
            combined_data = Visualizer.preview_data(column_data)
            
            result_tables.append(combined_data)
            result_tables.append(pd.DataFrame(['|'] * combined_data.shape[0], columns=['|']))
    
            aggregate_data = Visualizer.aggregate_small_categories(column_data)
            aggregate_data[cat_column] = aggregate_data[cat_column].astype(str)
            
            fig = Visualizer.bar_plot(aggregate_data, 'count', cat_column, 
                                f'Распределение категорий в столбце {cat_column}', 'Количество', cat_column)
    
            return result_tables, fig
        else:
            return 'Не передана категория'
        

    def analyze_categorical(self, categorical_columns: list = None, unique_threshold=15, include_numeric=True) -> tuple:

        if not self.cat_cols or categorical_columns:
            self.set_cat_cols(categorical_columns, unique_threshold, include_numeric)
                
        if not self.cat_cols:
            return None, None, None
            
        unique_summary = []
        result_tables = []
        figs = []
    
        for column in self.cat_cols:
            
            result_table, fig = self.analyze_single_categorical(column)
            
            result_tables.extend(result_table)
            unique_summary.append([column, self.data[column].nunique()])
            figs.append(fig)
        
        final_unique_summary = pd.DataFrame(unique_summary, columns=['столбец', 'уникальные'])
        final_result_table = pd.concat(result_tables, axis=1).fillna('')
    
        return final_unique_summary, final_result_table, figs

    
    def analyze_extreme_values(self):

        lst = []
        
        for column in self.num_cols:

            q1 = self.data[column].quantile(0.25)
            q3 = self.data[column].quantile(0.75)
    
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
    
            outliers = self.data.loc[(self.data[column] < lower) | (self.data[column] > upper), column]
            pl = self.data.loc[(self.data[column] > upper), column].count()
            mn = self.data.loc[(self.data[column] < lower), column].count()
            part = outliers.count() / self.data.shape[0] * 100
    
            lst.append([column, outliers.count(), f'{part:.2f}%', mn, pl])
        
        df = pd.DataFrame(lst, columns=['Признак', 'Количество', 'Доля', 'Количество ниже порога', 'Количество выше порога'])
        
        return df
    

    def analyze_numerical(self, numerical_columns: list = None):

        if not self.num_cols or numerical_columns:
            self.set_num_cols(numerical_columns)

        if not self.num_cols:
            return None, None, None
            
        figs = []
        description = self.data[self.num_cols].describe()
        extrems = self.analyze_extreme_values()

        for column in self.num_cols:

            figs.append(Visualizer.hist_box_plot(df=self.data, title=f'Распределение значений признака {column}', 
                                     xlabel=column, ylabel='Количество'))
        
        return description, extrems, figs
        

    def analyze_single_time_series(self, time_column: str, value_column: str = None):

        if not value_column and (self.target_name or self.num_cols):
            value_column = self.target_name if self.target_name else self.num_cols[-1]
            time_df = self.data[[time_column, value_column]].sort_values(time_column)

        else:
            time_df = self.data.sort_values(time_column)
        
        info = time_df[time_column].describe()
        
        avg_delta = time_df[time_column].diff().mean()
    
        time_df = time_df if len(time_df) <= 2500 else time_df.iloc[::len(time_df)//2500]
        
        intervals, rounded = Visualizer.determine_time_granularity(time_df[time_column]) 
        
        if not intervals.empty:
            fig, ax = plt.subplots(figsize=(10, 4))
            sns.histplot(intervals, bins=min(40, len(intervals.unique())), ax=ax, kde=False)
            ax = Visualizer.configure_axis_labels(ax, 'Распределение интервалов между записями', f'Интервал ({rounded})', 'Частота')
            plt.grid(True, linestyle="--", alpha=0.5)
            plt.close(fig)
        else:
            fig = None

        if value_column:
            time_df['rolling_mean'] = time_df[value_column].rolling(window=len(time_df)//100, min_periods=2).mean()
            
            fig1, ax1 = plt.subplots(figsize=(12, 5))
            sns.lineplot(data=time_df, x=time_column, y=value_column, label='Исходные данные', ax=ax1, alpha=0.5, linewidth=1)
            sns.lineplot(data=time_df, x=time_column, y='rolling_mean', label='Скользящее среднее', ax=ax1, linewidth=2, color='red')
            ax1 = Visualizer.configure_axis_labels(ax1, 'Временной ряд с трендом', time_column, value_column)
            plt.legend()
            plt.grid(True, linestyle="--", alpha=0.5)
            plt.tight_layout()
            plt.close(fig)
        else:
            fig1 = None

        return info, avg_delta, fig, fig1

    def analyze_time_series(self, time_columns: list = None, target_value: str = None):

        if not self.time_cols or time_columns:
            self.set_time_cols(time_columns)

        if not self.time_cols:
            return None, None, None
            
        columns_describe = self.data[self.time_cols].describe()
        avg_deltas = []
        intervals = []
        rolling_means = []
        
        for time_column in self.time_cols:
            info, avg_delta, fig1, fig2 = self.analyze_single_time_series(time_column, target_value)
            
            avg_deltas.append(avg_delta)
            intervals.append(fig1)
            rolling_means.append(fig2)

        return columns_describe, avg_deltas, intervals, rolling_means

