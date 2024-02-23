import sqlite3
import cachetools

cache = cachetools.TTLCache(maxsize=100, ttl=5)  # Cache up to 100 items for 5 seconds
class Select:

    def instrument_multiplier(instrument_name):
        @cachetools.cached(cache)
        def retrieve_multiplier(instrument_name):
            multiplier = None
            with sqlite3.connect("INSTRUMENTSDB.db") as connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("SELECT MULTIPLIER FROM INSTRUMENT_PRICE_MODIFIER WHERE NAME = ?", (instrument_name,))
                    row = cursor.fetchone()                    
                    if row:
                        multiplier = row[0]
                    return multiplier
                except sqlite3.Error as e:
                    raise RuntimeError(f"Database error: {e}") from e
                finally:
                    cursor.close()
        return retrieve_multiplier(instrument_name)
    
    
    
    
    

       

