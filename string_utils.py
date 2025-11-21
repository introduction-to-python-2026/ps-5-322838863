


def split_before_uppercases(formula):
    if not formula:
        return []
    parts = []
    current = formula[0]

    for ch in formula[1:]:
        if ch.isupper():
            parts.append(current)
            current = ch
        else:
            current += ch

    parts.append(current)
    return parts
    
     

def split_at_digit(formula):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            # First digit found
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number

    # No digit found
    return formula, 1
            
    
def count_atoms_in_molecule(formula):
    atom_dict = {}
    for atom in split_before_uppercases(formula):
        atom_name, atom_count = split_at_digit(atom)
        #atom_dict.update({atom_name: atom_count})
        atom_dict[atom_name] = atom_dict.get(atom_name, 0) + atom_count
    return atom_dict



def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
