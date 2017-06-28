def plot_spectrum(fframe, pframe, framnum):
    import numpy as np
    import scipy as sp
    import matplotlib    
    import matplotlib.pyplot as plt
    from bin_array import bin_array as ba
    from get_order_of_magnitude import get_order_of_magnitude as gom
    fig = plt.figure(2, figsize=(10,7))
    #ax1 = plt.subplot(211)
    ynorm = gom(fframe[fframe.columns[3]])
    plt.ylabel(r'$F_\lambda \; (10^{'+str(np.trunc(np.log10(ynorm)).astype(int)) +r'} \; \mathrm{erg \; s}^{-1}\;\mathrm{cm}^{-2}\mathrm{\AA}^{-1}$)')
    plt.xlabel(r'$\lambda \;(\mathrm{\AA})$')
    plt.plot(fframe['wl'], fframe[fframe.columns[framnum]]/ynorm)
    # Label some of the emission lines on the plot to motivate their removal
    plt.arrow(4860, 0.3, 0, -0.05, color='blue',head_width=75, head_length= 0.05)
    plt.arrow(4350, 0.3, 0, -0.05, color='blue', head_width = 75, head_length= 0.05)
    plt.arrow(4100, 0.3, 0, -0.05,  color='blue', head_width = 75, head_length= 0.05)
    plt.text(4350, 0.31, 'Hydrogen', color='blue', fontsize=15)
    plt.arrow(3300, 0.05, 0, 0.15, color = 'red',head_width=75, head_length= 0.05)
    plt.arrow(3800, 0.05, 0, 0.1, color = 'red',head_width=75, head_length= 0.05)
    plt.text(3500, 0.03, 'Ionized Iron',color='red', fontsize = 15 )
    plt.arrow(3500, 0.5, -500, 0, color = 'green', head_length= 100, head_width= 0.01)
    plt.text(3700, 0.5, 'Mg II', color = 'green', fontsize=15)
