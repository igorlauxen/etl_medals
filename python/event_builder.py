import pandas as pd
import csv  
import math

athletes_file_name = 'Teams.xlsx'
files_output = 'Eventos.csv'

header = ['id', 'nome'];

class EventBuilder:
    
    def build(self, input_file_path, output_file_path):

      data = pd.read_excel (input_file_path+athletes_file_name)
      event_df = pd.DataFrame(data, columns= ['Event'])
      eventos_df = pd.DataFrame({'id': [], 'nome': []})
      print (event_df.iterrows())
      count = 1
      with open(output_file_path+files_output, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in event_df.iterrows():
          # DataFrame.insert(loc, column, value, allow_duplicates=False)
          # row is a mapping 1 is the index of dataframe in loop and 0 is the value
          event_name = row[1][0]
          queryDf =  eventos_df[eventos_df["nome"] == event_name]
          if queryDf.empty == True:
            print("Creating row for event with name " + event_name)
            eventos_df = eventos_df.append({'id': count, 'nome': event_name}, ignore_index = True)
            count = count + 1
            writer.writerow([count, event_name])
        