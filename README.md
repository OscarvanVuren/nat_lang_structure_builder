# Natural_Language_Structure_Builder
Exercise for postdoctoral position at SDU

## Installation Instructions
Depends on `google-genai` and `mp-api`. These can be installed via pip.
```
pip install google-genai mp-api
```

## Running the Code
API keys must be provided as environment variables.
```
export GEMINI_API_KEY="YOUR GEMINI API KEY"
export MP_API_KEY="YOUR MATERIALS PROJECT API KEY"
```

With the file `main.py` in the `PYTHONPATH`, the program may be executed as shown below:
```
from nat_lang_structure_builder.main import nat_lang_inputs

nat_lang_inputs()
```
This is the interactive mode, where a free text input through the CLI allows for a single search of the Materials Projetc Database. Multiple queries may be run together by combining into a single text file and passed to the code as such.
```
from nat_lang_structure_builder.main import nat_lang_inputs

nat_lang_inputs("test_mats.txt")
```

## Design Considerations
Modularity and extensibility was a key design choice here, though functional programming rather than more Pythonic object orientation was used to simplify and accelerate production. Development into a more Pythonic structure would be relatively simple once the underlying procedures have been developed. The `.cif` file structure was chosen as it is readily compatible with software such as ASE for the setup of DFT simualations. This also matches the files that would be taken from experimental databases such as the ICSD. Writing outputs has been separated into its own routine to allow additional file formats in future, such as the generic `.xyz` or the ASE specific `.traj` format. The selection of materials in two steps: finding Materials Project IDs and then using these IDs to select structures, was used considering the potential to stop the code if the procedure returns too many matches.

The scope of materials that this code should be able to manage extends as far as the materials project database allows. This database contains simulated structures for many materials, and the code will return all strutures that match a query. Currently the choice of material needs to be specific, for example "a perovskite oxide with titanium **and** barium", rather than general; "a perovskite oxide with titanium **or** barium".

The program returns structured output files that can be used as geometry inputs into a DFT simulation and can convert natural language into `.cif` structures. Given more time, I would like to have expanded the scope to include experimental structures as well as simulated structures, through an interface to the Inorganic Crystal Structure Database. Additionally, the extension of the code to constructing geometries from the ground up, rather than just fetching from a database, is an exciting challenge that would be interesting to tackle.

Further selection of materials, considering computed properties such as lattice parameters (via the total volume of the unit cell), band gaps and electronic energies, would be possible. Time constraints enforced the choice of keys for selection of materials from the Materials Project Database, though these keys could be expanded relatively simply.