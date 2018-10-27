Algorithm 1. OnWallIneffectiveCollision(m1)
Input: m1 [1,2,...,n]
Output: m2
    1. m2 = m1
    2. Generate two random numbers i,j ranging from 0 to n
    3. if (m1[i] + j <= len(m1)) then
    4.    m2[i] = m1[i] + j
    5. else
    6.    if(m1[i]>j) then
    7.        m2[i] = m1[i] - j
    8.    else
    9.        m2[i] =  j - m1[i]
    10.    end if
    11. end if


Algorithm 2. Decomposition(m1)
Input: m1 [1,2,...,n]
Output: m2, m3
    1. mid = n/2
    2. Copy values from 0 to mid-1 positions of m1 into m2
    3. Copy values from mid to n-1 positions of m1 into m3
    4. Generate random values ranging from 0 to n and assign 0 to mid-1 positions of m2
    5. Generate random values ranging from 0 to n and assign mid to n-1 positions of m3


Algorithm 3. InermolecularIneffectiveCollision(m1, m2)
Input: m1 [1,2,...,n], m2 [1,2,...,n]
Output: m2, m3
    1. Generate two random numbers x,y ranging from 0 to n
    2. for i in range 0 to n do
    3.     if (i<x or i>y) then
    4.         m2[i] = m1[i]
    5.         m3[i] = m2[i]
    6.     else if (x<=i and i<=y)
    7.         m2[i] = m2[i]
    8.         m3[i] = m1[i]
    9.     end if
    10. end for

Algorithm 4. Synthesis(m1, m2)
Input: m1 [1,2,...,n], m2 [1,2,...,n]
Output: m2
    1. for i in range 0 to n do
    2.     Generate a random variable r uniformly distributed over 0 to 1
    3.     if(r<0.5) then
    4.         m2[i] = m1[i]
    5.     else
    6.         m2[i] = m2[i]
    7.     end if
    8. end for

Algorithm 5. RepairHP(m_list)
Input: m_list [m1,m2,...,mn]
Output: m_list1
    1. m_list1 = m_list
    2. for i in range 0 to n do
    3.      start,end,length = m_list[i]
    4.       hp = ((end-length+1) - (start+length))
    5.       if(hp<1):
    6.           length = length-1
    7.           m_list1[i] =  start,end,length
    8.       end if
    9.  end for

Algorithm Molecule_CRO()
    1. PopulationGeneration()
    2. RepairHP()
    3. KE <- InitialKE
    4. PE <- f(w)
    5. NumHit <- 0
    6. MinHit <- 0
    7. MinPE <- PE
    8. MinStruct <- Struct

Algorithm PopulationGeneration()
1.  Input : sequence,popSize
2.  for i = 0 to sequence_length do
    3.  for j = 0 to i do
        4.  if j < i do
            5.  if sequence [i] and sequence [j] form base pair then
                6.  zero_one[i, j] = 1
            7.  else
                8.  zero_one[i, j] = 0
            9.  end if
        10. end if
    11. end for
12. end for

13. for i = (sequence length -1) to 0 do
    14. for j = 0 to (sequence length - 2) do
        15. if diagonal 1 found then
            16. trace the first and last position and length and assign information table.
        17. end if.
    18. end for
19. end for
18. for i = 0 to popSize do
    20. sequence_number :- randomly generate an array where each value is between 0 to information table length.
    21. Add sequence number in the molecule list.
22. end for
