import pandas as pd

def convert_file_to_23():
	#filepath
	input_filepath = input("Filepath to raw data:").strip()
	try:
		#read the file
		df = pd.read_csv(input_filepath, sep=r's+'')
	except FileNotFoundError:
		print(\n["Error"])
		return
	except Exception as e:
        print(f"\n[Error] An error occurred while reading the file: {e}")
        return