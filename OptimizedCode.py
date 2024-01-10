from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from googletrans import Translator
import time

def translate_cell(cell):
    # Initialize Google Translator within the function
    translator = Translator()
    return translator.translate(str(cell), dest='en').text

def translate_excel(file_path):
    start_time = time.time()

    # Read the existing file
    df = pd.read_excel(file_path, header=None)

    # Translate all rows and columns in parallel
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(translate_cell, cell) for cell in df.values.flatten()]
        translated_cells = [future.result() for future in futures]

    # Reshape the translated data back to the original shape
    df_translated = pd.DataFrame(translated_cells).values.reshape(df.shape)

    # Save the translated DataFrame back to Excel
    pd.DataFrame(df_translated).to_excel('Translated_Order_Sheet.xlsx', index=False, header=False)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Translation and save completed in {elapsed_time:.2f} seconds.")

# Replace 'Order_Sheet.xls' with your actual file path
translate_excel('OrderExport.xls')
