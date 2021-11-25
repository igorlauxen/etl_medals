import pandas as pd
import csv  

medals_file_name = 'Medals.xlsx'
file_output = 'Medalhas.csv'

paises_file_name = 'Paises.csv'

header = ['id','rank', 'pais_id', 'ouro', 'prata', 'bronze', 'total', 'rank_total'];

class MedalBuilder:
    
    def build(self, input_file_path, output_file_path):
      paises_df = pd.read_csv(output_file_path+paises_file_name)

      data = pd.read_excel(input_file_path+medals_file_name)
      medals_df = pd.DataFrame(data, columns= ['Rank', 'Team/NOC', 'Gold', 'Silver',	'Bronze',	'Total',	'Rank by Total'])
      print (medals_df.iterrows())
      count = 1
      with open(output_file_path+file_output, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in medals_df.iterrows():
          line_data = row[1]
          country_name = line_data[1]
          country_entity =  paises_df[paises_df["nome"] == country_name]
          country_id = 0
          country_id = country_entity.id.values[0]
          writer.writerow([
            count,
            line_data[0],
            country_id,
            line_data[2],
            line_data[3],
            line_data[4],
            line_data[5],
            line_data[6]
          ])
          count = count + 1
        