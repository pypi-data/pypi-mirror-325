import pandas as pd
from difflib import SequenceMatcher

pd.set_option('display.max_columns', None)  

class DataPreprocessor():

    def __init__(self, data: pd.DataFrame, name: str = None):
        self.data = data
        self.name = name

    
    def check_types(self) -> pd.DataFrame:
        data_types = pd.DataFrame(self.data.dtypes).reset_index()
        data_types.columns = ['Признак', 'Тип']
        
        return data_types

    
    def get_missing_info(self) -> pd.DataFrame:
        missing_info = self.data.isna().sum()[self.data.isna().sum()>0].reset_index()
        missing_info['доля, %'] = round(self.data.isna().mean()[self.data.isna().sum()>0]*100, 2).reset_index()[0]
        missing_info = missing_info.rename(columns={'index': 'столбец', 0: 'количество'})
    
        return missing_info.sort_values(by='доля, %', ascending=False).reset_index(drop=True)

    
    def get_duplicates_info(self) -> tuple:
        duplicates = self.data.duplicated()
        
        count = duplicates.sum()
        part = duplicates.mean()
        sample = self.data[duplicates].head()
            
        return count, part, sample


    def find_fuzzy_duplicates(self, threshold=0.8, string_columns=None):
        
        if string_columns is None:
            string_columns = self.data.select_dtypes(include=['object', 'category']).columns.tolist()
    
        fuzzy_duplicates = {}
    
        for column in string_columns:
            unique_values = self.data[column].dropna().unique()

            if len(unique_values) < 100:
                similar_pairs = []
        
                for i, value1 in enumerate(unique_values):
                    for j, value2 in enumerate(unique_values):
                        if i >= j:  
                            continue
                        
                        similarity = SequenceMatcher(None, str(value1), str(value2)).ratio()
                        
                        if similarity >= threshold or value1.lower() == value2.lower():
                            similar_pairs.append((value1, value2, similarity))
        
                if similar_pairs:
                    fuzzy_duplicates[column] = pd.DataFrame(
                        similar_pairs, columns=['Value 1', 'Value 2', 'Similarity']
                    ).sort_values(by='Similarity', ascending=False)
    
        return fuzzy_duplicates

   