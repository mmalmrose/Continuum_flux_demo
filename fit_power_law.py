import lmfit
from lmfit import  Model, minimize, Parameters
from find_plaw_resid import find_plaw_resid
import numpy as np
def fit_power_law(data, ii):
    x = data['wl'].as_matrix()/1000.0
    y = data[data.columns[ii]].as_matrix()
    z = data[data.columns[ii]].as_matrix()   
    goodfit = np.where(y > 0.0)
    plaw_params = Parameters() 
    plaw_params.add('norm', value=0.05, min=np.float64(0.0))
    plaw_params.add('alpha', value=np.float64(-0.5))
    output = minimize(find_plaw_resid, plaw_params, args=(x[goodfit]/1000.0, 
    y[goodfit]/1.0e-14, z[goodfit]/3.0e-13), method='lm')
    return plaw_params

