def decomposition (molecule)
        
    int[] m1 = new int[m.Length]
    int[] m2 = new int[m.Length]
    int mid = m.Length / 2
    for (int i = 0 i < mid i++ )
    
        m1[i] = m[i]
    
    for (int i = mid i < m.Length i++ )
    
        m2[i] = m[i]
    
    for (int i = mid i < m.Length i++ )
    
        for (int i1 = 0 i1 < 4000 i1++)
        
            for (int i2 = 0 i2 < 2000 i2++)
            

            
        

        m1[i] = rand.Next(0, m.Length)
    
    for (int i = 0 i < mid i++)
    
        for (int i1 = 0 i1 < 4000 i1++)
        
            for (int i2 = 0 i2 < 2000 i2++)
            

            
        

        m2[i] = rand.Next(0, m.Length)
    
    m_new.Add(m1)
    m_new.Add(m2)

    return m_new
        
    