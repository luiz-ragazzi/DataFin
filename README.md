# DataFin Analyzer
This Python application processes a text file containing financial instrument data to perform comprehensive statistical analyses. It efficiently reads and analyzes the data, providing insightful statistical calculations

## Technologies
* Python (Pandas, cachetools)
* Sqllite3

## Using the APP
The Database file and the input example text (instruments.txt) are included in the project.

1. Clone the repository:
   ```sh
   git clone https://github.com/luiz-ragazzi/code_test.git
   cd code_test
   
2. Make sure to install the Python packages:
   ```sh
    pip install -r requirements.txt
3. Run `main.py`:
    ```sh
   python main.py
4. To run tests:
   ```sh
   pytest
   
## Explanation of `process_data` Function
  Process instrument data, calculate statistics, and return statistics results as a dictionary.
  
  Parameters:
  - instrument_name (str): Name of the instrument to process.
  - year (int): Year to filter by (optional).
  - month (int): Month to filter by (optional).
  
  Returns:
  - dict: Dictionary containing calculated statistics.


1. Example usage:
   ```sh
   # Initialize InstrumentProcessor
    processor = InstrumentProcessor("path/to/data.csv")
    
    # Process data for instrument "INSTRUMENT1" for the year 2014
    stats = processor.process_data("INSTRUMENT1", year=2014)
    print(stats)


## Function Breakdown

1. **Initializes a `DataStatistics` object**:
   - Creates a `DataStatistics` object, likely to calculate and store statistics for the specified instrument.

2. **Retrieves instrument multiplier**:
   - Fetches a potential multiplier value for the instrument from the `Select` class.
   - This multiplier might be used to adjust prices for consistency.

3. **Iterates through data chunks**:
   - Reads the data file in chunks using `pandas.read_csv`.
   - Processes each chunk as follows:
     - Filters columns to those specified in `self.columns`.
     - Formats dates using `self.set_date_format`.
     - Filters data based on instrument name, year, and month.
     - Applies the multiplier to prices, if available.
     - Sends the filtered and processed chunk to the `statistics_calculator` for analysis.

4. **Calculates final statistics**:
   - Calls `calculate_statistics` on the `statistics_calculator` to finalize calculations.

5. **Returns statistics**:
   - Retrieves the calculated statistics using `get_statistics` and returns them.
