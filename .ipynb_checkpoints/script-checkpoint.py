from utils.load_file import load_data
from utils.get_figures_number import *
from utils.get_alpha import *
from utils.get_beta import *
from utils.get_gamma import *
from utils.get_surface_area import *
from utils.get_volume import *
from utils.get_radius_described_sphere import *
from utils.get_volume_described_sphere import *



#from utils import *

print('Project Paralellogram is started! ')
fig_dic = {} #dictionary of read file
fig_num = 0 #figures number in dict file
fig_sides = [] # a b c sids of paralellepiped


fig_dic = load_data('parallelepipeds.json')
fig_num = get_figures_number(fig_dic)

print(fig_num) #print number of figures!
 
for i in fig_dic.values():
	#print(list(i.values()))
	fig_sides.append(list(i.values()))

print(fig_sides[0])