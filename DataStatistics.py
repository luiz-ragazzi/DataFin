import pandas as pd

class DataStatistics:   
    def __init__(self, name):
        self.name = name
        self.data_chunks = []
        self.statistics = {}

    def process_chunk(self, chunk):
        if not chunk.empty:
            self.statistics.update({
                'mean': chunk['price'].mean(),
                'standard_deviation': chunk['price'].std(),
                'max': chunk['price'].max(),
                'min': chunk['price'].min(),
                'count': len(chunk)
            })

    def calculate_statistics(self):
       
        if self.data_chunks:
            
            filtered_chunks = [chunk for chunk in self.data_chunks if not chunk.empty]
            if filtered_chunks:
                combined_prices = pd.concat([chunk['price'] for chunk in filtered_chunks])

                self.statistics = {
                    'mean': combined_prices.mean(),
                    'standard_deviation': combined_prices.std(),
                    'max': combined_prices.max(),
                    'min': combined_prices.min(),
                    'count': len(combined_prices)
                }
            else:                
                raise RuntimeError(f"Warning: No valid data found for name '{self.name}'")

    def get_statistics(self):        
        if self.statistics:
            return self.statistics
        else:
            return f"No statistics calculated for name '{self.name}'"