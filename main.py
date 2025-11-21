import string_utils as su, equation_utils as eu

def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    reactants, products = su.parse_chemical_reaction(reaction) 
    reactant_atoms = su.count_atoms_in_reaction(reactants) 
    product_atoms = su.count_atoms_in_reaction(products)
    
    equations, coefficients = eu.build_equations(reactant_atoms, product_atoms)
    coefficients = eu.my_solve(equations, coefficients) + [1]

    return coefficients 
