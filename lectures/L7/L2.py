import numpy as np

def L2(v, *args):
    """Returns the L2 norm (weighted if weights specified) of a vector v.
    
    INPUTS
    =======
    v: list
       Components of the vector v = [v1, v2, ..., vn]
    *args: list, optional
       Weights for each component of v
    
    RETURNS
    ========
    L2 norm: float
       Weighted L2 norm of the vector using the weight values specified by *args
       A value exception is raised when the vector and the weights have different length

    NOTES
    =====
    PRE: 
         - v is a list of numeric type values
         - w is a list of numeric type values
    POST:
         - v and *args are not changed by this function
         - raises a ValueError exception if the vector and the weights have different length
         - returns weighted L2 norm of the vector

    EXAMPLES
    =========
    >>> L2([4, 3], [1, 1])
    5
    """
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)