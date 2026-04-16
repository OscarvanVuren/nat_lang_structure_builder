def get_structs(userinp=True, inp_fname=None):
    """
    Takes a user input and returns a string or list of structures

    userinp: bool, activates CLI user input
    inp_fname: str, name of file from which structuresa are read
    """

    if inp_fname is not None:
        userinp=False

    if userinp:

        print("Input structure")

        structure=input()
    
    else:
        with open(inp_fname) as f:
            structure=[]
            for line in f.readlines():
                structure.append(line)
    
    return structure

def parse_struct(structure):
    """
    Parses structrues into the Gemini LLM to convert natural language into material identifiers

    structure: str, natural language representation of a material

    returns prop_dict: dict, dictionary containing the formula, elements, crystal system and space_group of the material, as determined by the LLM
    
    """
    from google import genai

    # To ensure standardisation and reproducibility, LLM prompt is very strictly controlled
    query_base="Return only the chemical formula, component elemental symbols grouped as a python list, crystal system, space group, in that order and on individual lines, with no other information of the following material."

    c=genai.Client()
    
    response = c.models.generate_content(
        model="gemini-3.1-flash-lite-preview", contents=f"{query_base} {structure}"
    )
    r=response.text
    c.close()
    
    props=["formula","elements","crystal_system","space_group"]
    prop_dict={}
    p=0
    for info in r.splitlines():
        prop_dict[props[p]]=info
        p+=1

    # convert 'elements' into Python list
    strip=prop_dict["elements"].strip("[]")
    replace_sing_quote=strip.replace("'","")
    replace_wsp=replace_sing_quote.replace(" ","")
    lst=replace_wsp.split(",")
    prop_dict["elements"]=lst

    return prop_dict