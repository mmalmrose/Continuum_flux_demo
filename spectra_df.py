import numpy as np
import pandas as pd
from pandas import DataFrame as df
from read_all_spec import read_all_spec
from readspectrum_combinedspec import readspectrum_combinedspec
from rebin import rebin
import matplotlib.pyplot as plt
def spectra_df(direc):
    #direc = './spectra'
    specfiles, polfiles = read_all_spec(direc)
#create the array for the wavelength and frequency
    c = 2.99792458e+18 # angstroms/s
    redshift = 0.435 # for 1222+216 
#read in the first spectrum to get the length
    (fspec, ferr, fend, fheader, fmjd) = readspectrum_combinedspec(specfiles[0])
    (pspec, perr, pend, pheader, pmjd) = readspectrum_combinedspec(polfiles[0])
    wavend = fend*4.0 + 4000.0
    wave = np.linspace(4000.0, wavend,fend)
    restwave = wave/(1.0+redshift)
    restnu = c/restwave
    nuspec = np.float64((fspec/c)*np.power(restwave,2))
#create a dataframe so that all spectra can be read into it
#make one for polarized flux as well
    d = {'wl': restwave.tolist(), str(fmjd)+'_fl': fspec.tolist()}
    p = {'wl': restwave.tolist(), str(pmjd)+'_pfl': pspec.tolist()}

    for i in range(1, len(specfiles)):
        (fspec, ferr, fend, fheader, fmjd) = readspectrum_combinedspec(specfiles[i])
        (pspec, perr, pend, pheader, pmjd) = readspectrum_combinedspec(polfiles[i])
        if fspec.shape != restwave.shape:
            fspec = rebin(fspec, restwave.shape)
        if pspec.shape != restwave.shape:
            pspec = rebin(pspec, restwave.shape)
        d.update({str(fmjd)+'_fl': fspec.tolist()})

        p.update({str(pmjd)+'_pfl': pspec.tolist()})

    flux_df = df(data = d)
    cols = flux_df.columns.tolist()
    cols.insert(0, cols.pop(cols.index('wl')))
    pol_df = df(data = p)
    cols = pol_df.columns.tolist()
    cols.insert(0, cols.pop(cols.index('wl')))
    return(flux_df, pol_df)

