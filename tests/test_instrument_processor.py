import pandas as pd
from processor import InstrumentProcessor
import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def sample_df():
    data = {'date': ['01-Jan-2024', '02-Jan-2024', '04-Feb-2024', '05-Feb-2024', '25-Dec-2024']}
    return pd.DataFrame(data)

def test_set_date_format(sample_df):
    intrument_processor = InstrumentProcessor('')
    result_df = intrument_processor.set_date_format(sample_df.copy())

    assert isinstance(result_df, pd.DataFrame)
    assert result_df.shape == (4, 2)  # Only weekdays should be included
    assert result_df['date'].dtype == 'datetime64[ns]'
    assert all(result_df['IsWeekDay'] == True)
    assert result_df['date'].min() >= pd.to_datetime('2024-01-01')



def test_process_mean_instrument2():
    processor = InstrumentProcessor("instruments.txt")
    result = processor.process_data('INSTRUMENT2', year=2014, month=11)
    mean = float("{:.2f}".format(result['mean']))
    assert mean == 9.26

def test_process_mean_instrument1():
    processor = InstrumentProcessor("instruments.txt")
    result = processor.process_data('INSTRUMENT1')
    mean = float("{:.2f}".format(result['mean']))
    assert mean == 3.37


def test_process_mean_instrument3():
    processor = InstrumentProcessor("instruments.txt")
    result = processor.process_data('INSTRUMENT3')
    mean = float("{:.2f}".format(result['mean']))
    assert mean == 109.71