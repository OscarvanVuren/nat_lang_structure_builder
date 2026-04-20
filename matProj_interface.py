
def get_matIDs(properties):
    from mp_api.client import MPRester
    print(f"test num elements {(len(properties["elements"]),len(properties["elements"]))}")
    with MPRester() as mpr:
        mats = mpr.materials.summary.search(formula=properties["formula"],
                                            elements=properties["elements"],
                                            crystal_system=properties["crystal_system"],
                                            spacegroup_symbol=properties["space_group"],
                                            num_elements=(len(properties["elements"]),len(properties["elements"])),
                                            fields=["material_id"])
    return mats

def get_structure_from_id(mpID):
    from mp_api.client import MPRester

    with MPRester() as mpr:
        result = mpr.materials.search(
            material_ids=mpID, fields=["initial_structures"]
            )

    init_structs = result[0]
    initial_structures = init_structs.initial_structures
    return initial_structures