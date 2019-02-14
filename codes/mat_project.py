import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
A = np.array([2,3])
B = np.array([4,5])
p_1 = -3
p_2 = np.matmul(A,A)-np.matmul(B,B)
P = np.array([p_1,p_2])
n_1_T = np.array([-1,4])
n_2_T = 2*(np.array(A-B))
N = np.vstack((n_1_T,n_2_T))
centre = np.matmul(np.linalg.inv(N),P)
radius = np.linalg.norm((centre-A))
print(radius)
#Plotting circle given the radius and centre
circle = plt.Circle((centre[0],centre[1]),radius,fill=False)
ax = plt.gca()
ax.set_xlim((-15,15))
ax.set_ylim((-11,11))
ax.add_patch(circle)
plt.plot(centre[0],centre[1],'o')#Plotting centre of circle
plt.text(centre[0]*(1+0.1),centre[1]*(1-0.5),'O')
#Plotting the given line using two points on the line
len = 10
lam_1 = np.linspace(-9,9,len)
lam_2 = np.linspace(0,1,len)
X = np.array([3,0])
Y = np.array([7,1])
x_XY = np.zeros((2,len))
x_OA = np.zeros((2,len))
for i in range(len):
	temp1 = X + lam_1[i]*(Y-X)
	x_XY[:,i] = temp1.T
	temp2 = centre + lam_2[i]*(A-centre)
	x_OA[:,i] = temp2.T
plt.plot(x_XY[0,:],x_XY[1,:],label='$-x+4y+3=0$')
plt.plot(x_OA[0,:],x_OA[1,:],label='$Radius$')
plt.legend(loc='best')
#Plotting first point through which circle passes
plt.plot(A[0],A[1],'o')
plt.text(-1,A[1]*(1-0.1),'A(2,3)')
#Plotting second point through which circle passes
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1+0.1),B[1]*(1-0.1),'B(4,5)')
plt.grid()
plt.savefig('/home/stavan/Documents/ML/Plot.eps')
plt.savefig('/home/stavan/Documents/ML/Plot.pdf')
plt.show()
