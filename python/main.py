from country_builder import CountryBuilder
from game_builder import GameBuilder
from event_builder import EventBuilder
from medal_builder import MedalBuilder
from team_builder import TeamBuilder
from coach_builder import CoachBuilder
from athletes_builder import AthletesBuilder

import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../olympics/")

# todo improve the load of files
input_file_path = path
output_file_path = path+'/output/'

# Note! The order of execution matters!

countryBuilder = CountryBuilder()
countryBuilder.build(input_file_path, output_file_path)

gameBuilder = GameBuilder()
gameBuilder.build(input_file_path, output_file_path)

eventBuilder = EventBuilder()
eventBuilder.build(input_file_path, output_file_path)

medalBuilder = MedalBuilder()
medalBuilder.build(input_file_path, output_file_path)

teamBuilder = TeamBuilder()
teamBuilder.build(input_file_path, output_file_path)

coachTeam = CoachBuilder()
coachTeam.build(input_file_path, output_file_path)

athletesBuilder = AthletesBuilder()
athletesBuilder.build(input_file_path, output_file_path)

print("Process done!")