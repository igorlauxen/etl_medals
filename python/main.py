import pandas as pd
from country_builder import CountryBuilder

input_file_path = '/Users/i841640/Documents/unisinos/big_data_etl/etl_medals/olympics/'
output_file_path = '/Users/i841640/Documents/unisinos/big_data_etl/etl_medals/olympics/output/'

countryBuilder = CountryBuilder()
countryBuilder.build(input_file_path, output_file_path)
