#importing needed packages for this script
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['font.family'] = 'serif'
plt.rcParams['xtick.labelsize'] = 13
plt.rcParams['ytick.labelsize'] = 13


##################
#This Section covers the If-Else Statements
##################
print('Example of buying a guitar using If-Else Statements!!')

#Buying a guitar example
money = 100

fender = 500
squire = 99

print(f'I have ${money}')
print(f'A Fender Stratocaster costs ${fender}')
print(f'A Squire Stratocastor costs ${squire}')

if money > fender:
    print('I can buy a Fender :D')
    
else:
    print("I cannot buy a Fender :'(")
    
if squire < money:
    print('I can buy a Squire though!')
    
else:
    
    print("I cannot buy a Squire :'(")

print()

#######
#example with elif
#######

print('example using elif')

Value = 20

print(f'Value is: {Value}')

if Value < 16:
    print('Value is Below 16')
    
elif Value < 24:
    print('Value is Below 24')
    
elif Value < 30:
    print('Value is Below 30')
    
else:
    print('Value is above 30')

print()

print('Example on conditional Statements')
x = 5 
y = 10

print(x == y)
print(x != y)
print(x <= y)
print(x >= y)
print(x > y)
print(x < y)

print(f'x = {x}')
print(f'y = {y}')

print(f'x == y evaluates to {x == y}')
print(f'x != y evaluates to {x != y}')
print(f'x <= y evaluates to {x <= y}')
print(f'x >= y evaluates to {x >= y}')
print(f'x > y evaluates to {x > y}')
print(f'x < y evaluates to {x < y}')
print()

##################
#Section below covers For-Loops
##################
print('Starting For-Loop examples')
print('Looping over range(10) gives us: ')
for i in range(10):
    print(i)

print()

print('Looping over range(1, 10) gives us: ')
for i in range(1, 10):
    print(i)

print('Making Wavelength and Spectra Arrays')
np.random.seed(10)
wavelength_array = np.linspace(1200, 4000, 12)
spectra_array = np.random.normal(size = 12)

print('Looping over the index of the wavelength array')
for i in range(len(wavelength_array)):
    print(f'Index: {i},  Value: {wavelength_array[i]}')
print()

print('Looping over the index of the spectra array')
for i in range(len(spectra_array)):
    print(f'Index: {i},  Value: {spectra_array[i]}')
print()



print('Looping over the actual values of the Wavelength array')

for wavelength in wavelength_array:
    
    print(wavelength)
print()

print('Looping over the actual values of the Spectra array')
for spectra in spectra_array:
    
    print(spectra)
print()

print('Example with zip() in For-Loops')

for wave, spec in zip(wavelength_array, spectra_array):
    
    print(f'Wavelength {wave:.2f} has Flux {spec:7.2f} ergs/s/cm^2/Angstroms')
print()

print('Example using enumerate() in For-Loops')

enumerate_arr = np.array([11, 22, 23, 44, 25, 16, 27])

for idx, val in enumerate(enumerate_arr):
    print(f'{idx} ---- {val}')

print()

print('Example combining If-Else statements with For-Loops')
np.random.seed(10)
wavelength_array = np.linspace(1200, 4000, 120)
spectra_array = np.random.normal(size = 120)

for i in range(len(wavelength_array)):
    
    if (wavelength_array[i] > 3000) & (wavelength_array[i] < 3500):
        print(f'Index: {i} -------- Wavelength: {wavelength_array[i]:.2f} ------  Flux: {spectra_array[i]:5.2f}')
print()

###################
#The Section below covers user defined functions
###################
def filter_by_mag(arr, mag):
    
    '''
    This function will take an array of values and returns a subset whose magnitude is above the inputted mag.
    
    Inputs
    ------------
    arr (array, list): An array of magnitude values, will assume it's in AB Magnitudes
    mag (float): A magnitude threshold (assumes AB Magnitudes) 
    
    Returns
    --------------
    valid_mag_arr (arr): an array of magnitudes that are above the magnitude threshold
    '''
    
    #defining empty array to store valid magnitudes
    valid_mag_arr = np.array([])
    
    #looping over all the magnitudes in the array arr
    for value in arr:
        
        if value >= mag:
            
            valid_mag_arr = np.append(valid_mag_arr, value)
        
    return valid_mag_arr

def plotting_histogram(data, num_bins = 20):

    '''
    This function will take in a 1D array of data and plot a histogram

    Input(s)
    ----------
    data: 1D array of values
    num_bins(optional): defaults to having 20 bins but it should be an integer or an array of bin edges 
    '''
    
    #generating a histogram of the data and grabbing the number counts in each bins as well as the bin edges
    bin_vals, bin_edges = np.histogram(data, bins = num_bins)
    
    #computing the bin center for plotting
    bin_center = (bin_edges[1:] + bin_edges[:-1]) / 2
    
    #plotting the histogram and points of the histogram
    plt.figure(figsize = (7, 5), facecolor = 'white', constrained_layout = True)
    plt.hist(data, bins = num_bins, histtype='step', color ='red')
    plt.scatter(bin_center, bin_vals, color = 'black', s = 100)
    plt.xlabel('Magnitudes')
    plt.ylabel('Frequency')
    plt.show()



def Display_Message():
    
    print('Welome to the Python Bootcamp')
    print('Today we are covering python functions')
    print('This function does not take any input nor does it return anything')
    print(':D')


def Function1(arg1, arg2):
    '''
    Function that takes 2 numbers and multiplies them together
    
    Inputs
    --------------------
    arg1 (float): numerical value to multiply with arg2 
    arg2 (float): numerical value to multiply with arg1
    
    Returns
    --------------------
    product (float): the multiplication of arg1 and arg2 (arg1 * arg2)    
    '''
    return arg1 * arg2

def Function2(arg3, arg4, arg1, arg2):
    
    '''
    Function to show a function in a function. We first compute the ratio of arg3/arg4 and then
    use Function1 to compute the product of arg1 and arg2 and then add the two
    
    Inputs
    ----------------
    arg3 (float): numerator of the ratio arg3/arg4
    arg4 (float): denom in ratio arg3/arg4
    arg1 (float): parameter in Function 1 to compute arg1 * arg2
    arg2 (float): parameter in Function 1 to compute arg1 * arg2
    
    Returns
    ----------------
    summation (float): arg3/arg4 + Function1(arg1, arg2)
    '''
    
    term1 = arg3/arg4
    term2 = Function1(arg1, arg2)
    
    print(f'Term 1 is: {term1}')
    print(f'Term 2 is: {term2}')
    
    print(f'Summation of the two is: {term1 + term2:.2f}')
    
    return term1 + term2

np.random.seed(10)
mag_array = np.random.exponential(scale = 20, size = 100)

#Example of calling a function
filtered_mag_array = filter_by_mag(mag_array, 24)
print()

print('The results of the filter_by_mag Function is:')
print(filtered_mag_array)
print()

print('Example using the plotting histogram function')
plotting_histogram(mag_array)
print()

print('Example using Display_Message')
Display_Message()