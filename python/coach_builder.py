import pandas as pd
import csv  

team_file_name = 'Coaches.xlsx'
file_output = 'Treinadores.csv'

paises_file_name = 'Paises.csv'
jogos_file_name = 'Jogos.csv'
eventos_file_name = 'Eventos.csv'

header = ['id','nome', 'nome_anterior' 'jogo_id', 'pais_id', 'event_id'];

class CoachBuilder:
    
    def build(self, input_file_path, output_file_path):
      paises_df = pd.read_csv(output_file_path+paises_file_name)
      jogos_df = pd.read_csv(output_file_path+jogos_file_name)
      eventos_df = pd.read_csv(output_file_path+eventos_file_name)

      data = pd.read_excel(input_file_path+team_file_name)

      coaches_df = pd.DataFrame(data, columns= ['Name', 'Discipline', 'NOC', 'Event'])
      added_coaches_df = pd.DataFrame(None, columns= ['Name', 'Discipline', 'NOC', 'Event'])
      print (coaches_df.iterrows())
      count = 1
      with open(output_file_path+file_output, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in coaches_df.iterrows():
          line_data = row[1]
          game_id = 0
          country_id = 0
          event_id = 0

          coach_name = line_data[0]

          game_name = line_data[1]
          game_entity =  jogos_df[jogos_df["nome"] == game_name]
          game_id = game_entity.id.values[0]

          country_name = line_data[2]
          country_entity =  paises_df[paises_df["nome"] == country_name]
          country_id = country_entity.id.values[0]

          event_name = line_data[3]
          
          event_entity =  eventos_df[eventos_df["nome"] == event_name]
          if pd.isna(event_name) == False and event_entity.empty == False:
            event_id = event_entity.id.values[0]

          previous_coach_name = ""
          previous_coach = added_coaches_df[(added_coaches_df["Discipline"] == game_name) | (added_coaches_df["NOC"] == country_name) | (added_coaches_df["Event"] == event_name)]
          if not previous_coach.empty:
            previous_coach_name = previous_coach.Name.values[0]
          writer.writerow([
            count,
            coach_name,
            previous_coach_name,
            game_id,
            country_id,
            event_id
          ])
          count = count + 1

          added_coaches_df = added_coaches_df.append(row[1])
        