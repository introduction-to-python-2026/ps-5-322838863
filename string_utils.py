# string_utils.py

def split_before_uppercases(formula):
    """Splits a string before every uppercase letter."""
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
    """Splits a string into element name and count (integer)."""
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1  # default count = 1


def count_atoms_in_molecule(formula):
    """Returns a dictionary of atom counts for a single molecule."""
    atom_dict = {}
    for atom in split_before_uppercases(formula):
        atom_name, atom_count = split_at_digit(atom)
        atom_dict[atom_name] = atom_dict.get(atom_name, 0) + atom_count
    return atom_dict


def parse_chemical_reacti
