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
#from math import pi

def get_characs(dict_:dict)->dict:
	sides_list = [] #sides of parallelepiped
	res_dict = {} #result dictionary	
	counter = 1

	#taking out sides to work easier
	for i in dict_.values():
		#print(list(i.values()))
		sides_list.append(list(i.values()))

	for sides in sides_list:
		a= float(sides[0])
		b= float(sides[1])
		c= float(sides[2])
		diag = get_diag(a,b,c)
		volume = get_volume(a,b,c)
		surface_area = get_surface_area(a,b,c)
		radius_sphere = get_radius_described_sphere(diag)
		sphere_volume = get_volume_described_sphere(radius_sphere)
		alpha = get_alpha(a,diag)
		beta = get_beta(b,diag)
		gamma = get_gamma(c,diag)

		res_dict['figure_'+str(counter)] = {"diag": str(diag),"volume": str(volume),"surface_area":str(surface_area),"alpha": str(alpha),"beta": str(beta),"gamma": str(gamma),"radius_described_sphere":str(radius_sphere),"volume_described_sphere":str(sphere_volume)}
		counter = counter + 1
	return res_dict
