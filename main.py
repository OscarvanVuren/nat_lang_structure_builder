from mp_api.client import MPRester
import os

from read_input import get_structs, parse_struct
from matProj_interface import get_matIDs, get_structure_from_id

# check for api keys
#if "MP_API_KEY" or "GEMINI_API_KEY" not in os.environ:
#    print("API keys not found")
#    exit()
#print("API keys found")

# get structure as properties

structure=get_structs(inp_fname="../test_mats.txt")

properties=parse_struct(structure)
print(properties)

# search materials project for matching material IDs
ids=get_matIDs(properties)

list_ids=[]
for mat in ids:
    list_ids.append(mat.material_id)
    #print(mat.material_id)

st=get_structure_from_id(list_ids)
test_struct=st[0]

test_struct.to(filename="Al2O3.cif")

#with open("test.txt","w") as f:
#    f.write(test_struct)