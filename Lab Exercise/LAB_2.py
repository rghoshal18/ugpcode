#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

#-------------------------------------------------------------------------------------

def simps(f,a,b,N=50):
    
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

#-------------------------------------------------------------------------------------

def trapz(f,a,b,N=50):
    
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T
#-------------------------------------------------------------------------------------

def derivative(f,a,method='central',h=0.01):
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")
        
#-------------------------------------------------------------------------------------

# A basic code for matrix input from user 

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

# Initialize matrix 

matrix = [] 

print("Enter the entries rowwise:") 


# For user input 
for i in range(R):       # A for loop for row entries 
    a =[] 
    for j in range(C):  # A for loop for column entries 
        a.append(int(input())) 
    matrix.append(a) 

a = [] 
for i in range(R): 
    addp =[]
    for j in range(C):
            addp.append(matrix[i][j])
    a.append(addp)
    
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
        
print("\n")

#-------------------------------------------------------------------------------------

print("Question: 3 ")
print("\n")
print("3rd row of matrix")
for i in range(0,C):
    print(matrix[2][i], end =" ")
print("\n")

#-------------------------------------------------------------------------------------
print("Question: 4 ")
print("\n")
print("4th column of matrix")
print("\n")

for i in range(0,R):
    print(matrix[i][3], end =" ")
print("\n")

#-------------------------------------------------------------------------------------
print("Question: 5 ")
print("\n")
matrix.sort()
print("Sorted matrix")
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end= " ")
    print("\n")


#-------------------------------------------------------------------------------------
print("Question: 6 ")
print("\n")
b = [] 
for i in range(R): 
    p =[]
    for j in range(C):
        if(matrix[i][j] > 2 ):
            p.append(2*matrix[i][j])
        else:
             p.append(matrix[i][j])
    b.append(p)

# Printing The Matrix
for i in range(R): 
    for j in range(C): 
        print(b[i][j], end= " ")
    print("\n")
    
#-------------------------------------------------------------------------------------

print("Question: 7 ")
print("\n")

addm = [] 
for i in range(R): 
    addp =[]
    for j in range(C):
            l = matrix[i][j] + b[i][j]
            addp.append(l)
    addm.append(addp) 
    
# Printing The Matrix
for i in range(R): 
    for j in range(C): 
        print(addm[i][j], end= " ")
    print("\n")
    
#-------------------------------------------------------------------------------------

print("Question: 8 ")
print("\n")

subm = [] 
for i in range(R): 
    addp =[]
    for j in range(C):
            l = matrix[i][j] - b[i][j]
            addp.append(l)
    subm.append(addp)
    
    
# Printing The Matrix
for i in range(R): 
    for j in range(C): 
        print(subm[i][j], end= " ")
    print("\n")
    
#-------------------------------------------------------------------------------------
print("Question: 9 ")
print("\n")

result = [] 
for i in range(R): 
    addp =[]
    for j in range(C):
            addp.append(0)
    result.append(addp) 

# iterating by row of A 
for i in range(len(a)):   
    # iterating by coloum by B  
    for j in range(len(b[0])): 
        # iterating by rows of B 
        for k in range(len(b)): 
            result[i][j] += a[i][k] * b[k][j] 

# Printing The Matrix
for i in range(R): 
    for j in range(C): 
        print(result[i][j], end= " ")
    print("\n")
    
#-------------------------------------------------------------------------------------
print("Question: 10 ")
print("\n")   
newm = []
for i in range(R): 
    addp =[]
    for j in range(C):
            addp.append(a[i][j]/18)
    newm.append(addp)

print("Dividing each element of matrix 'a' by 18 ")
# Printing The Matrix
for i in range(R): 
    for j in range(C): 
        print(newm[i][j], end= " ")
    print("\n")
    
newmat = []
for i in range(R): 
    addp =[]
    for j in range(C):
            addp.append(b[i][j]/18)
    newmat.append(addp)
    
print("Dividing each element of matrix 'b' by 18 ")
# Printing The Matrix
for i in range(R): 
    for j in range(C): 
        print(newmat[i][j], end= " ")
    print("\n")

#-------------------------------------------------------------------------------------

print("Question: 11 ")
print("\n") 
print("Inverse of matrix 'a'")
x = np.array(a) 
y = np.linalg.inv(x)
ra = np.linalg.matrix_rank(x)
con = np.linalg.cond(x)
noo = np.linalg.norm(x)
sv =   np.linalg.svd(x)

# Printing The Matrix
for i in range(R): 
    for j in range(C): 
        print(y[i][j], end= " ")
    print("\n")

print("Rank of matrix 'a' " + str(ra))
print("Condition number of matrix 'a': " + str(con))
print("Norm of matrix a")
print(noo)
print("SVD of matrix 'a': " + str(sv))
print("Inverse of matrix 'b'")
x = np.array(b) 
y = np.linalg.inv(x)
ra = np.linalg.matrix_rank(x)
con = np.linalg.cond(x)
noo = np.linalg.norm(x)
sv =   np.linalg.svd(x)
# Printing The Matrix
for i in range(R): 
    for j in range(C): 
        print(y[i][j], end= " ")
    print("\n")
    
print("Rank of matrix 'b'" + str(ra))
print("Condition number of matrix 'b': " + str(con))
print("Norm of matrix 'b': ")
print(noo)
print("SVD of matrix 'b': " + str(sv))

#-------------------------------------------------------------------------------------
print("Question: 13 ")
print("\n") 

print("Exp(x): ")
print(derivative(np.exp,0.5,h=0.01))
print("Cos(x): ")
print(derivative(np.cos,0.5,h=0.01))

#-------------------------------------------------------------------------------------
print("Question: 14 ")
print("\n")

print("Trapezoidal Rule: ")
print("Exp(x): ")
print(trapz(np.exp,0,1.57,50))
print("Cos(x): ")
print(trapz(np.cos,0,1.57,50))

#-------------------------------------------------------------------------------------
print("Question: 15 ")
print("\n")

print("Simpson Rule: ")
print("Exp(x): ")
print(simps(np.exp,0,1.57,50))
print("Cos(x): ")
print(simps(np.cos,0,1.57,50))
#-------------------------------------------------------------------------------------

