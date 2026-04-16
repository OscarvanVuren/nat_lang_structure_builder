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