


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
 in enumerate(formula):
        if ch.isdigit():
            # First digit found
            prefix = formual[:i]
            number = int(formual[i:])
            return prefix, number

    # No digit found
    return formual, 1
            
dict = atom_dict{}
def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""


    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        atom_dict.update{atom_name: atom_count}
    return atom_dict{}
        
        
        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
