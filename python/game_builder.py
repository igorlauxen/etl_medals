import pandas as pd
import csv  

file_path = '/Users/i841640/Documents/unisinos/big_data_etl/etl_medals/olympics/'
athletes_file_name = 'Athletes.xlsx'
output_file_path = '/Users/i841640/Documents/unisinos/big_data_etl/etl_medals/olympics/output/'
paises_output = 'Jogos.csv'

header = ['id', 'nome'];

class GameBuilder:
    
    def build(self, input_file_path, output_file_path):

      data = pd.read_excel (input_file_path+athletes_file_name)
      game_df = pd.DataFrame(data, columns= ['Discipline'])
      jogos_df = pd.DataFrame({'id': [], 'nome': []})
      print (game_df.iterrows())
      count = 1
      with open(output_file_path+paises_output, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in game_df.iterrows():
          # DataFrame.insert(loc, column, value, allow_duplicates=False)
          # row is a mapping 1 is the index of dataframe in loop and 0 is the value
          game_name = row[1][0]
          duplication =  jogos_df[jogos_df["nome"] == game_name]
          if duplication.index.to_list() == []:
            print("Creating row for game with name " + game_name)
            jogos_df = jogos_df.append({'id': count, 'nome': game_name}, ignore_index = True)
            count = count + 1
            writer.writerow([count, game_name])
        