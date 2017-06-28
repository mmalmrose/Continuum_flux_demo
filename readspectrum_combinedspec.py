def readspectrum_combinedspec(inspec):
    import numpy as np
    import scipy as sp    
    from scipy import misc
    from astropy.io import fits as pyfits
    from astropy.time import Time
    image = pyfits.open(inspec)
    imheader = pyfits.getheader(inspec)
    specdat = np.array(image[0].data)

   # help(specdat)
    specsize = specdat.shape
    specsize= len(specsize)
   # print specsize, 'spectrum size'
    ''' check the dimension of the spectrum.  if only a single line, then we need to 
    get the uncertainty from the spread of the spectrum values, otherwise read
    the uncertainty in from the data
    '''
    if specsize== 1:
       thespec = specdat
       error = specdat
       error=np.insert(error, 0 , 0.0)
       #error.insert[0]
       error = error[0:len(specdat)]
       error = specdat-error
       errorbar = np.std(error)
       error[0:] = errorbar
       dtobs = image[0].header['DATE-OBS']

       #print dtobs
       tmobs = image[0].header['UT']
       timecode = dtobs+'T'+tmobs.strip()
       mjd = Time(timecode, format='isot', scale='utc').mjd
    if specsize == 2:
       error = specdat[1, :]
       thespec = specdat[0, :]
       begdate = image[0].header['FIRSTDAT']
       enddate = image[0].header['LASTDATE']
       #mjd = 50000.+(1./2.)*(np.float32(begdate) - np.float32(enddate)) + np.float32(begdate)
       sdate = (1./2.)*np.float32(enddate - begdate)
    mjd = image[0].header['MJD_AVE'] 
    return (thespec, error, len(thespec), image[0].header, mjd)  
