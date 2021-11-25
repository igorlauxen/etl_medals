import pandas as pd
import csv  

file_path = '/Users/i841640/Documents/unisinos/big_data_etl/etl_medals/olympics/'
athletes_file_name = 'Athletes.xlsx'
output_file_path = '/Users/i841640/Documents/unisinos/big_data_etl/etl_medals/olympics/output/'
paises_output = 'Paises.csv'

header = ['id', 'nome'];

class CountryBuilder:
    
    def build(self, input_file_path, output_file_path):

      data = pd.read_excel (input_file_path+athletes_file_name)
      country_df = pd.DataFrame(data, columns= ['NOC'])
      paises_df = pd.DataFrame({'id': [], 'nome': []})
      print (country_df.iterrows())
      count = 1
      with open(output_file_path+paises_output, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in country_df.iterrows():
          # DataFrame.insert(loc, column, value, allow_duplicates=False)
          # row is a mapping 1 is the index of dataframe in loop and 0 is the value
          country_name = row[1][0]
          duplication =  paises_df[paises_df["nome"] == country_name]
          if duplication.index.to_list() == []:
            print("Creating row for country with name " + country_name)
            paises_df = paises_df.append({'id': count, 'nome': country_name}, ignore_index = True)
            count = count + 1
            writer.writerow([count, country_name])
        