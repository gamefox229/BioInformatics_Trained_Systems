import pandas as pd

def convert_file_to_23():
	#filepath
	input_filepath = input("Filepath to raw data:").strip()
	try:
		#read the file
		df = pd.read_csv(input_filepath, sep=r's+'')
	except FileNotFoundError:
		print("file not found")
		return
	except Exception as e:
        print(f"\n[Error]")
        return
	#23andMeHeaders
	output_lines = [
		"# 23andMe-compatible format generated from raw data file",
		"# rsid\tchromosome\tposition\tgenotype"
		]