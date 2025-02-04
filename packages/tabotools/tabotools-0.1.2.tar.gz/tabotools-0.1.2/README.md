# TaboTools

TaboTools is a Python library designed to streamline data processing workflows, including file loading, data preprocessing, exploratory analysis, and visualization. This package provides a set of tools to simplify the tasks of cleaning, analyzing, and visualizing your data.

## Features

- **File Loading:** Automatically loads data from various file formats.
- **Data Preprocessing:** Checks data types, detects full and implicit duplicates, and processes date columns.
- **Exploratory Data Analysis:** Provides quick statistical insights and analysis of different feature types.
- **Data Visualization:** Generates customizable visualizations to aid in data understanding.

## Installation

You can install TaboTools directly from PyPI:

```bash
pip install tabotools
```

## Usage

Below is an example of how to use the DataProcessor class provided by TaboTools. In this example, we initialize the processor with an abstract file path and specify which columns should be parsed as dates.

```python
from tabotools import DataProcessor

# Initialize the DataProcessor with a generic data file and a list of date columns.
data_processor = DataProcessor(
    file_path='data/sample_data.csv',
    parse_dates=['created_at', 'updated_at', 'published_at']
)

# Run data preprocessing: this method checks data types and identifies duplicate records.
data_processor.data_preprocessor()

# Perform exploratory data analysis by specifying the target feature.
data_processor.eda(target_value='sale_price')

# Display dataset information including:
# - File path and source
# - DataFrame name or identifier
# - Lists of categorical, numerical, and time columns
# - The designated target feature
data_processor.info()
```
## Dependencies

TaboTools requires the following libraries:

- Python
- pandas
- matplotlib
- seaborn
- IPython

## Contributing

Contributions to TaboTools are welcome! If you have any suggestions, bug fixes, or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
