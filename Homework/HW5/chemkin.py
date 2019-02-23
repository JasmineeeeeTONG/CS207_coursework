import numpy as np

def get_progress_rate(k, c_species, v_reactants):
    """Returns the progress rate for a reaction of the form: va*A+vb*B --> vc*C.
    
    INPUTS
    =======
    k: float
       Reaction rate coefficient
    c_species: 1D list of floats
       Concentration of all species
    v_reactants: 1D list of floats
       Stoichiometric coefficients of reactants
    
    RETURNS
    ========
    w: float
       prgress rate of this reaction

    NOTES
    =====
    PRE: 
         - k, each entry of c_species and v_reactants have numeric type
         - c_species and v_reactants have the same length
    POST:
         - k, c_species and v_reactants are not changed by this function
         - raises a ValueError if k <= 0
         - raises an Exception if c_species and v_reactants have different length
         - returns the prgress rate w for the reaction

    EXAMPLES
    =========
    >>> get_progress_rate(10, [1.0, 2.0, 3.0], [2.0, 1.0, 0.0])
    20.0
    """
    if k <= 0:
        raise ValueError('k must be positive.')
    if len(c_species) != len(v_reactants):
        raise Exception('List c_species and list v_reactants must have same length.')
    w = k
    for c, v in zip(c_species, v_reactants):
        w *= pow(c, v)
    return w


def get_progress_rate_list(k, c_species, v_reactants, v_products):
    """Returns the list of progress rate for a list of reactions.
    
    INPUTS
    =======
    k: 1D list of floats
       k[i] is the reaction rate coefficient for the i-th reaction
    c_species: 1D list of floats
       Concentration of all species
    v_reactants: 2D list of floats
       v_reactants[i] are the list of stoichiometric coefficients of reactants of the i-th reaction
    v_products: 2D list of floats
       v_products[i] are the list of stoichiometric coefficients of products of the i-th reaction
    
    RETURNS
    ========
    w: 1D list of floats
       The list of prgress rates of the list of reactions

    NOTES
    =====
    PRE: 
         - each entry of k, c_species and v_reactants have numeric type
         - c_species and v_reactants[i] have the same length
         - v_reactants and v_products have the same shape
    POST:
         - k, c_species and v_reactants are not changed by this function
         - raises an Exception if k and v_reactants (or v_products) have different length
         - raises a ValueError if any k[i] <= 0
         - raises an Exception if c_species and v_reactants[i] have different length
         - returns the list of prgress rates for the list of reactions

    EXAMPLES
    =========
    >>> get_progress_rate_list([10, 10], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [2.0, 0.0, 2.0]], [[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]])
    [40.0, 10.0]
    """
    if len(v_reactants) != len(v_products):
        raise Exception('1st dimension of v_reactants and v_products must have same lenth.')
    
    num_reactions = len(v_reactants)
    if num_reactions != len(k):
        raise Exception('Length of k must equal the number of reactions.')
    
    w_list = []
    for i in range(num_reactions):
        w = k[i]
        if w <= 0:
            raise ValueError('k must be positive.')
        
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
    """Returns the list of progress rate for a list of reactions.
    
    INPUTS
    =======
    k: 1D list of floats
       k[i] is the reaction rate coefficient for the i-th reaction
    c_species: 1D list of floats
       Concentration of all species
    v_reactants: 2D list of floats
       v_reactants[i] are the list of stoichiometric coefficients of reactants of the i-th reaction
    v_products: 2D list of floats
       v_products[i] are the list of stoichiometric coefficients of products of the i-th reaction
    
    RETURNS
    ========
    w: 1D list of floats
       The list of prgress rates of the list of reactions

    NOTES
    =====
    PRE: 
         - each entry of k, c_species and v_reactants have numeric type
         - c_species and v_reactants[i] have the same length
         - v_reactants and v_products have the same shape
    POST:
         - k, c_species and v_reactants are not changed by this function
         - raises an Exception if k and v_reactants (or v_products) have different length
         - raises a ValueError if any k[i] <= 0
         - raises an Exception if c_species and v_reactants[i] have different length
         - returns the list of prgress rates for the list of reactions

    EXAMPLES
    =========
    >>> get_reaction_rate([10, 10], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [0.0, 0.0, 2.0]], [[0.0, 0.0, 1.0], [1.0, 2.0, 0.0]])
    array([[-30.],
           [-60.],
           [ 20.]])
    """
    w_list = get_progress_rate_list(k, c_species, v_reactants, v_products)
    w_matrix = np.asarray(w_list).reshape(len(w_list), 1)
    
    v_r_matrix = np.asarray(v_reactants).transpose()
    v_p_matrix = np.asarray(v_products).transpose()
    v_matrix = v_p_matrix - v_r_matrix
    
    reaction_rate_matrix = np.dot(v_matrix, w_matrix)
    return reaction_rate_matrix
    