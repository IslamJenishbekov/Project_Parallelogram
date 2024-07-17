import json

def set_write_file (dict_:dict)->bool:

	file_to_write = json.dumps(dict_, indent = 4)

	with open('characteristics.json','w') as outfile:
		outfile.write(file_to_write)

	print("json file is successfully created!")

	return 0