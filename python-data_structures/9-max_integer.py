#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    
    m_v = my_list[0]

    for v in my_list[1:]:
        if v > m_v:
            m_v = v
        
    return m_v

