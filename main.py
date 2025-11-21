from string_utils import parse_chemical_reaction, count_atoms_in_reaction
from equation_utils import build_equations, my_solve

def balance_reaction(reaction):
    """Balances a chemical reaction and returns the coefficients as rationals."""
    reactants, products = parse_chemical_reaction(reaction)
    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    solved = my_solve(equations, coefficients)

    return solved + [1]  # last coefficient forced to 1
