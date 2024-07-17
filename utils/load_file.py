import json

def load_data(a:str)->dict:
	with open (a,'r') as jsonfile:
		load_data=json.load(jsonfile)

	print('file has been successfuly read')
	return load_data

#print(load_data)