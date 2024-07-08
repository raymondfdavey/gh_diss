import os
import graphviz

def create_file_structure_graph(root_dir):
    dot = graphviz.Digraph(comment='File Structure')

    for root, dirs, files in os.walk(root_dir):
        for d in dirs:
            dot.node(os.path.join(root, d))
            dot.edge(root, os.path.join(root, d))
        for f in files:
            dot.node(os.path.join(root, f))
            dot.edge(root, os.path.join(root, f))
    
    return dot

root_directory = '/Users/rd81/MRI_DATA/MINI'
dot = create_file_structure_graph(root_directory)
dot.render('file_structure.gv', view=True)