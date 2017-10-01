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

def get_progress_rate_complex(k, c_species, v_reactants, v_products):
    """Returns the progress rate for a reaction of the form: a*A + b*B --> c*C; d*A + e*C --> f*B + g*C
    
    INPUTS
    =======
    k: 1D list of floats
       Reaction rate coefficient
    c_species: 1D list of floats
       Concentration of specie, including both reactants and products
    v_reactants: 2D list of floats
       1st dimemsion indicates the number of reactions, which is 2 for here
       Stoichiometric coefficients of reactants
    v_products: 2D list of floats
       1st dimemsion indicates the number of reactions, which is 2 for here
       Stoichiometric coefficients of products
    
    RETURNS
    ========
    w_list: 1D list of floats
        progress rate of these 2 reactions

    NOTES
    =====
    PRE: 
         - Each entry of k, c_species and v_reactants have numeric type
         - Each dimension of v_reactants and v_products have the same length
    POST:
         - k, c_species, v_reactants and v_products are not changed by this function
         - raises an Exception if any dimension of v_reactants and v_products have different length
         - raises an Exception if k and the 1st dimension of v_reactants (or v_products) must have different length
         - raises an Exception if c_species and the 2nd dimension of v_reactants (or v_products) have different length
         - returns the prgress rate [w1, w2] as a list for reaction: a*A + b*B --> c*C; d*A + e*C --> f*B + g*C

    EXAMPLES
    =========
    >>> get_progress_rate_complex(10, [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0],[2.0, 0.0, 2.0]], [[0.0, 0.0, 2.0],[0.0, 1.0, 1.0]])
    [40.0, 10.0]
    """
    if len(v_reactants) != len(v_products):
        raise Exception('1st dimension of v_reactants and v_products must have same lenth.')
    if len(v_reactants) != len(k):
        raise Exception('k and the 1st dimension of v_reactants must have same length.')
    
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
        for c, v in zip(c_species, vi_r):
            w *= pow(c, v)
        w_list.append(w)
    return w_list

def get_reaction_rate(k, c_species, v_reactants, v_products):
    """Returns the reaction rate for a reaction of the form: a*A + b*B --> c*C; d*C --> e*A + f*B
    
    INPUTS
    =======
    k: 1D list of floats
       Reaction rate coefficient
    c_species: 1D list of floats
       Concentration of specie, including both reactants and products
    v_reactants: 2D list of floats
       1st dimemsion indicates the number of reactions, which is 2 for here
       Stoichiometric coefficients of reactants
    v_products: 2D list of floats
       1st dimemsion indicates the number of reactions, which is 2 for here
       Stoichiometric coefficients of products
    
    RETURNS
    ========
    w_list: 1D list of floats
        progress rate of these 2 reactions

    NOTES
    =====
    PRE: 
         - Each entry of k, c_species and v_reactants have numeric type
         - Each dimension of v_reactants and v_products have the same length
    POST:
         - k, c_species, v_reactants and v_products are not changed by this function
         - raises an Exception if any dimension of v_reactants and v_products have different length
         - raises an Exception if k and the 1st dimension of v_reactants (or v_products) must have different length
         - raises an Exception if c_species and the 2nd dimension of v_reactants (or v_products) have different length
         - returns the prgress rate [w1, w2] as a list for reaction: a*A + b*B --> c*C; d*C --> e*A + f*B

    EXAMPLES
    =========
    >>> get_reaction_rate(10, [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0],[2.0, 0.0, 2.0]], [[0.0, 0.0, 1.0],[1.0, 2.0, 0.0]])
    [40.0, 10.0]
    """
    if len(v_reactants) != len(v_products):
        raise Exception('1st dimension of v_reactants and v_products must have same lenth.')
    if len(v_reactants) != len(k):
        raise Exception('k and the 1st dimension of v_reactants must have same length.')
    
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
        for c, v in zip(c_species, vi_r):
            w *= pow(c, v)
        w_list.append(w)
    return w_list
