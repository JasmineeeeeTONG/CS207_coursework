import numpy as np
import math
import warnings

# Return constant value of k
def const_k(k):
    """Returns the constant value of k.
    
    INPUTS
    =======
    k: float
    
    RETURNS
    ========
    constant value of k: float
    
    NOTES
    =====
    PRE: 
         - k has numeric type
         
    POST:
         - returns a float for the constant value of k

    EXAMPLES
    =========
    >>> const_k(0.5)
    0.5
    """
    return k

# Return Arrhenius reaction rate 
def arr_k(T, params, R=8.314):
    """Returns the value of k determined by the Arrhenius rate.
    
    INPUTS
    =======
    T: float
       Temperature in a Kelvin scale
    params: list, length = 2
       params[0]: A
       params[1]: E
    R: float, optional, default value is 8.314
       Constant term, should never be changed except to convert units
    
    RETURNS
    ========
    the Arrhenius rate k: float

    NOTES
    =====
    PRE: 
         - T, params[0], params[1] have numeric type
         - three or fewer inputs
    POST:
         - T and each entry of parmas are not changed by this function
         - raises a ValueError if T <= 0
         - raises an Exception if the length of params is not 2
         - raises a ValueError if params[0] <= 0
         - raises a warning if R is modified
         - returns the value of k determined by the Arrhenius rate

    EXAMPLES
    =========
    >>> arr_k(1000, [4, 100])
    3.9521765654534593
    """
    if T <= 0: 
        raise ValueError('Error: Temperature T must be positive.')
    if len(params) != 2:
        raise Exception('Error: The length of params must be 2 in the order of [A, E].')
    if params[0] <= 0:
        raise ValueError('Error: The Arrhenius prefactor A must be positive.')
    if R != 8.314:
        warnings.warn('Warning: R = 8.314, the ideal gas constant should never be changed except to convert units.')
    A = params[0]
    E = params[1]
    try:
        ans = A * math.exp((-1)*E/(R*T))
        if ans == 0: 
            warnings.warn('Underflow: k is too close to 0, return value is set to 0.')
    except OverflowError:
        warnings.warn('Overflow: k is too large, return value is set to float(\'inf\').')
        ans = float('inf')
    return ans

# Return modified Arrhenius reaction rate 
def modified_arr_k(T, params, R=8.314):
    """Returns the value of k determined by the Arrhenius rate.
    
    INPUTS
    =======
    T: float
       Temperature in a Kelvin scale
    params: list, length = 3
       params[0]: A
       params[1]: b
       params[2]: E
    R: float, optional, default value is 8.314
       Constant term, should never be changed except to convert units
    
    RETURNS
    ========
    the modified Arrhenius rate k: float

    NOTES
    =====
    PRE: 
         - T, params[0], params[1], params[2] have numeric type
         - three or fewer inputs
    POST:
         - T and each entry of parmas are not changed by this function
         - raises a ValueError if T <= 0
         - raises an Exception if the length of params is not 3
         - raises a ValueError if params[0] <= 0
         - raises a ValueError if params[1] is a complex number
         - raises a warning if R is modified
         - returns the value of k determined by the modified Arrhenius rate

    EXAMPLES
    =========
    >>> modified_arr_k(100, [2, 1, 100])
    177.33459568242117
    """
    if T <= 0: 
        raise ValueError('Temperature T must be positive.')
    if len(params) != 3:
        raise Exception('To get modified Arrhenius reaction rate, the length of params must be 3 in the order of [A, b, E].')
    if params[0] <= 0:
        raise ValueError('The Arrhenius prefactor A must be positive.')
    if isinstance(params[1], complex) and params[1].imag != 0:
        raise ValueError('The modified Arrhenius parameter b must be real.')
    if R != 8.314:
        warnings.warn('Warning: R = 8.314, the ideal gas constant should never be changed except to convert units.')
    A = params[0]
    b = params[1]
    E = params[2]
    try:
        ans = A * pow(T, b) * math.exp((-1)*E/(R*T))
        if ans == 0: 
            warnings.warn('Underflow: k is too close to 0, return value is set to 0.')
    except OverflowError:
        warnings.warn('Overflow: k is too large, return value is set to float(\'inf\').')
        ans = float('inf')
    return ans
    