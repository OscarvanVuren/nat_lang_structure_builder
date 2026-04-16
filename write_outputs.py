
def output_cif(struct,formula,tags=None):

    if tags is not None:
        filename=f"{formula}_{tags}.cif"

    else:
        filename=f"{formula}.cif"
        
    print(f"Writing file {filename}")
    struct.to(filename=filename)

    
