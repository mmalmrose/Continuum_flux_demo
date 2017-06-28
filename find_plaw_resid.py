import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from lmfit import minimize, Parameters
def find_plaw_resid(params, x, data, sig_data):
    normalize = params['norm'].value
    index = params['alpha'].value
    model = np.float64(normalize*np.power(x,(-1)*index))
    resid = ((data-model))**2/sig_data**2
    return resid
    
