Algorithm 1. OnWallIneffectiveCollision(molecule)
Input: molecule [1,2,...,n]
Output: new_molecule
    1. new_molecule = molecule
    2. Generate two random numbers i,j ranging from 0 to n
    3. if (molecule[i] + j <= len(molecule)) then
    4.    new_molecule[i] = molecule[i] + j
    5. else
    6.    if(molecule[i]>j) then
    7.        new_molecule[i] = molecule[i] - j
    8.    else
    9.        new_molecule[i] =  j - molecule[i]
    10.    end if
    11. end if


Algorithm 2. Decomposition(molecule)
Input: molecule [1,2,...,n]
Output: new_molecule1, new_molecule2
    1. mid = n/2
    2. Copy values from 0 to mid-1 positions of molecule into new_molecule1
    3. Copy values from mid to n-1 positions of molecule into new_molecule2
    4. Generate random values ranging from 0 to n and assign 0 to mid-1 positions of new_molecule1
    5. Generate random values ranging from 0 to n and assign mid to n-1 positions of new_molecule2


Algorithm 3. InermolecularIneffectiveCollision(molecule1, molecule2)
Input: molecule1 [1,2,...,n], molecule2 [1,2,...,n]
Output: new_molecule1, new_molecule2
    1. Generate two random numbers x,y ranging from 0 to n
    2. for i in range 0 to n do
    3.     if (i<x or i>y) then
    4.         new_molecule1[i] = molecule1[i]
    5.         new_molecule2[i] = molecule2[i]
    6.     else if (x<=i and i<=y)
    7.         new_molecule1[i] = molecule2[i]
    8.         new_molecule2[i] = molecule1[i]
    9.     end if
    10. end for

Algorithm 4. Synthesis(molecule1, molecule2)
Input: molecule1 [1,2,...,n], molecule2 [1,2,...,n]
Output: new_molecule
    1. for i in range 0 to n do
    2.     Generate a random variable r uniformly distributed over 0 to 1
    3.     if(r<0.5) then
    4.         new_molecule[i] = molecule1[i]
    5.     else
    6.         new_molecule[i] = molecule2[i]
    7.     end if
    8. end for