import numpy as np
def read_all_spec(direc):
    myspec = direc+'/specfiles.txt'
    mypol =  direc+'/polfiles.txt'
    allspectra =  np.genfromtxt(myspec.strip(), dtype='S150')
    polspectra =  np.genfromtxt(mypol.strip(), dtype='S150')
    allspectra = [direc+'/'+ allspectra[x] for x in range(len(allspectra))]
    polspectra =  [direc+'/'+ polspectra[x] for x in range(len(polspectra))]
    return(allspectra, polspectra)
