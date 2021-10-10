# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import numpy as np
import numpy as np
a11=int(input("enter the a11: "))
a12=int(input("enter the a12.: "))
a13=int(input("enter the a13: "))
a21=int(input("enter the a21: "))
a22=int(input("enter the a22: "))
a23=int(input("enter the a23: "))
a31=int(input("enter the a31: "))
a32=int(input("enter the a32: "))
a33=int(input("enter the a33: "))
M=[[a11,a12,a13],
[a21,a22,a23],
[a31,a32,a33]]
I=[[1,0,0],
[0,1,0],
[0,0,1]]
M1=np.array(M)
I1=np.array(I)
print("the matrix to find its inverse is: ")
print(M1)
print("--------------------")
for i in range(3):
  n=M1[i][i]
  n1=[n,n,n]
  n2=np.array(n1)
  iden1=M1[i]/n2
  inv1=I1[i]/n2
  M1=M1.tolist()
  I1=I1.tolist()
  inv1=list(inv1)
  iden1=list(iden1)
  del(M1[i])
  del(I1[i])
  if i==0:
    M1=[iden1]+M1
    M1=np.array(M1)
    I1=[inv1]+I1
    I1=np.array(I1)
    for j in range(1,3):
      m=M1[j][i]
      M1[j]=M1[j]-(m*M1[i])
      I1[j]=I1[j]-(m*I1[i])
  elif i==1:
    M1=[M1[0]]+[iden1]+[M1[1]]
    M1=np.array(M1)
    I1=[I1[0]]+[inv1]+[I1[1]]
    I1=np.array(I1)
    for j in range(0,3,2): 
      m=M1[j][i]
      M1[j]=M1[j]-(m*M1[i])
      I1[j]=I1[j]-(m*I1[i])
      
  elif i==2:
    M1=M1 +[iden1]
    M1=np.array(M1)
    I1=I1+[inv1]
    I1=np.array(I1)
    for j in range(0,2):
      m=M1[j][i]
      M1[j]=M1[j]-(m*M1[i])
      I1[j]=I1[j]-(m*I1[i])
print("the inverse of the matrix is: ")
print(I1)
print("--------------------")
print("we get the identity matrix too!!!!!")
print(M1)


