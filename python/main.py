import pandas as pd
from country_builder import CountryBuilder
from game_builder import GameBuilder
from event_builder import EventBuilder
from medal_builder import MedalBuilder
from team_builder import TeamBuilder

input_file_path = '/Users/i841640/Documents/unisinos/big_data_etl/etl_medals/olympics/'
output_file_path = '/Users/i841640/Documents/unisinos/big_data_etl/etl_medals/olympics/output/'

# Note! The order of execution matters!

countryBuilder = CountryBuilder()
#countryBuilder.build(input_file_path, output_file_path)

gameBuilder = GameBuilder()
#gameBuilder.build(input_file_path, output_file_path)

eventBuilder = EventBuilder()
eventBuilder.build(input_file_path, output_file_path)

medalBuilder = MedalBuilder()
#medalBuilder.build(input_file_path, output_file_path)

teamBuilder = TeamBuilder()
teamBuilder.build(input_file_path, output_file_path)