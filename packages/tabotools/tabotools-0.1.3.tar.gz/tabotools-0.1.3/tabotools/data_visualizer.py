import io
from IPython.display import HTML

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')


class Visualizer:

    TITLE_SIZE = 18

    @staticmethod
    def show_title(title: str, title_size=16, return_html=False):
        
        content = f"<br><p style='font-weight:bold; font-size: {title_size}px;'>{title}</p>"
    
        if return_html:
            return content
            
        display(HTML(content))
        return None     

    
    @staticmethod
    def show_info(df: pd.DataFrame, name: str, path: str, return_html=False):

        content = Visualizer.show_title(name,  title_size=20, return_html=True)
        content += f'<p>Файл по пути {path} был успешно загружен.</p>'
        content += Visualizer.show_title('Общие сведения:', return_html=True)

        buffer = io.StringIO()
        df.info(buf=buffer)
        info = buffer.getvalue()[1:].replace('\n', '<br>')

        content += f'<pre>{info}</pre>'
        content += Visualizer.show_title('Фрагмент датафрейма:', return_html=True)
        content += df.sample(min(5, df.shape[0])).to_html()

        if return_html:
            return content

        display(HTML(content))
        return None

    
    @staticmethod
    def preview_data(df: pd.DataFrame, row_limit=15) -> pd.DataFrame:
        
        if df.shape[0] <= row_limit:

            return df
        
        preview_df = pd.concat(
            [
                df.head(row_limit - row_limit//3),
                pd.DataFrame([['...']*df.shape[1]], columns=df.columns),
                df.tail(row_limit//3)
            ],
            ignore_index=True
        )
            
        return preview_df
        

    @staticmethod
    def aggregate_small_categories(df: pd.DataFrame, row_limit = 5) -> pd.DataFrame:

        if df.shape[0] <= row_limit + 1:
            return df
            
        columns = df.columns 
        
        summary_row = ['Other']
        summary_row.extend(df[columns[1:]].iloc[row_limit:].sum().to_list())
        
        aggregated_df = pd.concat(
            [
                df.head(row_limit),
                pd.DataFrame([summary_row], columns=columns)
            ], 
            ignore_index=True
        )

        return aggregated_df


    @staticmethod
    def determine_time_granularity(time_series: pd.Series) -> tuple:
        
        deltas = time_series.sort_values().diff().dropna().dt.total_seconds()
        round_to = None
        
        if deltas.empty:
            return None, None
    
        mode_delta = deltas.mode()[0] if len(deltas) > 1 else deltas.median()
        
        
        if mode_delta < (minute := 60):
            return deltas, 'секунда'
            
        elif mode_delta < (hour := minute**2):
            deltas /=  minute
            round_to='минута'
            
        elif mode_delta < (day := 24*hour):
            deltas /= hour
            round_to='час'
            
        elif mode_delta < (week := 7*day):
            deltas /= day
            round_to='день'
            
        elif mode_delta < (month := 30*day):
            deltas /= week
            round_to='неделя'
            
        elif mode_delta < (year := 365*day):
            deltas /= month
            round_to='месяц'
            
        else:
            deltas /= year
            round_to='год'

        return deltas, round_to
    
    @staticmethod
    def configure_axis_labels(ax, title: str, xlabel: str, ylabel: str, title_size: int = 16, x_size: int = 12, y_size: int = 12):

        ax.set_title(title, size=title_size)
        ax.set_xlabel(xlabel, size=x_size)
        ax.set_ylabel(ylabel, size=y_size)

        return None
 
    @staticmethod
    def annotate(ax, kind: int = 2) -> None:
        
        if kind == 1:
            for p in ax.patches:
               
                ax.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2),
                            ha='left', va='center', fontsize=10, xytext=(5, 0), textcoords='offset points')
    
        elif kind == 2:
            for p in ax.patches:
               
                ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                            ha='center', va='bottom', fontsize=8, xytext=(0, 10), textcoords='offset points')

        return None

    @staticmethod
    def bar_plot(df: pd.DataFrame, x: str, y: str, title, xlabel, ylabel, size: tuple = (10, 4)):

        fig, ax = plt.subplots(figsize=size)
        sns.barplot(data=df, y=y, x=x, hue=y, ax=ax, palette='viridis', legend=False)

        Visualizer.annotate(ax, kind=1)
        Visualizer.configure_axis_labels(ax, title, xlabel, ylabel)
        plt.close(fig)

        return fig

    @staticmethod
    def hist_box_plot(df: pd.DataFrame, title: str, xlabel: str, ylabel: str, kind: int=3):
        
        fig, (ax_box, ax_count) = plt.subplots(2, figsize=(14,8), sharex = True, 
                                               gridspec_kw = {'height_ratios': (.1, .9)})
    
        sns.boxplot(x=df[xlabel], ax=ax_box,
                     color='#8F94FB')

        sns.histplot(data=df[xlabel], ax=ax_count,
                     color='#7F7FD5', alpha=0.3, kde=True)
        
        ax_count.axvline(x=df[xlabel].mean(), color='#5B5BB7', linestyle='-', label='среднее значение')
        ax_count.axvline(x=df[xlabel].median(), color='#7F7FD5', linestyle='--', label='медиана')
        
        ax_count.legend()
        Visualizer.configure_axis_labels(ax_box, title, '', '')
        Visualizer.configure_axis_labels(ax_count, '', xlabel, ylabel)
        
        if kind == 2:
            Visualizer.annotate(ax_count, kind=kind)

        plt.close(fig)
        
        return fig
