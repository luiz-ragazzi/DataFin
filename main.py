from processor import InstrumentProcessor
from select_db import Select

'''
the instrument_multiplier queries the Database to see if there is a multiplier
for an instrument, returns the multiplier value or None

''' 
multiplier = Select.instrument_multiplier('INSTRUMENT1')
print(multiplier)


'''
the process_data process statistics functions
arguments: instrument_name, year, month

''' 
instrument_name = 'INSTRUMENT2'
processor = InstrumentProcessor("instruments.txt")
result = processor.process_data(instrument_name, year=2014, month=11)
print('Statistics for instrument: ' + instrument_name)
print(result)
