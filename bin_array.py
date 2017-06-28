'''
Takes an array and returns an array that has been averaged into a number of bins.
will also return the standard deviation of the vals in that bin
'''
import numpy as np
def bin_array(arrayvals, nbins):
    startlen = len(arrayvals)
    binsize = np.int(np.ceil(np.float(startlen)/nbins))
    outarray = np.array([])
    outsigma = np.array([])
    for i in range(nbins):
        indexvals = [i*binsize, (i+1)*binsize-1]
        if indexvals[1] < np.float(startlen):
            outarray=np.append(outarray, np.nanmean(arrayvals[indexvals[0]:indexvals[1]]))
            ranged= (np.nanmax(arrayvals[indexvals[0]:indexvals[1]])-np.nanmin(arrayvals[indexvals[0]:indexvals[1]]))*0.5
            #print 'ranged', ranged
          #  outsigma=np.append(outsigma, np.nanstd(arrayvals[indexvals[0]:indexvals[1]])/np.sqrt(binsize))
            outsigma=np.append(outsigma, np.nanstd(arrayvals[indexvals[0]:indexvals[1]]))
           # outsigma=np.append(outsigma, ranged)
        #    print indexvals
        #if indexvals[1]  > np.float(startlen):
        #    outarray=np.append(outarray, np.mean(arrayvals[indexvals[0]:startlen]))
        #    outsigma=np.append(outsigma, np.std(arrayvals[indexvals[0]:startlen])/np.sqrt(np.float(startlen)-indexvals[0]))
    return (outarray, outsigma)
