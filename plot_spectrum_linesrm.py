def plot_spectrum_linesrm(fframe, newframe, framnum):
    import numpy as np
    import scipy as sp
    import matplotlib    
    import matplotlib.pyplot as plt
    from bin_array import bin_array as ba
    fig = plt.figure(3, figsize=(10,7))
    #ax1 = plt.subplot(211)
    ynorm = 1.0e-14
    plt.ylabel(r'$F_\lambda \; (10^{'+str(np.trunc(np.log10(ynorm)).astype(int)) +r'} \; \mathrm{erg \; s}^{-1}\;\mathrm{cm}^{-2}\mathrm{\AA}^{-1}$)')
    plt.xlabel(r'$\lambda \;(\mathrm{\AA})$')
    plt.plot(fframe['wl'], fframe[fframe.columns[framnum]]/ynorm, color = 'blue')
    plt.plot(fframe['wl'], newframe[newframe.columns[framnum]]/ynorm, color='red')
    # Label some of the emission lines on the plot to motivate their removal
    plt.text(4350, 0.31, 'Original', color='blue', fontsize=15)
    plt.text(4350, 0.27, 'Lines Removed', color = 'red', fontsize=15)
