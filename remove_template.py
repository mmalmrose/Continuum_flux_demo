import scipy as sp
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d
def remove_template(tempfile, dframe):
    linetemplate= np.genfromtxt(tempfile, dtype=[('lambda', 'float'), ('flux', 'float')], delimiter=',')
    bad = np.where(linetemplate['flux'] <= 0)
    linetemplate['flux'][bad] = np.std(linetemplate['flux'])
    linetemplate['lambda'] = linetemplate['lambda']
    interpfunc=interp1d(linetemplate['lambda'] , linetemplate['flux'], kind='cubic', bounds_error=False)
    newtemplate= interpfunc(dframe['wl'])
    newframe = dframe.copy(deep=True)
        #remove the template from all of the df columns
    for i in range(0, (len(dframe.columns))-1):
        newframe[newframe.columns[i]] = dframe[dframe.columns[i]] - newtemplate
    return(newtemplate, newframe)
