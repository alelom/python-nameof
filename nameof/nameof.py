import inspect
import ast
from typing import Any, Union
import os

def nameof(var: Any, wrap_in_chars: str = "", replace_with_whitespace: Union[str, list[str]] = [] ) -> str:
    """
    Returns the name of the variable or attribute passed as the first argument.
    
    Args:
        var: The variable whose name should be returned.
        wrap_in_chars: Optional string to wrap the result with (added to start and end).
        replace_with_whitespace: Optional string or list of strings to replace with whitespace in the result.
    
    Returns:
        str: The name of the variable, possibly wrapped and/or with specified characters replaced by whitespace.
    
    Raises:
        ValueError: If the variable name cannot be determined.
    """
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
                            result = arg.id
                        # Support attribute access, e.g., nameof(obj.attr)
                        elif isinstance(arg, ast.Attribute):
                            result = arg.attr
                        else:
                            continue

                        # Replace specified characters with whitespace
                        if replace_with_whitespace:
                            if isinstance(replace_with_whitespace, str):
                                chars_list = [replace_with_whitespace]
                            else:
                                chars_list = replace_with_whitespace
                            for ch in chars_list:
                                result = result.replace(ch, " ")
                        # Wrap in specified characters
                        if wrap_in_chars:
                            result = f"{wrap_in_chars}{result}{wrap_in_chars}"
                        return result
              
    except Exception as e:
        if os.environ.get("nameof_test") or os.environ.get("nameof_test_debug"):
            print("Error in nameof function:", e)
    
    raise ValueError("Could not determine variable name. Ensure the variable is defined in the caller's scope.")