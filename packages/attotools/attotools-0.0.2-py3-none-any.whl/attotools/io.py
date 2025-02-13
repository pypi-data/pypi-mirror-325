from cmath import isnan
import cv2
import struct
import numpy as np

def get_sBit(filename):
    sBit = 0
    with open(filename, 'rb') as f:
        bytes = f.read()
        bytes = bytes[8:]
        sBit = 0
        while bytes:
            length = struct.unpack('>I', bytes[:4])[0]
            bytes = bytes[4:]
            chunk_type = bytes[:4]
            bytes = bytes[4:]
            chunk_data = bytes[:length]
            bytes = bytes[length:]
            if chunk_type == b"sBIT":
                sBit = int.from_bytes(chunk_data[0:8],byteorder='little')
                break
            bytes = bytes[4:]

    return sBit

def load_png(filename):
    sbit = get_sBit(filename)
    data = cv2.imread(filename,cv2.IMREAD_ANYCOLOR|cv2.IMREAD_ANYDEPTH)
    byteNum = data.dtype.itemsize*8
    if(sbit>0 and sbit!=byteNum):
        data = data>>(byteNum-sbit)
    return data

def save_tikz(filename,data,x=[],y=[],labels=[],type='Mat'):
    data = np.array(data,dtype=np.float32)
    if type.lower()=='mat':
        if len(x)==0:
            x = np.linspace(0,MM-1,MM)
        if len(y)==0:
            y = np.linspace(0,NN-1,NN)
        x = np.array(x)
        y = np.array(y)
        MM,NN = data.shape
        if x.ndim==1 and y.ndim==1:
            with open(filename, "w") as of:
                for ii in range(len(x)):
                    for jj in range(len(y)):
                        of.write(f'{x[ii]} {y[jj]} {data[jj,ii]}\n')
                    of.write('\n')
        elif x.ndim==2 and y.ndim==2:
            with open(filename, "w") as of:
                for ii in range(NN):
                    for jj in range(MM):
                        of.write(f'{x[ii][jj]} {y[ii][jj]} {data[ii,jj]}\n')
                    of.write('\n')
    
    if type.lower()=='arr':
        labels = np.array(labels)
        if data.ndim==1:
            data = np.reshape(data,(len(data),1))
        MM,NN = data.shape
        if len(x)==MM:
            data = np.insert(data,0,x,axis=1)
            labels=np.insert(labels,0,'x')
        elif len(x)!=0:
            print('Dimension of x does not match!')
        N_label = len(labels)
        labels = list(labels)
        for ii in range(NN):
            temp = f'AnonCol_{ii}'
            if ii>=N_label:
                labels.append(temp)
        with open(filename, "w") as of:
            for ii,lbl in enumerate(labels):
                if ii>0:
                    of.write(' ')
                of.write(lbl)
            of.write('\n')
            for ii in range(MM):
                for jj in range(NN):
                    if jj>0:
                        of.write(' ')
                    of.write(f'{data[ii][jj]}')
                if ii<MM-1:
                    of.write('\n')