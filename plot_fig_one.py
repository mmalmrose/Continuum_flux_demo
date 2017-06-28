import matplotlib.pyplot as plt
import scipy as sp
import matplotlib    
import matplotlib.pyplot as plt
import numpy as np
def plot_fig_one(fspec, pspec, framenum):
    #plt.plot(fspec['wl'], fspec[fspec.columns[1]], color = 'blue')
    #plt.text(4350, 0.25e-14, 'Total Flux', color='blue', fontsize=15)
    #plt.plot(pspec['wl'], pspec[pspec.columns[1]], color='green')
    #plt.text(4350, 0.05e-14, 'Polarized Flux', color='green', fontsize=15)
    fig = plt.figure(1, figsize=(10,7))
    ax1 = plt.subplot(211)
    ynorm = 1.0e-15
    plt.ylabel(r'$F_\lambda \; (10^{'+str(np.trunc(np.log10(ynorm)).astype(int)) +r'} \; \mathrm{erg \; s}^{-1}\;\mathrm{cm}^{-2}\mathrm{\AA}^{-1}$)')
    plt.xlabel(r'$\lambda \;(\mathrm{\AA})$')
    plt.plot(fspec['wl'], fspec[fspec.columns[framenum]]/ynorm, color = 'blue')
    plt.text(4350, 2.5, 'Total Flux', color='blue', fontsize=15)
    plt.plot(pspec['wl'], pspec[pspec.columns[framenum]]/ynorm, color = 'green')
    plt.text(4350, 0.5, 'Polarized Flux', color='green', fontsize=15)
    ax2 = plt.subplot(212)
    plt.ylabel(r'$\mathrm{Log_{10}} F_\lambda  \; \mathrm{erg \; s}^{-1}\;\mathrm{cm}^{-2}\mathrm{\AA}^{-1}$)')
    plt.xlabel(r'$\mathrm{Log_{10}} \lambda \;(\mathrm{\AA})$')
    plt.plot(np.log10(fspec['wl']), np.log10(fspec[fspec.columns[framenum]]), color = 'blue')
    plt.plot(np.log10(pspec['wl']), np.log10(pspec[pspec.columns[framenum]]), color = 'green')

