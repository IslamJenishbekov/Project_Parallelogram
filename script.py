from utils.load_file import load_data
from utils.get_figures_number import *
from utils.get_alpha import *
from utils.get_beta import *
from utils.get_gamma import *
from utils.get_surface_area import *
from utils.get_volume import *
from utils.get_radius_described_sphere import *
from utils.get_volume_described_sphere import *
from utils.get_diag import *
from utils.characs import *
from utils.write_file import *
from utils.printing_first import *
import json

#start of program
print('Project Paralellogram is started! ')
print(get_printing_first())

fig_dic = {} #dictionary of read file
fig_num = 0 #figures number in dict file


fig_dic = load_data('parallelepipeds.json') #load json dictionary from file
fig_num = get_figures_number(fig_dic)



characteristics = get_characs(fig_dic) #Making dictionary.
	#print(characteristics)

print(set_write_file(characteristics)) #wrtie calculated json to file.

#part2

pars = load_data("characteristics.json")
labels = ["avg_diag",
          "avg_volume",
          "avg_surface_area",
          "avg_alpha",
          "avg_beta",
          "avg_gamma",
          "avg_radius_described_sphere",
          "avg_volume_described_sphere"]
pars_count = len(pars)
sum_features = [0 for i in range(8)]

for key, value in pars.items():
    sum_features[0] += float(value["diag"])
    sum_features[1] += float(value["volume"])
    sum_features[2] += float(value["surface_area"])
    sum_features[3] += float(value["alpha"])
    sum_features[4] += float(value["beta"])
    sum_features[5] += float(value["gamma"])
    sum_features[6] += float(value["radius_described_sphere"])
    sum_features[7] += float(value["volume_described_sphere"])

for i in range(8):
    sum_features[i] /= pars_count

res = {i : j for i, j in zip(labels, sum_features)}

file = json.dumps(res, indent=4)

with open('statistics.json', 'w') as outfile:
    outfile.write(file)



#end of program
print('End of program')