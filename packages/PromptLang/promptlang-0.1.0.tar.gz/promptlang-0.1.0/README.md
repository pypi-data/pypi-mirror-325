# PromptLang

PromptLang is a lightweight and efficient language designed for dynamic prompt processing with inline data transformations and caching.

## Features
- **Data Retrieval**: Access values dynamically using `{user.name}`.
- **Function Calls**: Invoke functions with `{fn:do_something user.patient_id}`.
- **Mandatory Fields**: Ensure essential data is provided using `{mandatory user.name}`.
- **Logical OR Operation**: Handle fallback values with `{user.patient_id | user.name}`.

## Example Usage
```python
from promptlang import PromptLang

def get_diagnosis_details(id):
   return "some serious thing"

data = {"user": {"name": "Alice", "patient_id": 1234}}
cache = {}
pl = PromptLang(data, cache)

prompt = """
Please check the diagnosis is aligned with symptoms?
User's name is {user.name} and Discharge Details are {fn:get_diagnosis_details user.patient_id}
"""
print(pl.generate_prompt(prompt))
```

## Installation
To install PromptLang, use:
```sh
pip install promptlang
```

## License
This project is licensed under the MIT License.

