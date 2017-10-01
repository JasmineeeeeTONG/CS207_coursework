import numpy as np
def get_progress_rate(k, c_species, v_reactants):
    """Returns the progress rate for a reaction of the form: va*A+vb*B --> vc*C.
    
    INPUTS
    =======
    k: float
       Reaction rate coefficient
    c_species: 1D list of floats
       Concentration of specie, including both reactants and products
    v_reactants: 1D list of floats
       Stoichiometric coefficients of reactants
    
    RETURNS
    ========
    w: float
       prgress rate of this single reaction

    NOTES
    =====
    PRE: 
         - k, each entry of c_species and v_reactants have numeric type
         - c_species and v_reactants have the same length
    POST:
         - k, each entry of c_species and v_reactants are not changed by this function
         - raises an Exception if c_species and v_reactants have different length
         - returns the prgress rate w for the reaction: va*A+vb*B --> vc*C

    EXAMPLES
    =========
    >>> get_progress_rate(10, [1.0, 2.0, 3.0], [2.0, 1.0, 0.0])
    20.0
    """
    if len(c_species) != len(v_reactants):
        raise Exception('List c_species and list v_reactants must have same length.')
    w = k
    for c, v in zip(c_species, v_reactants):
        w *= pow(c, v)
    return w

def get_progress_rate_list(k, c_species, v_reactants, v_products):
    if len(v_reactants) != len(v_products):
        raise Exception('1st dimension of v_reactants and v_products must have same lenth.')
    
    num_reactions = len(v_reactants)
    w_list = []
    for i in range(num_reactions):
        w = k[i]
        vi_r = v_reactants[i]
        vi_p = v_products[i]
        if len(vi_r) != len(vi_p):
            raise Exception('2nd dimension of v_reactants and v_products must have same lenth.')
        if len(vi_r) != len(c_species):
            raise Exception('c_species and the 2nd dimension of v_reactants must have same length.')
        w = get_progress_rate(k[i], c_species, vi_r)
        w_list.append(w)
    return w_list

def get_reaction_rate(k, c_species, v_reactants, v_products):
    w_list = get_progress_rate_list(k, c_species, v_reactants, v_products)
    w_matrix = np.asarray(w_list).reshape(len(w_list), 1)
    
    v_r_matrix = np.asarray(v_reactants).transpose()
    v_p_matrix = np.asarray(v_products).transpose()
    v_matrix = v_p_matrix - v_r_matrix
    
    reaction_rate_matrix = np.dot(v_matrix, w_matrix)
    return reaction_rate_matrix