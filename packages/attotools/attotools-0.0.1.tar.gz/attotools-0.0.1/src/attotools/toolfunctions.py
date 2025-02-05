import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
import csaps

# convert SI units to Atomic units
def SI2Atom(x,PhyQuan):
    PhyQuan = PhyQuan.lower()
    if PhyQuan == "mass":
        y = x/9.1093897e-31 
    elif PhyQuan == "length":
        y = x/5.29177249e-11
    elif PhyQuan == "time":
        y = x/2.41888129e-17
    elif PhyQuan == "velocity":
        y = x/2.188e6
    elif PhyQuan == "angularfrequency":
        y = x/4.13414251e16
    elif PhyQuan == "energy":
        y = x/(27.211*1.6e-19)
    elif PhyQuan == "charge":
        y = x/1.6e-19
    elif PhyQuan == "efield":
        y = x/5.142e11
    elif PhyQuan == "intensity":
        y = x/3.509e20
    elif PhyQuan == "force":
        y = x/8.239e-8
    else:
        print("Undefined Physical Quantity: ", PhyQuan ,"!")
        y = x
    return y

# move array elements along specified axis
def shift_arr(arr, shift, fill_value=0,axis=1):
    result = np.empty_like(arr)
    shift = int(shift)
    if shift > 0:
        if arr.ndim==1:
            result[:shift] = fill_value
            result[shift:] = arr[:-shift]
        elif arr.ndim==2:
            if axis==0:
                result[:shift,:] = fill_value
                result[shift:,:] = arr[:-shift,:]
            else:
                result[:,:shift] = fill_value
                result[:,shift:] = arr[:,:-shift]
    elif shift < 0:
        if arr.ndim==1:
            result[shift:] = fill_value
            result[:shift] = arr[-shift:]
        elif arr.ndim==2:
            if axis==0:
                result[shift:,:] = fill_value
                result[:shift,:] = arr[-shift:,:]
            else:
                result[:,shift:] = fill_value
                result[:,:shift] = arr[:,-shift:]
    else:
        result[:] = arr
    return result

# curve smoothing
def smooth(x,balance=0.2,BgSub=True):
    shapeP = x.shape
    # Background substraction
    if BgSub:
        if x.ndim==1:
            x = x-x[0]
        elif x.ndim==2:
            x = x - np.reshape(x[:,0],[shapeP[0],1]).dot(np.ones([1,shapeP[1]]))
    
    phi = np.unwrap(x)
    N = phi.shape[phi.ndim-1]
    xx = np.linspace(0,N-1,N)
    data = csaps.csaps(xx,phi,xx,smooth=balance)
    return data

# random values with polynomial
def rand_poly(N,xmin=-1,xmax=1, order=3):
    x = np.linspace(xmin,xmax,N)
    coef = np.random.rand(order)
    return(np.polyval(coef,x))

# demo 2d array
def demo_arr2d(M=6,N=np.nan):
    if np.isnan(N):
        N=M
    arr = np.zeros((M,N))
    for ii in range(M):
        for jj in range(N):
            arr[ii][jj] = 10*(ii+1)+(jj+1)
    
    return arr

# average every N points
def moving_average(y,dx,N):
    yo=[]
    M = len(y)
    Ind = np.array(np.arange(0,M,dx))
    N2 = int(N/2)
    for ii in Ind:
        a = max(ii-N2,0)
        b = min(ii+N2,M-1)
        yo.append(np.mean(y[a:b]))
    
    return (np.array(yo),Ind)
    