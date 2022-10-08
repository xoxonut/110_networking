from sympy import *
from itertools import cycle
from time import process_time
import random
N=4
omega = [[exp(2*pi*I/N*n*m) for n in range(N)]for m in range(N)]
inputData=[1,2,3,4]
outputData=[]
output1=0

for i in omega:
    outputData.append(simplify(sum( m*n for m,n in zip(inputData,i)))/N)

print(*outputData,sep='\n',end='\n\n')

def FFT(l,n):
    def FFT_helper(l,n):
        if n==1 : return l 
        omega=[exp(2*pi*I/n*m) for m in range(n)]
        ODD=FFT_helper(list(filter(lambda x: l.index(x)%2==0,l)),n//2)
        EVEN=FFT_helper(list(filter(lambda x: l.index(x)%2!=0,l)),n//2)
        return [simplify(i+o*j) for o,i,j in zip(omega,cycle(ODD),cycle(EVEN))]
    return[i/n for i in FFT_helper(l,n)]

FFTData=FFT(inputData,N)
print(*FFTData,sep='\n',end='\n')


