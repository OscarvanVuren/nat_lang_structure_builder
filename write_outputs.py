
def output_cif(struct,formula,tags=None):
    """
    Writes a structure to a .cif (Crystallographic Information File) using pyMatgen

    struct: pyMatgen structure, from materials project database
    formula: str, formula of structure to name files
    tags: str, tags to identify different structrures with same formula
    """

    if tags is not None:
        filename=f"{formula}_{tags}.cif"

    else:
        filename=f"{formula}.cif"
        
    print(f"Writing file {filename}")
    struct.to(filename=filename)

    
