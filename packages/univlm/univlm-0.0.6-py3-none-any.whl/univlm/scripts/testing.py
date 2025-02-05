import ast
from collections import OrderedDict
import os
import sys

def extract_if_exp(node):
    """Handle IfExp nodes by evaluating the condition."""
    if isinstance(node, ast.IfExp):
        # For IfExp, we'll take the 'body' value as default
        return extract_value(node.body)
    return None

def extract_value(node):
    """Extract value from various AST node types."""
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.Str):
        return node.s
    elif isinstance(node, ast.Tuple):
        return tuple(extract_value(elt) for elt in node.elts)
    elif isinstance(node, ast.IfExp):
        return extract_if_exp(node)
    elif isinstance(node, ast.Name):
        return node.id
    return str(ast.unparse(node))

def create_extraction_script(input_file):
    class OrderedDictVisitor(ast.NodeVisitor):
        def __init__(self):
            self.dicts = {}
            
        def visit_Assign(self, node):
            if isinstance(node.value, ast.Call) and \
               isinstance(node.value.func, ast.Name) and \
               node.value.func.id == 'OrderedDict':
                
                if len(node.value.args) == 1 and isinstance(node.value.args[0], ast.List):
                    pairs = []
                    for elt in node.value.args[0].elts:
                        if isinstance(elt, ast.Tuple) and len(elt.elts) == 2:
                            try:
                                key = extract_value(elt.elts[0])
                                value = extract_value(elt.elts[1])
                                pairs.append((key, value))
                            except Exception as e:
                                print(f"Warning: Error processing entry - {e}")
                                continue
                    
                    if hasattr(node.targets[0], 'id'):
                        self.dicts[node.targets[0].id] = OrderedDict(pairs)

    # Ensure correct path handling
    base_dir = os.path.dirname(input_file)  # Get the directory where the file is located
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"Error parsing file: {e}")
        return None

    visitor = OrderedDictVisitor()
    visitor.visit(tree)

    # Create output file in the same directory as the input file
    output_file = os.path.join(base_dir, f"extracted_{os.path.basename(os.path.splitext(input_file)[0])}.py")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("from collections import OrderedDict\n\n")
        
        for name, ordered_dict in visitor.dicts.items():
            f.write(f"{name} = OrderedDict([\n")
            for key, value in ordered_dict.items():
                try:
                    f.write(f"    ({repr(key)}, {repr(value)}),\n")
                except Exception as e:
                    print(f"Warning: Error writing entry {key}: {e}")
            f.write("])\n\n")

    return output_file

# If a file is passed as an argument, process it
if __name__ == "__main__":
    input_file = sys.argv[1]  
    create_extraction_script(input_file)
