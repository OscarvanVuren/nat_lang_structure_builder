def nat_lang_inputs(textFile=None,max_matches=5):
    """
    Main routine for natural language parser
    textfile: str, filename of text file containing material descriptions
    
    """
    
    from read_input import get_structs, parse_struct
    from matProj_interface import get_matIDs, get_structure_from_id
    from write_outputs import output_cif
    
    structures=get_structs(inp_fname=textFile)
    
    for structure in structures:
        print(f"Operating on structure {structure}")
        properties=parse_struct(structure)
        print(properties)
        
        # search materials project for matching material IDs
        ids=get_matIDs(properties)
        
        list_ids=[]
        for mat in ids:
            list_ids.append(mat.material_id)
            
        print("Materials Project IDs matching query \n", list_ids)
        # stop for too many matches
        if len(list_ids)>max_matches:
            print(f"Number of matched materials selected is greater than the threshold set of {max_matches} \n",
                  f"Consider making your query more specific or increasing max_matches.")
            exit()

    
        for matprID in list_ids:
            st=get_structure_from_id([matprID])
            test_struct=st[0]
            output_cif(test_struct, properties["formula"],tags=matprID)
            