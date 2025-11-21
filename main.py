import string_utils as string_u , equation_utils as equation_u

def balance_reaction(reaction):
    """Balances a chemical reaction and returns the coefficients as rationals."""
    reactants, products = equation_u.parse_chemical_reaction(reaction)
    reactant_atoms = equation_u.count_atoms_in_reaction(reactants)
    product_atoms = equation_u.count_atoms_in_reaction(products)

    equations, coefficients = equation_u.build_equations(reactant_atoms, product_atoms)
    solved = string_u.my_solve(equations, coefficients)

    return solved + [1]  # last coefficient forced to 1
