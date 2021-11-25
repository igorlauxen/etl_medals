import pandas as pd
import csv  

team_file_name = 'Athletes.xlsx'
file_output = 'Atletas.csv'

paises_file_name = 'Paises.csv'
jogos_file_name = 'Jogos.csv'

header = ['id','nome', 'jogo_id', 'pais_id'];

class AthletesBuilder:
    
    def build(self, input_file_path, output_file_path):
      paises_df = pd.read_csv(output_file_path+paises_file_name)
      jogos_df = pd.read_csv(output_file_path+jogos_file_name)

      data = pd.read_excel(input_file_path+team_file_name)
      athletes_df = pd.DataFrame(data, columns= ['Name', 'Discipline', 'NOC'])
      print (athletes_df.iterrows())
      count = 1
      with open(output_file_path+file_output, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in athletes_df.iterrows():
          line_data = row[1]
          
          game_id = 0
          country_id = 0

          game_name = line_data[1]
          game_entity =  jogos_df[jogos_df["nome"] == game_name]
          game_id = game_entity.id.values[0]

          country_name = line_data[2]
          country_entity =  paises_df[paises_df["nome"] == country_name]
          country_id = country_entity.id.values[0]

          writer.writerow([
            count,
            line_data[0],
            game_id,
            country_id
          ])
          count = count + 1
        