'''
You are given three integers x,y,z  and  representing the dimensions of
a cuboid along with an integer n. You have to print a list of all possible 
coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n . Here, 

Four integers x,y,z,n each on four separate lines, respectively.
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    L = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(L)
