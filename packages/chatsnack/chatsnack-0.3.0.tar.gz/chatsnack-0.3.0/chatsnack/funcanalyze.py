import inspect
import yaml
import re
from typing import get_type_hints

def parse_docstring_for_params(docstring, params):
    param_descriptions = {}
    lines = iter(docstring.split("\n"))
    current_param = None
    for line in lines:
        if current_param:
            if any(param in line for param in params):
                current_param = None
            else:
                param_descriptions[current_param] += ' ' + line.strip()
        for param in params:
            if param in line:
                current_param = param
                param_descriptions[param] = line.split(":")[1].strip()
    return param_descriptions

def python_func_to_yaml(func, parse_docstring=False):
    func_name = func.__name__
    func_docstring = inspect.getdoc(func)
    func_signature = inspect.signature(func)
    func_params = func_signature.parameters

    param_descriptions = {}
    if parse_docstring and func_docstring:
        param_descriptions = parse_docstring_for_params(func_docstring, func_params)

    # Get type hints
    type_hints = get_type_hints(func)

    yaml_data = {
        "name": func_name,
        "description": func_docstring.split("\n")[0] if func_docstring else None,
        "parameters": {
            "type": "object",
            "properties": {
                name: {
                    "type": str(type_hints.get(name, None)),  # Use get_type_hints
                    **({"description": param_descriptions.get(name, '') + 
                        (f' Defaults to {param.default}.' if param.default is not inspect.Parameter.empty else '')}
                        if param_descriptions.get(name, '') or param.default is not inspect.Parameter.empty else {})
                } for name, param in func_params.items()
            },
            "required": [name for name, param in func_params.items() if param.default is inspect.Parameter.empty]
        },
    }

    yaml_str = yaml.dump([yaml_data], sort_keys=False)

    return yaml_str
