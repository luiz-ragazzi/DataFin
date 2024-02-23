import pandas as pd
from DataStatistics import DataStatistics
from select_db import Select

class InstrumentProcessor:
   

    def __init__(self, data_path, chunk_size=50_000):
        self.columns = ['name', 'date', 'price']
        self.data_path = data_path
        self.chunk_size = chunk_size
        self.stats_per_chunk = []

    
    def set_date_format(self, df):
        df['date'] = pd.to_datetime(df['date'], format="%d-%b-%Y")
        df = self._filter_weekdays(df)
        return df

    def _filter_weekdays(self, df):
        df['IsWeekDay'] = df['date'].dt.weekday < 5
        return df[df['IsWeekDay'] == True]



    def filter_data(self, data, instrument_name, year=None, month=None):
        data = data.copy()
        data = data[data["name"] == instrument_name]
        if year:
            data = data[data["date"].dt.year == year]
        if month:
            data = data[data["date"].dt.month == month]
        return data    

    def process_data(self, instrument_name, year=None, month=None):        

        statistics_calculator = DataStatistics(instrument_name)
        multplier = Select.instrument_multiplier(instrument_name)

        for chunk in pd.read_csv(self.data_path, names=self.columns, chunksize=self.chunk_size):
            data_filtered = chunk[self.columns]
            data_filtered = self.set_date_format(data_filtered)
            data_filtered = self.filter_data(data_filtered, instrument_name, year, month) 
            if multplier is not None:
                data_filtered['price'] = data_filtered['price'].apply(lambda x: x * multplier)

            statistics_calculator.process_chunk(data_filtered)         
            
        statistics_calculator.calculate_statistics()
        return statistics_calculator.get_statistics()
           



