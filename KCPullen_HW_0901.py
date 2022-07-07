# Keiland Pullen
# DSC 430: Python Programming
# Due Date 11/19/2019
# Link to video: https://youtu.be/A0JRmttQc80
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0901: Numpy Intro

import numpy as np             # import NumPy module

a = np.arange(0, 100, 1)       # NumPy to create an array

print("a = ",a); print()

b = np.arange(0, 100, 10)       # NumPy to create an array
print("b = ", b); print()

c = np.linspace(0, 10, num=10, endpoint=True) #NumPy to create an array
print("c = ", c); print()

d = np.random.rand(10,10)       # NumPy to create random 10 x 10 matrix
print("d = ", d); print()

a = a.reshape(10,10)            # NumPy.reshape to reshape a matrix
print("a reshaped = ",a); print()

print ("a[4,5] = ", a[4,5]); print()

print("a[4] = ", a[4]); print()

sumd = np.sum(d);               # NumPy.sum to find the sum of a matrix
print ("sum of d = ", sumd); print()

maxa = np.max(a)                # NumPy.max to find the Max value of a matrix
print ("max of a = ", maxa); print()

transb = np.transpose(b)        # NumPy.transpose to transpose a matrix
print("transpose of b = ",transb); print()

aplusd = np.add(a, d)           # NumPy.add to add 2 matrices
print("a + d = ", aplusd); print()

atimesd = np.multiply(a, d)     # NumPy.multiply to multiply 2 matrices
print("a * d = ", atimesd); print()

adotd = np.dot(a, d)            # NumPy.dot to calculate the dot product of 2 matrices
print("a dot d = ",adotd)


