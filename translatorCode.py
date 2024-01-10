import pandas as pd
from googletrans import Translator
import time

def translate_excel(file_path):
    start_time = time.time()

    
    df = pd.read_excel(file_path, header=None)

    
    translator = Translator()

    
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            df.at[i, j] = translator.translate(str(df.at[i, j]), dest='en').text

   
    df.to_excel('Translated_Order_Sheet.xlsx', index=False, header=False)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Translation and save completed in {elapsed_time:.2f} seconds.")

translate_excel('OrderExport.xls')
