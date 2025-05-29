import inspect
import ast
from typing import Any, Callable


def nameof(var: Any):
    # Try to extract the argument expression from the caller's source code
    frame = inspect.currentframe()
    code_context = None
    
    if frame is not None and frame.f_back is not None:
        outer_frame = frame.f_back
        frameinfo = inspect.getframeinfo(outer_frame)
        code_context = frameinfo.code_context
    try:
        if code_context:
            call_line = code_context[0].strip()
            tree = ast.parse(call_line)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and hasattr(node.func, 'id') and node.func.id == 'nameof': #type:ignore
                    if node.args:
                        arg = node.args[0]
                        if isinstance(arg, ast.Name):
                            return arg.id
                        # Support attribute access, e.g., nameof(obj.attr)
                        if isinstance(arg, ast.Attribute):
                            return arg.attr
              
    except Exception as e:
        print(e)
    
    # Fallback to variable name logic
    frame = inspect.currentframe()
    if frame is not None and frame.f_back is not None:
        callers_local_vars = frame.f_back.f_locals.items()
        names = [name for name, val in callers_local_vars if val is var]
        if len(names) == 1:
            return names[0]
        elif len(names) > 1:
            return "_and_".join(names)
    
    raise ValueError("Could not determine variable name. Ensure the variable is defined in the caller's scope.")