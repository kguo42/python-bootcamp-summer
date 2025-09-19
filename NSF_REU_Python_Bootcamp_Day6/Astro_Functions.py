import numpy as np
from astropy.io import fits
from astropy.table import Table

def computing_redshift(lambda_obs, lambda_rest):
    '''
    Function to compute the redshift of a source given the observed wavelength of the line and 
    the rest frame wavelength of the line
    
    Inputs
    -------------
    lambda_obs (float): observed wavelength of the emission line
    lambda_rest (float):  Rest-Frame wavelength of the emission line
    
    Returns
    -------------
    z (float): the redshift of the source
    
    '''
    
    z = lambda_obs - lambda_rest / lambda_rest
    
    return z


def computing_error_on_ratio(num, denom, err_num, err_denom):
    
    '''
    This function computes the error propagation of a ratio
    
    Uses sigma_ratio = ratio * sqrt((num/err_num)^2 + (denom/err_denom)^2)
    
    Inputs
    ----------------
    
    num: The value in the numerator
    denom: the value in the denominator
    err_num: The error on the value in the numerator
    err_denom: the error on the value in the denominator
    
    Returns
    ------------
    ratio_err: The error on the ratio (num/denom)
    '''
    
    
    ratio = num/denom
    
    ratio_err = ratio * np.sqrt((num/err_num)**2 + 
                                (denom/err_denom)*2)
    
    return ratio_err
    
    
def Removing_Emission_Line_Regions(wavelength, spectra):
    
    '''
    This function is an intermediate function needed to compute the UV-beta slope of galaxies. 
    This function will remove emission line regions so that we can fit the beta line so emission lines won't bias the fit
    
    Inputs
    ------------
    wavelength: rest-frame wavelength of the spectra in Angstroms
    spectra: spectra of the source, same length as wavelengths
    
    Returns
    ------------
    masked_wavelength: a wavelength window where emission lines are removed
    masked_flux: the flux windows where the emission lines are removed
    '''
    
    window1_mask = (wavelength >= 1268) & (wavelength <= 1284) 
    window2_mask = (wavelength >= 1309) & (wavelength <= 1316) 
    window3_mask = (wavelength >= 1342) & (wavelength <= 1371) 
    window4_mask = (wavelength >= 1407) & (wavelength <= 1515) 
    window5_mask = (wavelength >= 1562) & (wavelength <= 1583) 
    window6_mask = (wavelength >= 1677) & (wavelength <= 1740) 
    window7_mask = (wavelength >= 1760) & (wavelength <= 1833) 
    window8_mask = (wavelength >= 1866) & (wavelength <= 1890) 
    window9_mask = (wavelength >= 1930) & (wavelength <= 1950) 
    window10_mask = (wavelength >= 2400) & (wavelength <= 2580) 
    
    full_mask = (window1_mask & window2_mask & window3_mask & window4_mask & window5_mask & 
                 window6_mask & window7_mask & window8_mask & window9_mask * window10_mask)
    
    return wavelength[full_mask], spectra[full_mask]


def Filter_Table_by_Redshift(filename):
    
    '''
    This function will return back a subset of a catalog so that we can then use that subset in our calculations
    
    Inputs
    -----------
    filename: the file path of the file
    
    
    Returns
    -----------
    mass_in_range: Astropy table with the masses in range
    '''
    
    #reading in the file as an Astropy Table
    candels_tab = Table.read(filename)
    
    #making a redshift mask
    z_mask = (candels_tab['zbest'] >= 2) & (candels_tab['zbest'] <= 5)
    
    #applying mask to the table
    reduced_tab = candels_tab[z_mask]
    
    #finding the index where the mass is between 8 - 10
    idx = np.where((reduced_tab['Mass'] >= 8) & (reduced_tab['Mass'] <= 10))
    
    mass_in_range = candels_tab[idx]
    
    return mass_in_range


def log10_and_error_propagaton_of_log10(A, sigma_A, a = 1, b = 1):
    
    '''
    This is an error propagation of the function f = a * log10(b*A) with A being the value and sigma_A the error on A
    
    sigma_f = np.abs(a) sigma_A/(A * ln(10))
    
    
    '''
    log_value = a * np.log(b*A)
    sigma_log10 = (np.abs(a) * b*sigma_A)/(A * np.ln(10)) 
    
    return log_value, sigma_log10