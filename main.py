# Main routine for natural language parser

def nat_lang_inputs(textFile=None):
    
    from mp_api.client import MPRester
    import os
    
    from read_input import get_structs, parse_struct
    from matProj_interface import get_matIDs, get_structure_from_id
    from write_outputs import output_cif
    
    # check for api keys
    #if "MP_API_KEY" or "GEMINI_API_KEY" not in os.environ:
    #    print("API keys not found")
    #    exit()
    #print("API keys found")
    
    # get structure as properties
    
    structure=get_structs(inp_fname=textFile)
    
    properties=parse_struct(structure)
    print(properties)
    
    # search materials project for matching material IDs
    ids=get_matIDs(properties)
    
    list_ids=[]
    for mat in ids:
        list_ids.append(mat.material_id)
        
    print("Materials Project IDs matching query \n", list_ids)

    for matprID in list_ids:
        st=get_structure_from_id([matprID])
        test_struct=st[0]
        output_cif(test_struct, properties["formula"],tags=matprID)


    #st=get_structure_from_id(list_ids)
    #print(st)
    #test_struct=st[0]
    
    #output_cif(test_struct, properties["formula"])
    
    #with open("test.txt","w") as f:
    #    f.write(test_struct)